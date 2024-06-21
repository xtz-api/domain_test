import hmac
import hashlib
import posixpath
import re
import shlex
import datetime
import collections.abc as abc
from urllib.parse import urlparse, parse_qs, quote, unquote
from requests.auth import AuthBase
from six import PY2, text_type
from .volcsigningkey import VolcSigningKey
from .exceptions import DateMismatchError, NoSecretKeyError, DateFormatError


class VolcAuth(AuthBase):
    default_include_headers = {'host', 'content-type', 'date', 'x-*'}

    def __init__(self, *args, **kwargs):
        l = len(args)
        if l not in [2, 4, 5]:
            msg = 'VolcAuth() takes 2, 4 or 5 arguments, {} given'.format(l)
            raise TypeError(msg)
        self.access_id = args[0]
        if isinstance(args[1], VolcSigningKey) and l == 2:
            # instantiate from signing key
            self.signing_key = args[1]
            self.region = self.signing_key.region
            self.service = self.signing_key.service
            self.date = self.signing_key.date
        elif l in [4, 5]:
            # instantiate from args
            secret_key = args[1]
            self.region = args[2]
            self.service = args[3]
            self.date = args[4] if l == 5 else None
            self.signing_key = None
            self.regenerate_signing_key(secret_key=secret_key)
        else:
            raise TypeError()

        raise_invalid_date = kwargs.get('raise_invalid_date', False)
        if raise_invalid_date in [True, False]:
            self.raise_invalid_date = raise_invalid_date
        else:
            raise ValueError('raise_invalid_date must be True or False in VolcAuth.__init__()')

        self.session_token = kwargs.get('session_token')
        if self.session_token:
            self.default_include_headers.add('x-security-token')

        self.include_hdrs = set(self.default_include_headers)

        # if the key exists and it's some sort of listable object, use it.
        if 'include_hdrs' in kwargs and isinstance(kwargs['include_hdrs'], abc.Iterable):
            self.include_hdrs = set(kwargs['include_hdrs'])

        AuthBase.__init__(self)

    def regenerate_signing_key(self, secret_key=None, region=None,
                               service=None, date=None):
        if secret_key is None and (self.signing_key is None or self.signing_key.secret_key is None):
            raise NoSecretKeyError

        secret_key = secret_key or self.signing_key.secret_key
        region = region or self.region
        service = service or self.service
        date = date or self.date
        if self.signing_key is None:
            store_secret_key = True
        else:
            store_secret_key = self.signing_key.store_secret_key

        self.signing_key = VolcSigningKey(secret_key, region, service, date,
                                          store_secret_key)

        self.region = region
        self.service = service
        self.date = self.signing_key.date

    def __call__(self, req):
        # check request date matches scope date
        req_date = self.get_request_date(req)
        if req_date is None:
            if 'date' in req.headers:
                del req.headers['date']
            if 'x-date' in req.headers:
                del req.headers['x-date']
            now = datetime.datetime.utcnow()
            req_date = now.date()
            req.headers['x-date'] = now.strftime('%Y%m%dT%H%M%SZ')
        req_scope_date = req_date.strftime('%Y%m%d')
        if req_scope_date != self.date:
            self.handle_date_mismatch(req)

        # encode body and generate body hash
        if hasattr(req, 'body') and req.body is not None:
            self.encode_body(req)
            content_hash = hashlib.sha256(req.body)
            # print("content_hash: %s" % content_hash)
        else:
            content_hash = hashlib.sha256(b'')
        req.headers['x-content-sha256'] = content_hash.hexdigest()
        if self.session_token:
            req.headers['x-security-token'] = self.session_token

        # generate signature
        result = self.get_canonical_headers(req, self.include_hdrs)
        cano_headers, signed_headers = result
        cano_req = self.get_canonical_request(req, cano_headers,
                                              signed_headers)
        sig_string = self.get_sig_string(req, cano_req, self.signing_key.scope)
        sig_string = sig_string.encode('utf-8')
        hsh = hmac.new(self.signing_key.key, sig_string, hashlib.sha256)
        sig = hsh.hexdigest()
        auth_str = 'HMAC-SHA256 '
        auth_str += 'Credential={}/{}, '.format(self.access_id,
                                                self.signing_key.scope)
        auth_str += 'SignedHeaders={}, '.format(signed_headers)
        auth_str += 'Signature={}'.format(sig)
        req.headers['Authorization'] = auth_str
        return req

    @classmethod
    def get_request_date(cls, req):
        date = None
        for header in ['x-date', 'date']:
            if header not in req.headers:
                continue
            try:
                date_str = cls.parse_date(req.headers[header])
            except DateFormatError:
                continue
            try:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                continue
            else:
                break

        return date

    @staticmethod
    def parse_date(date_str):
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug',
                  'sep', 'oct', 'nov', 'dec']
        formats = {
            # RFC 7231, e.g. 'Mon, 09 Sep 2011 23:36:00 GMT'
            r'^(?:\w{3}, )?(\d{2}) (\w{3}) (\d{4})\D.*$':
                lambda m: '{}-{:02d}-{}'.format(
                    m.group(3),
                    months.index(m.group(2).lower()) + 1,
                    m.group(1)),
            # RFC 850 (e.g. Sunday, 06-Nov-94 08:49:37 GMT)
            # assumes current century
            r'^\w+day, (\d{2})-(\w{3})-(\d{2})\D.*$':
                lambda m: '{}{}-{:02d}-{}'.format(
                    str(datetime.date.today().year)[:2],
                    m.group(3),
                    months.index(m.group(2).lower()) + 1,
                    m.group(1)),
            # C time, e.g. 'Wed Dec 4 00:00:00 2002'
            r'^\w{3} (\w{3}) (\d{1,2}) \d{2}:\d{2}:\d{2} (\d{4})$':
                lambda m: '{}-{:02d}-{:02d}'.format(
                    m.group(3),
                    months.index(m.group(1).lower()) + 1,
                    int(m.group(2))),
            # x-date format dates, e.g. 20100325T010101Z
            r'^(\d{4})(\d{2})(\d{2})T\d{6}Z$':
                lambda m: '{}-{}-{}'.format(*m.groups()),
            # ISO 8601 / RFC 3339, e.g. '2009-03-25T10:11:12.13-01:00'
            r'^(\d{4}-\d{2}-\d{2})(?:[Tt].*)?$':
                lambda m: m.group(1),
        }

        out_date = None
        for regex, xform in formats.items():
            m = re.search(regex, date_str)
            if m:
                out_date = xform(m)
                break
        if out_date is None:
            raise DateFormatError
        else:
            return out_date

    def handle_date_mismatch(self, req):
        req_datetime = self.get_request_date(req)
        new_key_date = req_datetime.strftime('%Y%m%d')
        self.regenerate_signing_key(date=new_key_date)

    @staticmethod
    def encode_body(req):
        if isinstance(req.body, text_type):
            split = req.headers.get('content-type', 'text/plain').split(';')
            if len(split) == 2:
                ct, cs = split
                cs = cs.split('=')[1]
                req.body = req.body.encode(cs)
            else:
                ct = split[0]
                if (ct == 'application/x-www-form-urlencoded' or 'x-' in ct):
                    req.body = req.body.encode()
                else:
                    req.body = req.body.encode('utf-8')
                    req.headers['content-type'] = ct + '; charset=utf-8'

    def get_canonical_request(self, req, cano_headers, signed_headers):
        url = urlparse(req.url)
        path = self.volc_cano_path(url.path)
        split = req.url.split('?', 1)
        qs = split[1] if len(split) == 2 else ''
        qs = self.volc_cano_querystring(qs)
        payload_hash = req.headers['x-content-sha256']
        req_parts = [req.method.upper(), path, qs, cano_headers,
                     signed_headers, payload_hash]
        cano_req = '\n'.join(req_parts)
        return cano_req

    @classmethod
    def get_canonical_headers(cls, req, include=None):
        if include is None:
            include = cls.default_include_headers
        include = [x.lower() for x in include]
        headers = req.headers.copy()
        if 'host' not in headers:
            headers['host'] = urlparse(req.url).netloc.split(':')[0]
        cano_headers_dict = {}
        for hdr, val in headers.items():
            hdr = hdr.strip().lower()
            val = cls.volc_norm_whitespace(val).strip()
            if (hdr in include or '*' in include
                    or ('x-*' in include and hdr.startswith('x-')
                        and not hdr == 'x-client-context')):
                vals = cano_headers_dict.setdefault(hdr, [])
                vals.append(val)
        cano_headers = ''
        signed_headers_list = []
        for hdr in sorted(cano_headers_dict):
            vals = cano_headers_dict[hdr]
            val = ','.join(sorted(vals))
            cano_headers += '{}:{}\n'.format(hdr, val)
            signed_headers_list.append(hdr)
        signed_headers = ';'.join(signed_headers_list)
        return (cano_headers, signed_headers)

    @staticmethod
    def get_sig_string(req, cano_req, scope):
        date = req.headers['x-date']
        hsh = hashlib.sha256(cano_req.encode())
        sig_items = ['HMAC-SHA256', date, scope, hsh.hexdigest()]
        sig_string = '\n'.join(sig_items)
        return sig_string

    def volc_cano_path(self, path):
        safe_chars = '/~'
        qs = ''
        fixed_path = path
        if '?' in fixed_path:
            fixed_path, qs = fixed_path.split('?', 1)
        fixed_path = posixpath.normpath(fixed_path)
        fixed_path = re.sub('/+', '/', fixed_path)
        if path.endswith('/') and not fixed_path.endswith('/'):
            fixed_path += '/'
        full_path = fixed_path
        # If Python 2, switch to working entirely in str as quote() has problems
        # with Unicode
        if PY2:
            full_path = full_path.encode('utf-8')
            safe_chars = safe_chars.encode('utf-8')
            qs = qs.encode('utf-8')
        # S3 seems to require unquoting first. 'host' service is used in
        if self.service in ['s3', 'host']:
            full_path = unquote(full_path)
        full_path = quote(full_path, safe=safe_chars)
        if qs:
            qm = b'?' if PY2 else '?'
            full_path = qm.join((full_path, qs))
        if PY2:
            full_path = unicode(full_path)
        return full_path

    @staticmethod
    def volc_cano_querystring(qs):
        safe_qs_chars = '&=+'
        safe_qs_unresvd = '-_.~'
        # If Python 2, switch to working entirely in str
        # as quote() has problems with Unicode
        if PY2:
            qs = qs.encode('utf-8')
            safe_qs_chars = safe_qs_chars.encode()
            safe_qs_unresvd = safe_qs_unresvd.encode()
        qs = unquote(qs)
        space = b' ' if PY2 else ' '
        qs = qs.split(space)[0]
        qs = quote(qs, safe=safe_qs_chars)
        qs_items = {}
        for name, vals in parse_qs(qs, keep_blank_values=True).items():
            name = quote(name, safe=safe_qs_unresvd)
            vals = [quote(val, safe=safe_qs_unresvd) for val in vals]
            qs_items[name] = vals
        qs_strings = []
        for name, vals in qs_items.items():
            for val in vals:
                qs_strings.append('='.join([name, val]))
        qs = '&'.join(sorted(qs_strings))
        if PY2:
            qs = unicode(qs)
        return qs

    @staticmethod
    def volc_norm_whitespace(text):
        """
        Replace runs of whitespace with a single space.

        Ignore text enclosed in quotes.

        """
        return ' '.join(shlex.split(text, posix=False))


class StrictVolcAuth(VolcAuth):
    def handle_date_mismatch(self, req):
        raise DateMismatchError


class PassiveVolcAuth(VolcAuth):
    def handle_date_mismatch(self, req):
        pass
