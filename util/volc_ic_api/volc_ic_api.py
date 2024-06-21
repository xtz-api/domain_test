import logging

from util.volc_api.volc_requests import VolcRequests
from util.volc_api.volc_constant import VOLC_CONSTANT, VOLC_IC_CONSTANT, VOLC_IC_CONSTANT_OPENAPI


class VolcIcApi(VolcRequests):
    def __init__(self, client=None):
        super().__init__(client)
        self.default_params = {"Version": VOLC_IC_CONSTANT.VERSION}
        self.openapi_params = {"Version": VOLC_IC_CONSTANT_OPENAPI.VERSION}
        self.url = "%s%s" % (self.client.host, VOLC_CONSTANT.VOLC_URL_PATH)

    # =============================自然人/法人管理*=============================
    """创建模版"""

    def CreateTemplate(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.CreateTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.CreateTemplate, params, data, VOLC_CONSTANT.POST)

    """查看模版详情"""

    def GetTemplate(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.GetTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetTemplate, params, data, VOLC_CONSTANT.GET)

    """查看模板列表"""

    def ListTemplates(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.ListTemplates))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListTemplates, params, data, VOLC_CONSTANT.GET)

    """更新模板"""

    def UpdateTemplate(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.UpdateTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.UpdateTemplate, params, data, VOLC_CONSTANT.POST)

    # =============================需求管理*=============================

    """创建需求单"""

    def CreateReq(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.CreateReq))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.CreateReq, params, data, VOLC_CONSTANT.POST)

    """查询需求单详情"""

    def GetReq(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetReq))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetReq, params, data, VOLC_CONSTANT.GET)

    """查询需求列表"""

    def ListReq(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.ListReq))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListReq, params, data, VOLC_CONSTANT.GET)

    """关闭商机需求"""

    def CloseReq(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.CloseReq))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.CloseReq, params, data, VOLC_CONSTANT.POST)

    # =============================工商服务订单*=============================

    """创建预配置火山订单"""

    def CreatePreOrder(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.CreatePreOrder))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.CreatePreOrder, params, data, VOLC_CONSTANT.POST)

    """暂存-注册资料"""

    def SaveICRegMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.SaveICRegMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.SaveICRegMaterial, params, data, VOLC_CONSTANT.POST)

    """提交审核-注册资料"""

    def SubmitRegMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.SubmitRegMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.SubmitRegMaterial, params, data, VOLC_CONSTANT.POST)

    """获取工商注册基本信息"""

    def GetICInfo(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetICInfo))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetICInfo, params, data, VOLC_CONSTANT.GET)

    """获取工商注册资料"""

    def GetICRegMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetICRegMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetICRegMaterial, params, data, VOLC_CONSTANT.GET)

    """获取行业和行业范围"""

    def GetIndustryScopes(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetIndustryScopes))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetIndustryScopes, params, data, VOLC_CONSTANT.GET)

    """获取工商注册列表"""

    def ListICInfos(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.ListICInfos))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListICInfos, params, data, VOLC_CONSTANT.GET)

    # =============================银行开户*=============================

    """创建预配置火山订单-->同上面工商订单的创建"""

    """获取银行开户详情"""

    def GetOpenBankInfo(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetOpenBankInfo))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetOpenBankInfo, params, data, VOLC_CONSTANT.GET)

    """获取银行开户订单列表"""

    def ListOpenBankInfos(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.ListOpenBankInfos))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListOpenBankInfos, params, data, VOLC_CONSTANT.GET)

    """提交银行开户审核资料"""

    def SubmitOpenBankMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.SubmitOpenBankMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.SubmitOpenBankMaterial, params, data, VOLC_CONSTANT.POST)

    # =============================税务报道*=============================

    """获取税务报道详情"""

    def GetTaxReportingInfo(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetTaxReportingInfo))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetTaxReportingInfo, params, data, VOLC_CONSTANT.GET)

    """获取税务报道订单列表"""

    def ListTaxReportingInfos(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.ListTaxReportingInfos))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListTaxReportingInfos, params, data, VOLC_CONSTANT.GET)

    """提交税务报道审核资料"""

    def SubmitTaxReportingMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.SubmitTaxReportingMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.SubmitTaxReportingMaterial, params, data, VOLC_CONSTANT.POST)

    # =============================企业订单*=============================
    """获取企业认证管家订单详情"""

    def GetButlerInfo(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.GetButlerInfo))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetButlerInfo, params, data, VOLC_CONSTANT.GET)

    """获取企业认证管家订单列表"""

    def ListButlerInfos(self, params={}, data=None):
        params.update(self.default_params)
        logging.info("%s,%s" % (self.url, VOLC_IC_CONSTANT.ListButlerInfos))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListButlerInfos, params, data, VOLC_CONSTANT.GET)

    # =============================资质服务订单*=============================

    """创建资质预配置火山订单"""

    def CreateQualificationOrder(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.CreateQualificationOrder))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.CreateQualificationOrder, params, data, VOLC_CONSTANT.POST)

    """获取资质订单基本信息"""

    def GetQualificationInfo(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.GetQualificationInfo))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetQualificationInfo, params, data, VOLC_CONSTANT.GET)

    """获取资质订单资料，包括资料/进度条"""

    def GetQualificationMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.GetQualificationMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.GetQualificationMaterial, params, data, VOLC_CONSTANT.GET)

    """获取资质订单列表"""

    def ListQualificationInfos(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.ListQualificationInfos))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.ListQualificationInfos, params, data, VOLC_CONSTANT.GET)

    """提交资质资料"""

    def SubmitQualificationMaterial(self, params=None, data=None):
        if params is None:
            params = {}
        params.update(self.default_params)
        logging.info("%s %s" % (self.url, VOLC_IC_CONSTANT.SubmitQualificationMaterial))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_IC_CONSTANT.SubmitQualificationMaterial, params, data, VOLC_CONSTANT.POST)
