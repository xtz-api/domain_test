import pytest
from util.volc_api.volc_constant import VOLC_DOMAIN_CONSTANT
from util.volc_api.volc_client_model import VolcClientConfig
from util.auth import get_volc_auth


@pytest.fixture(scope="session")
def volc_domnain_client(idc, env):
    volc_client = VolcClientConfig()

    # 获取host
    if not idc or idc == "boe":
        host = "http://volcengineapi-boe.byted.org"
    else:
        # logging.error("请修改代码，设置不同线上机房使用的火山网关host！！！")
        host = "http://volcengineapi.byted.org"

    volc_client.host = host

    # 设置请求头
    volc_client.headers["X-TT-Env"] = env
    volc_client.headers["Content-Type"] = "application/json;charset=UTF-8"
    volc_client.headers["Debug-Mode"] = "True"  # True：展示详细错误

    # 获取鉴权
    volc_client.auth = get_volc_auth(idc, VOLC_DOMAIN_CONSTANT.AK, VOLC_DOMAIN_CONSTANT.SK, VOLC_DOMAIN_CONSTANT.REGION,
                                     VOLC_DOMAIN_CONSTANT.SERVICE)
    # EnvConfig.AuthServer = CONSTANT.AuthServerVolcBOE
    return volc_client
