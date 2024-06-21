from util.requests_volcauth.volcauth import VolcAuth


def get_volc_auth(idc, access_key, secret_key, region, service):
    if not idc or idc == "boe" or idc == "online":
        auth = VolcAuth(access_key, secret_key, region, service)
        return auth
    else:
        return

