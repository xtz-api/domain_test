import logging
from test_cases.api_ic_base import IcService


class IcInfoAPI(IcService):
    def get_GetButlerInfo(self, **kwargs):
        """获取企业认证管家订单详情"""
        params = {
            "ButlerID": self.BankID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def get_ListButlerInfos(self, **kwargs):
        """获取企业认证管家订单列表"""
        params = {
            "ButlerID": self.BankID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp
