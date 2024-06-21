import pytest
from util.volc_api.volc_constant import VOLC_IC_CONSTANT_OPENAPI, VOLC_IC_CONSTANT
from util.volc_api.volc_client_model import VolcClientConfig
from util.auth import get_volc_auth


# PS：这个是工商的
@pytest.fixture(scope="session")
def volc_ic_client(idc, env):
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_IC_CONSTANT.AK_2
        sk = VOLC_IC_CONSTANT.SK_2
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_IC_CONSTANT.AK_ONLINE
        sk = VOLC_IC_CONSTANT.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_IC_CONSTANT.REGION,
                                     VOLC_IC_CONSTANT.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client


# PS：等到工商有openApi时再对接信息
@pytest.fixture(scope="session")
def volc_ic_client_openapi(idc, env):
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
        ak = VOLC_IC_CONSTANT_OPENAPI.AK_2
        sk = VOLC_IC_CONSTANT_OPENAPI.SK_2
    elif idc == "online":
        host = "http://open.volcengineapi.com"
        ak = VOLC_IC_CONSTANT_OPENAPI.AK_ONLINE
        sk = VOLC_IC_CONSTANT_OPENAPI.SK_ONLINE
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"
    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, ak, sk, VOLC_IC_CONSTANT_OPENAPI.REGION,
                                     VOLC_IC_CONSTANT_OPENAPI.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client
