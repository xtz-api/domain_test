import json
import logging
from util.volc_domain_api.volc_domain_api import VolcDomainApi

# import pymysql

# from domain_autotest.conftest import CONSTANT

class DomainService(object):
    def __init__(self, client, auto_delete=None, code=None, content=None, Type=None, domain=None, period=None,renew_price=None,zone=None, name=None, email=None,
                 registration_type=None, status_mask=None, page_number=None,page_size=None, verify_status_mask=None, register_list=None, auto_renew=None, ns_list=None,
                 template_id=None):
        self.client = client
        self.api = VolcDomainApi(client)
        self.code = code
        self.content = content
        self.Type = Type
        self.domain = domain
        self.period = period
        self.renew_price = renew_price
        self.template_id = template_id
        self.ns_list = ns_list
        if auto_renew is not None:
            self.auto_renew = auto_renew
        else:
            self.auto_renew = False
        self.register_list = register_list
        if verify_status_mask is not None:
            self.verify_status_mask = verify_status_mask
        else:
            self.verify_status_mask = 1
        if zone is not None:
            self.zone = zone
        else:
            self.zone = ".com"

        self.name = name
        self.email = email
        self.registration_type = registration_type
        self.status_mask = status_mask
        if page_number is not None:
            self.page_number = page_number
        else:
            self.page_number = "1"
        if page_size is not None:
            self.page_size = page_size
        else:
            self.page_size = "0"

    # def domain_validate(self):
    #     """提交实名认证资料"""
    #     body = {
    #         "code": self.code,
    #         "content": self.content,
    #         "type": self.Type
    #     }
    #     params = {"test_cases": self.domain}
    #     _, resp = self.api.Domain_Validate(params=params, data=body)
    #     logging.info(resp)
    #     logging.info(_)
    #     return resp
    #
    # def domain_list(self, **kwargs):
    #     """domain_list"""
    #     params = {
    #         "page_number": self.page_number,
    #         "page_size": self.page_size,
    #     }
    #     params.update(**kwargs)
    #     logging.info(params)
    #     _, resp = self.api.Domain_List(params=params)
    #     return resp
    #
    # def batch_renew(self, data):
    #     """批量续费域名"""
    #     _, resp = self.api.Batch_Renew(data=data)
    #     return resp
    #
    # def renew(self):
    #     """续费域名"""
    #     body = {
    #         "test_cases": self.domain,
    #         "period": self.period,
    #         "renew_price": self.renew_price,
    #         "zone": self.zone
    #     }
    #     _, resp = self.api.Renew(data=body)
    #     return resp
    #
    # def new_domain(self):
    #     """注册域名"""
    #     body = {
    #         "register_list": [
    #             {
    #                 "auto_renew": self.auto_renew,
    #                 "test_cases": self.domain,
    #                 "period": self.period,
    #                 "price": self.renew_price,
    #                 "template_id": self.template_id,
    #                 "zone": self.zone,
    #                 "ns_list": self.ns_list,
    #             }
    #         ]
    #     }
    #     # if kwargs is not None:
    #     #     body.update(**kwargs)
    #     logging.info(body)
    #     _, resp = self.api.New_Domain(data=body)
    #     return resp
    #
    # def restore(self, data):
    #     """赎回域名"""
    #     body = {
    #         "test_cases": self.domain,
    #         "renew_price": self.renew_price,
    #         "zone": self.zone
    #     }
    #     _, resp = self.api.Restore(data=data)
    #     return resp
