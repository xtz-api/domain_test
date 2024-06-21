import pytest
from util.volc_api.volc_constant import VOLC_DOMAIN_CONSTANT, VOLC_DOMAIN_CONSTANT_OPENAPI
from util.volc_api.volc_client_model import VolcClientConfig
from util.auth import get_volc_auth


@pytest.fixture(scope="session")
def volc_domain_client(idc, env):
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_DOMAIN_CONSTANT.AK_2
        sk = VOLC_DOMAIN_CONSTANT.SK_2
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_DOMAIN_CONSTANT.AK_ONLINE
        sk = VOLC_DOMAIN_CONSTANT.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_DOMAIN_CONSTANT.REGION,
                                     VOLC_DOMAIN_CONSTANT.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client


@pytest.fixture(scope="session")
def volc_domain_client_openapi(idc, env):
    """auto-tgm-2100266070"""
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_2
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_2
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_ONLINE
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_DOMAIN_CONSTANT_OPENAPI.REGION,
                                     VOLC_DOMAIN_CONSTANT_OPENAPI.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client


@pytest.fixture(scope="session")
def volc_domain_client_openapi_gogokid(idc, env):
    """gogokid-2100000056"""
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_ONLINE
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_DOMAIN_CONSTANT_OPENAPI.REGION,
                                     VOLC_DOMAIN_CONSTANT_OPENAPI.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client


@pytest.fixture(scope="session")
def volc_domain_client_openapi_d1(idc, env):
    """
    DomianTest1账号
    """
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_Domaintest1
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_Domaintest1
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_ONLINE
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_DOMAIN_CONSTANT_OPENAPI.REGION,
                                     VOLC_DOMAIN_CONSTANT_OPENAPI.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client


@pytest.fixture(scope="session")
def volc_domain_client_openapi_d2(idc,env):
    """domaintest2-2100056829"""
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_Domaintest2
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_Domaintest2
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_DOMAIN_CONSTANT_OPENAPI.AK_ONLINE
        sk = VOLC_DOMAIN_CONSTANT_OPENAPI.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_DOMAIN_CONSTANT_OPENAPI.REGION,
                                     VOLC_DOMAIN_CONSTANT_OPENAPI.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client