import logging

from test_domain.api_domain_service_base import DomainService


class DomainServiceTemplate(DomainService):
    def template_list(self, **kwargs):
        """获取域名列表"""
        params = {
            "page_number": self.page_number,
            "page_size": self.page_size,
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.Template_List(params=params)
        return _, resp

    def template_get(self, **kwargs):
        """获取域名列表"""
        params = {
            "template": 0
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.Template_Get(params=params)
        return _, resp

    def template_del(self, **kwargs):
        """获取域名列表"""
        params = {
            "template": 0
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.Template_Del(params=params)
        return _, resp

    def template_update(self, data, **kwargs):
        """获取域名列表"""
        params = {
            "template": 0
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.Template_update(params=params, data=data)
        return _, resp
