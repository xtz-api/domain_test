import logging
from test_cases.api_ic_base import IcService


class IcTemplateAPI(IcService):
    def post_createTemplate(self, data, **kwargs):
        """创建模板"""
        params = {
            "TemplateID": self.TemplateID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreateTemplate(params=params, data=data)
        return _, resp

    def get_getTemplate(self, **kwargs):
        """查看模板详情"""
        params = {
            "TemplateID": self.TemplateID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.GetTemplate(params=params)
        return _, resp

    def get_listTemplates(self, **kwargs):
        """查看模板列表"""
        params = {
            "TemplateID": self.TemplateID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.ListTemplates(params=params)
        return _, resp

    def post_updateTemplate(self, data, **kwargs):
        """更新模板信息"""
        params = {
            "TemplateID": self.TemplateID
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.UpdateTemplate(params=params, data=data)
        return _, resp

