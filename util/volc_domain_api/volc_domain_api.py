import logging

from util.volc_api.volc_requests import VolcRequests
from util.volc_api.volc_constant import VOLC_CONSTANT, VOLC_DOMAIN_CONSTANT


class VolcDomainApi(VolcRequests):
    def __init__(self, client=None):
        super().__init__(client)
        self.default_params = {"Version": VOLC_DOMAIN_CONSTANT.VERSION}
        self.url = "%s%s" % (self.client.host, VOLC_CONSTANT.VOLC_URL_PATH)

    def Domain_Validate(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UploadDomainAuthenticationInfo, params, data,
                              VOLC_CONSTANT.POST)

    def Batch_Renew(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchRenew, params, data,
                              VOLC_CONSTANT.POST)

    def New_Domain(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RegisterDomain, params, data,
                              VOLC_CONSTANT.POST)

    def Renew(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RenewDomain, params, data,
                              VOLC_CONSTANT.POST)

    def Restore(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RestoreDomain, params, data,
                              VOLC_CONSTANT.POST)

    def Template_List(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListTemplates, params, data,
                              VOLC_CONSTANT.GET)

    def Template_Get(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.GetTemplates))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetTemplates, params, data,
                              VOLC_CONSTANT.GET)

    def Template_Del(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DelTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DelTemplate, params, data,
                              VOLC_CONSTANT.POST)

    def Template_update(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.UpdateTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UpdateTemplate, params, data,
                              VOLC_CONSTANT.POST)

    def Transfer_In(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.TransferIn))
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferIn, params, data,
                              VOLC_CONSTANT.POST)
    def Transfer_In_Check(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.TransferInCheck))
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferInCheck, params, data,
                              VOLC_CONSTANT.POST)
    def Renew_Check(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.RenewCheck))
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RenewCheck, params, data,
                              VOLC_CONSTANT.POST)

    def Domain_List(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s"%(self.url, VOLC_DOMAIN_CONSTANT.ListDomains))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListDomains, params, data,
                              VOLC_CONSTANT.GET)

    """调domain接口删除指定域名信息"""
    def Del_ShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        logging.info(params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DelShopping))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DelShopping, params, data,
                              VOLC_CONSTANT.POST)

    """调domain接口查询购物车域名列表"""
    def get_ShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListShopping))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListShopping, params, data,
                              VOLC_CONSTANT.GET)

    """调domain接口查询信息模板列表"""
    def get_TemplateList(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListTemplate, params, data,
                              VOLC_CONSTANT.GET)

    """调domian接口增加一条域名信息"""
    def add_ShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.AddShopping))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.AddShopping, params, data,
                              VOLC_CONSTANT.POST)

    def Modify_Dns(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainNS))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainNS, params, data,
                              VOLC_CONSTANT.POST)
    """询价"""
    def Query_Single_Domain(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.QuerySingleDomainPrice))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.QuerySingleDomainPrice, params, data,
                              VOLC_CONSTANT.GET)
    def Download_Cert_Image(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage, params, data,
                              VOLC_CONSTANT.GET)
    def Whois(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.Whois))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.Whois, params, data,
                              VOLC_CONSTANT.GET)
    """查看域名详情"""
    def Del_ShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        logging.info(params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DelShopping))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DelShopping, params, data,
                              VOLC_CONSTANT.POST)