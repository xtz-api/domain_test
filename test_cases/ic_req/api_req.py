import logging
from test_cases.api_ic_base import IcService


class IcReqAPI(IcService):

    def post_createReq(self, data, **kwargs):
        """创建需求单"""
        params = {
            "OpportunityID": self.OpportunityID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreateReq(params=params, data=data)
        return _, resp

    def get_listReq(self, **kwargs):
        """获取需求列表"""
        params = {
            "OpportunityID": self.OpportunityID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.ListReq(params=params)
        return _, resp

    def get_getReq(self, **kwargs):
        """获取需求单详情"""
        params = {
            "OpportunityID": self.OpportunityID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.GetReq(params=params)
        return _, resp

    # def post_closeReq(self, data, **kwargs):
    #     """关闭商机需求"""
    #     params = {
    #         "OpportunityID": self.OpportunityID
    #     }
    #     params.update(**kwargs)
    #     logging.info(kwargs)
    #     _, resp = self.api.CloseReq(data=data, params=params)
    #     return _, resp

    def post_CreatePreOrder(self, data, **kwargs):
        """创建工商预配置火山订单"""
        params = {
            "OpportunityID": self.OpportunityID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(data=data, params=params)
        return _, resp

    def post_CreateQualificationOrder(self, data, **kwargs):
        """创建资质预配置火山订单"""
        params = {
            "OpportunityID": self.OpportunityID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreateQualificationOrder(data=data, params=params)
        return _, resp
