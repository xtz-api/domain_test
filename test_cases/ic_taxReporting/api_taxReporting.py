import logging
from test_cases.api_ic_base import IcService


class IcInfoAPI(IcService):

    def get_GetTaxReportingInfo(self, **kwargs):
        """获取税务报道详情"""
        params = {
            "TaxID": self.TaxID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def get_ListTaxReportingInfos(self, **kwargs):
        """获取税务报道订单列表"""
        params = {
            "TaxID": self.TaxID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def post_SubmitTaxReportingMaterial(self, data, **kwargs):
        """提交税务报道审核资料"""
        params = {
            "TaxID": self.TaxID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params, data=data)
        return _, resp
