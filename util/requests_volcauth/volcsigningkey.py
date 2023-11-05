import hmac
import hashlib
from warnings import warn
from datetime import datetime
from six import text_type


class VolcSigningKey:
    def __init__(self, secret_key, region, service, date=None,
                 store_secret_key=True):
        self.region = region
        self.service = service
        self.date = date or datetime.utcnow().strftime('%Y%m%d')
        self.scope = '{}/{}/{}/request'.format(self.date, self.region, self.service)
        self.store_secret_key = store_secret_key
        self.secret_key = secret_key if self.store_secret_key else None
        self.key = self.generate_key(secret_key, self.region, self.service, self.date)

    @classmethod
    def generate_key(cls, secret_key, region, service, date,
                     intermediates=False):
        init_key = secret_key.encode('utf-8')
        date_key = cls.sign_sha256(init_key, date)
        region_key = cls.sign_sha256(date_key, region)
        service_key = cls.sign_sha256(region_key, service)
        key = cls.sign_sha256(service_key, 'request')
        if intermediates:
            return key, date_key, region_key, service_key
        else:
            return key

    @staticmethod
    def sign_sha256(key, msg):
        if isinstance(msg, text_type):
            msg = msg.encode('utf-8')
        return hmac.new(key, msg, hashlib.sha256).digest()

    @property
    def amz_date(self):
        msg = ("This attribute has been renamed to 'date'. 'amz_date' is "
               "deprecated and will be removed in a future version.")
        warn(msg, DeprecationWarning)
        return self.date
