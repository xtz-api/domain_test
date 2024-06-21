import logging
from test_cases.api_ic_base import IcService


class IcInfoAPI(IcService):
    def post_CreatePreOrder(self, data, **kwargs):
        """创建预配置火山订单--银行开户订单"""
        params = {
            "BankID": self.BankID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params, data=data)
        return _, resp

    def get_GetOpenBankInfo(self, **kwargs):
        """获取银行开户详情"""
        params = {
            "BankID": self.BankID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def get_ListOpenBankInfos(self, **kwargs):
        """获取银行开户订单列表"""
        params = {
            "BankID": self.BankID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def post_SubmitOpenBankMaterial(self, data, **kwargs):
        """提交银行开户审核资料"""
        params = {
            "BankID": self.BankID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params, data=data)
        return _, resp
