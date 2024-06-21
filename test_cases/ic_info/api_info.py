import logging
from test_cases.api_ic_base import IcService


class IcInfoAPI(IcService):
    def post_CreatePreOrder(self, data, **kwargs):
        """创建预配置火山订单--工商订单"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params, data=data)
        return _, resp

    def post_SaveICRegmaterial(self, data, **kwargs):
        """暂存注册资料"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.SaveICRegMaterial(params=params, data=data)
        return _, resp

    def post_SubmitRegMaterial(self, data, **kwargs):
        """提交注册资料"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params, data=data)
        return _, resp

    def get_GetICInfo(self, **kwargs):
        """获取工商注册基本信息"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def get_GetICRegMaterial(self, **kwargs):
        """获取工商注册资料"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def get_GetIndustryScopes(self, **kwargs):
        """获取行业和行业范围"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp

    def get_ListICInfos(self, **kwargs):
        """获取工商订单列表"""
        params = {
            "ICID": self.ICID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreatePreOrder(params=params)
        return _, resp