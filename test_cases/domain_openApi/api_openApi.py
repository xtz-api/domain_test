import logging
from test_cases.api_domain_service_base import DomainService


# 域名操作
class DomainServiceManager(DomainService):

    def get_checkFee(self, **kwargs):
        """域名询价"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.Checkfee_OPENAPI(params=params)
        return _, resp

    def get_getDomain(self, **kwargs):
        """获取域名详情"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.GetDomain_OPENAPI(params=params)
        # logging.info("Api StatusCode is -->%s，API Response is -->%s" % (_, resp))
        return _, resp

    def get_listDomains(self, **kwargs):
        """获取域名列表"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.ListDomains_OPENAPI(params=params)
        # logging.info("Api StatusCode is -->%s" % resp)
        return _, resp

    def get_getDomainCertificateUrl(self, **kwargs):
        """获取域名证书URL"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.GetDomainCertificateUrl_OPENAPI(params=params)
        return _, resp

    def post_modifyDomainNS(self, data, **kwargs):
        """修改域名NS"""
        params = {
            "domain": self.domain
        }
        params.update(kwargs)
        logging.info(kwargs)
        _, resp = self.api.ModifyDomainNS_OPENAPI(params=params, data=data)
        return _, resp

    def post_setDomainAutoRenew(self, data, **kwargs):
        """开启/关闭域名自动续费"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.SetDomainAutoRenew_OPENAPI(params=params, data=data)
        return _, resp


# 模板操作
class DomainServiceTemplate(DomainService):
    def get_listTemplates(self, **kwargs):
        """获取模板列表"""
        params = {
            "page_number": self.page_number,
            "page_size": self.page_size
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.ListTemplates_OPENAPI(params=params)
        return _, resp

    def get_getTemplate(self, **kwargs):
        """获取模板详情"""
        params = {
            "tag": 0
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.GetTemplate_OPENAPI(params=params)
        return _, resp

    def post_createTemplate(self, data, **kwargs):
        """创建模板"""
        params = {
            # PS：这个domain的键值对应该都是错误的，先写着这个吧，后续再更改一下
            "domian": self.domain

        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.CreateTemplate_OPENAPI(params=params, data=data)
        return _, resp

    def post_updateTemplate(self, data, **kwargs):
        """更新模板信息"""
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(kwargs)
        _, resp = self.api.UpdataTemplate_OPENAPI(params=params, data=data)
        return _, resp

    # # PS：这个实名模板的API暂时有些小问题，暂时先不用。
    # def post_validateTemplate(self, data, **kwargs):
    #     """实名模板"""
    #     params = {
    #         "domain": self.domain
    #     }
    #     params.update(**kwargs)
    #     logging.info(kwargs)
    #     _, resp = self.api.ValidateTemplate_OPENAPI(params=params, data=data)
    #     return _, resp


# 异步任务操作
class DomainServiceAsync(DomainService):

    # 域名异步注册
    def post_registerDomain(self, data, **kwargs):
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.RegisterDomain_OPENAPI(params=params, data=data)
        return _, resp

    # 域名异步过户
    def post_domainRegistrantChange(self, data, **kwargs):
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.DomainRegistrationChange_OPENAPI(params=params, data=data)
        return _, resp

    # 查询异步任务详情
    def get_getAsyncTask(self, **kwargs):
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.GetAsyncTask_OPENAPI(params=params)
        return _, resp

    # 域名异步续费
    def post_renewDomain(self, data, **kwargs):
        params = {
            "domain": self.domain
        }
        params.update(**kwargs)
        logging.info(params)
        _, resp = self.api.RenewDomain_OPENAPI(params=params, data=data)
        return _, resp
