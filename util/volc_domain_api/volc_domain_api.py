import logging

from util.volc_api.volc_requests import VolcRequests
from util.volc_api.volc_constant import VOLC_CONSTANT, VOLC_DOMAIN_CONSTANT, VOLC_DOMAIN_CONSTANT_OPENAPI


class VolcDomainApi(VolcRequests):
    def __init__(self, client=None):
        super().__init__(client)
        self.default_params = {"Version": VOLC_DOMAIN_CONSTANT.VERSION}
        self.openapi_params = {"Version": VOLC_DOMAIN_CONSTANT_OPENAPI.VERSION}
        self.url = "%s%s" % (self.client.host, VOLC_CONSTANT.VOLC_URL_PATH)

    """**********************************************===注册域名===**********************************************"""
    """域名询价"""
    def QuerySingle_DomainPrice(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.QuerySingleDomainPrice, params, data,
                              VOLC_CONSTANT.GET)

    """获取购物车列表"""
    def GetShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetShoppingList, params, data,
                              VOLC_CONSTANT.GET)


    """单个-添加到购物车"""
    def AddDomain_ToShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.AddDomainToShoppingList, params, data,
                              VOLC_CONSTANT.POST)

    """批量-添加到购物车"""
    def BatchAddDomain_ToShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchAddDomainToShoppingList, params, data,
                              VOLC_CONSTANT.POST)

    """删除购物车中单个域名"""
    def Remove_DomainFromShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RemoveDomainFromShoppingList, params, data,
                              VOLC_CONSTANT.POST)

    """清空购物车"""
    def Clear_ShoppingList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ClearShoppingList, params, data,
                              VOLC_CONSTANT.POST)

    """注册域名"""
    def Register_Domain(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RegisterDomain, params, data,
                              VOLC_CONSTANT.POST)

    """**********************************************===火山支付--看看后续能不能搞到接口===**********************************************"""

    """**********************************************===WHOIS查询--待补充===**********************************************"""

    """**********************************************===域名操作管理===**********************************************"""
    """开启/关闭域名自动续费"""
    def SetAuto_Renew(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SetAutoRenew, params, data,
                              VOLC_CONSTANT.POST)

    """修改DNS服务器"""
    def Modify_DomainNS(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainNS, params, data,
                              VOLC_CONSTANT.POST)

    """开启/关闭禁止转移锁"""
    def Set_TransferProhibition(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SetTransferProhibition, params, data,
                              VOLC_CONSTANT.GET)

    """开启/关闭禁止更新锁"""
    def Set_UpdateProhibition(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SetUpdateProhibition, params, data,
                              VOLC_CONSTANT.POST)

    """修改备注"""
    def Modify_DomainComments(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainComments, params, data,
                              VOLC_CONSTANT.POST)

    """获取域名证书"""
    def Download_DomainCertImage(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage, params, data,
                              VOLC_CONSTANT.GET)

    """账号间转移"""
    def Domain_InternalTransfer(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DomainInternalTransfer, params, data,
                              VOLC_CONSTANT.POST)

    # 自定义DNS Host相关操作
    """获取DNS服务器列表"""
    def List_DNSHost(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListDNSHost, params, data,
                              VOLC_CONSTANT.GET)

    """创建DNS服务器"""
    def Add_DNSHost(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.AddDNSHost, params, data,
                              VOLC_CONSTANT.POST)

    """修改DNS服务器"""
    def Update_DNSHost(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UpdateDNSHost, params, data,
                              VOLC_CONSTANT.POST)

    """删除DNS服务器"""
    def Delete_DNSHost(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DeleteDNSHost, params, data,
                              VOLC_CONSTANT.POST)

    # 域名转出相关操作
    """域名转出"""
    def Transfer_Out(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferOut, params, data,
                              VOLC_CONSTANT.POST)

    """获取域名转出列表"""
    def ListDomain_TransferOutInfo(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListDomainTransferOutInfo, params, data,
                              VOLC_CONSTANT.GET)

    """重新获取转移密码"""
    def TransferOut_Again(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferOutAgain, params, data,
                              VOLC_CONSTANT.POST)

    """取消转出"""
    def CancelTransfer_Out(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CancelTransferOut, params, data,
                              VOLC_CONSTANT.POST)

    # 会员间Push
    """会员间Push"""
    def Create_Push(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CreatePush, params, data,
                              VOLC_CONSTANT.POST)

    """获取会员间Push列表"""
    def List_PushInfos(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListPushInfos, params, data,
                              VOLC_CONSTANT.GET)

    """取消转移"""
    def Cancel_Push(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CancelPush, params, data,
                              VOLC_CONSTANT.POST)

    """持有者过户"""
    def Change_Ownership(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ChangeOwnership, params, data,
                              VOLC_CONSTANT.POST)

    # 隐私保护相关操作
    """开通隐私保护"""
    def Open_PrivacyProtection(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.OpenPrivacyProtection, params, data,
                              VOLC_CONSTANT.POST)
    """续费隐私保护"""
    def Renew_PrivacyProtection(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RenewPrivacyProtection, params, data,
                              VOLC_CONSTANT.POST)
    """开启/关闭隐私保护自动续费"""
    def Set_PrivacyProtectionAutoRenew(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SetPrivacyProtectionAutoRenew, params, data,
                              VOLC_CONSTANT.POST)

    """域名续费"""
    def Renew_Domain(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RenewDomain, params, data,
                              VOLC_CONSTANT.POST)

    """查看详情"""
    def Get_Domain(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetDomain, params, data,
                              VOLC_CONSTANT.GET)

    """获取域名列表"""
    def List_Domains(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListDomains, params, data,
                              VOLC_CONSTANT.GET)

    """**********************************************===信息模板===**********************************************"""
    """创建模板"""
    def Create_Template(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CreateTemplate, params, data,
                              VOLC_CONSTANT.POST)

    """查看模板详情"""
    def Get_Template(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetTemplate, params, data,
                              VOLC_CONSTANT.GET)

    """获取模板列表"""
    def List_Templates(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListTemplates, params, data,
                              VOLC_CONSTANT.GET)

    """编辑模板"""
    # 编辑模板持有者信息
    def Update_Template(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UpdateTemplate, params, data,
                              VOLC_CONSTANT.POST)
    # 编辑模板证件信息
    def Upload_TemplateAuthenticationInfo(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UploadTemplateAuthenticationInfo, params, data,
                              VOLC_CONSTANT.POST)

    """删除模板"""
    def Delete_Template(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DeleteTemplate, params, data,
                              VOLC_CONSTANT.POST)

    """获取邮箱列表"""
    def Email_VerifyList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.EmailVerifyList, params, data,
                              VOLC_CONSTANT.GET)

    """添加邮箱"""
    def Email_VerifyCreate(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.EmailVerifyCreate, params, data,
                              VOLC_CONSTANT.POST)

    """删除邮箱"""
    def Email_VerifyDelete(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.EmailVerifyDelete, params, data,
                              VOLC_CONSTANT.POST)

    """**********************************************===域名转入===**********************************************"""
    """域名转入列表"""
    def List_TransferInDomains(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListTransferInDomains, params, data,
                              VOLC_CONSTANT.GET)

    """立即转入"""
    def Transfer_In(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferIn, params, data,
                              VOLC_CONSTANT.POST)

    """取消转入"""
    def Cancel_TransferIn(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CancelTransferIn, params, data,
                              VOLC_CONSTANT.POST)

    """**********************************************===批量操作===**********************************************"""
    """批量-持有者过户"""
    def Batch_RegistrantChange(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchRegistrantChange, params, data,
                              VOLC_CONSTANT.POST)

    """批量-域名续费"""
    def Batch_Renew(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchRenew, params, data,
                              VOLC_CONSTANT.POST)

    """批量-DNS修改"""
    def Batch_ModifyDomainNS(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchModifyDomainNS, params, data,
                              VOLC_CONSTANT.POST)

    """批量-设置自动续费"""
    def Batch_SetAutoRenew(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchSetAutoRenew, params, data,
                              VOLC_CONSTANT.POST)

    """**********************************************===委托购买===**********************************************"""
    """获取委托购买列表"""
    def List_Entrust(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListEntrust, params, data,
                              VOLC_CONSTANT.GET)

    """提交委托购买"""
    def Create_Entrust(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CreateEntrust, params, data,
                              VOLC_CONSTANT.POST)

    """取消委托购买"""
    def Cancel_Entrust(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CancelEntrust, params, data,
                              VOLC_CONSTANT.POST)

    """立即支付委托购买"""
    def Entrust_OrderPay(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.EntrustOrderPay, params, data,
                              VOLC_CONSTANT.POST)

    """获取委托购买详情"""
    def Get_EntrustDetail(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetEntrustDetail, params, data,
                              VOLC_CONSTANT.GET)

    """**********************************************===特惠资源包===**********************************************"""
    """获取资源包列表"""
    def List_UserResourcePackages(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListUserResourcePackages, params, data,
                              VOLC_CONSTANT.GET)

    """购买资源包"""
    def Buy_ResourcePackage(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BuyResourcePackage, params, data,
                              VOLC_CONSTANT.POST)

    """查看资源包详情"""
    # 查看资源包基本信息
    def Get_UserResourcePackage(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetUserResourcePackage, params, data,
                              VOLC_CONSTANT.GET)
    # 查看资源包抵扣详情
    def List_UserPackageUsage(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListUserPackageUsage, params, data,
                              VOLC_CONSTANT.GET)

    """**********************************************===操作日志===**********************************************"""
    """获取日志列表"""

    def List_OperateList(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListOperateList, params, data,
                              VOLC_CONSTANT.GET)

    """查看日志详情"""

    def Get_Operation(self, params={}, data=None):
        params.update(self.default_params)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetOperation, params, data,
                              VOLC_CONSTANT.GET)

    # def Batch_Renew(self, params={}, data=None):
    #     params.update(self.default_params)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchRenew, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def New_Domain(self, params={}, data=None):
    #     params.update(self.default_params)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RegisterDomain, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Renew(self, params={}, data=None):
    #     params.update(self.default_params)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RenewDomain, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Restore(self, params={}, data=None):
    #     params.update(self.default_params)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RestoreDomain, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Template_List(self, params={}, data=None):
    #     params.update(self.default_params)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListTemplates, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # def Template_Get(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.GetTemplates))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetTemplates, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # def Template_Del(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DelTemplate))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DelTemplate, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Template_update(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.UpdateTemplate))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UpdateTemplate, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Transfer_In(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.TransferIn))
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferIn, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Transfer_In_Check(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.TransferInCheck))
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.TransferInCheck, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # def Renew_Check(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.RenewCheck))
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.RenewCheck, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """调domain接口删除指定域名信息(删除清单表中的某个域名)"""
    #
    # def Del_ShoppingList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info(params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DelShopping))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DelShopping, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """批量添加购物车"""
    #
    # def BatchAddDomainToShoppingList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info(params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.BatchAddDomainToShoppingList))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchAddDomainToShoppingList, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """清空购物车"""
    #
    # def ClearShoppingList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info(params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ClearShoppingList))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ClearShoppingList, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """调domain接口查询购物车域名列表(获取域名清单）"""
    #
    # def get_ShoppingList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListShopping))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListShopping, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """调domain接口查询信息模板列表"""
    #
    # def get_TemplateList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListTemplate))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListTemplate, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """调domian接口增加一条域名信息"""
    #
    # def add_ShoppingList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.AddShopping))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.AddShopping, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """询价"""
    #
    # def Query_Single_Domain(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.QuerySingleDomainPrice))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.QuerySingleDomainPrice, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # def Download_Cert_Image(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # def Whois(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.Whois))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.Whois, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """设置/取消域名转移锁"""
    #
    # def SetTransferProhibition(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.SetTransferProhibition))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SetTransferProhibition, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """设置/取消域名更新锁"""
    #
    # def SetUpdateProhibition(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.SetUpdateProhibition))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SetUpdateProhibition, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """域名过户"""
    #
    # def ChangeOwnership(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ChangeOwnership))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ChangeOwnership, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """数据概览"""
    #
    # def Overview(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.Overview))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.Overview, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """修改域名权威NS"""
    #
    # def ModifyDomainNS(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainNS))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainNS, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """导出域名列表"""
    #
    # def ExportDomains(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ExportDomains))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ExportDomains, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """同步dns_host"""
    #
    # def SyncDNSHost(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.SyncDNSHost))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.SyncDNSHost, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """获取dns_host列表"""
    #
    # def ListDNSHost(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListDNSHost))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListDNSHost, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """增加dns_host"""
    #
    # def AddDNSHost(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.AddDNSHost))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.AddDNSHost, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """更新dns_host"""
    #
    # def UpdateDNSHost(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.UpdateDNSHost))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UpdateDNSHost, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """删除dns_host"""
    #
    # def DeleteDNSHost(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DeleteDNSHost))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DeleteDNSHost, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """修改域名备注"""
    #
    # def ModifyDomainComments(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainComments))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainComments, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """检查域名列表是否属于账号"""
    #
    # def CheckAccountDomainList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.CheckAccountDomainList))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.CheckAccountDomainList, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """获取域名证书的图片"""
    #
    # def DownloadDomainCertImage(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCertImage, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """域名证书下载"""
    #
    # def DownloadDomainCert(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCert))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DownloadDomainCert, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """批量过户"""
    #
    # def BatchRegistrantChange(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.BatchRegistrantChange))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchRegistrantChange, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """批量ns修改"""
    #
    # def BatchModifyDomainNS(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.BatchModifyDomainNS))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.BatchModifyDomainNS, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """修改域名联系人信息"""
    #
    # def ModifyDomainContactorInfo(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainContactorInfo))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ModifyDomainContactorInfo, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """获取操作记录详情"""
    #
    # def GetOperation(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.GetOperation))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetOperation, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """获取域名详情"""
    #
    # def GetDomain(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.GetDomain))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.GetDomain, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """获取操作记录列表"""
    #
    # def ListOperateList(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListOperateList))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListOperateList, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """获取域名列表"""
    #
    # def ListDomains(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.ListDomains))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.ListDomains, params, data,
    #                           VOLC_CONSTANT.GET)
    #
    # """提交域名实名认证资料"""
    #
    # def UploadDomainAuthenticationInfo(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.UploadDomainAuthenticationInfo))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.UploadDomainAuthenticationInfo, params, data,
    #                           VOLC_CONSTANT.POST)
    #
    # """软删除域名"""
    #
    # def DeleteDomain(self, params={}, data=None):
    #     params.update(self.default_params)
    #     logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT.DeleteDomain))
    #     logging.info(self.client.auth)
    #     return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT.DeleteDomain, params, data,
    #                           VOLC_CONSTANT.POST)

    # ================================******************OpenAPI********************========================================================

    """OpenAPI-域名询价"""

    def Checkfee_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.Checkfee))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.Checkfee, params, data,
                              VOLC_CONSTANT.GET)

    """OpenAPI-获取域名详情"""

    def GetDomain_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetDomain))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetDomain, params, data,
                              VOLC_CONSTANT.GET)

    """OpenAPI-获取域名列表"""

    def ListDomains_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ListDomains))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ListDomains, params, data,
                              VOLC_CONSTANT.GET)

    """OpenAPI-获取域名证书URL"""

    def GetDomainCertificateUrl_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetDomainCertificateUrl))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetDomainCertificateUrl, params, data,
                              VOLC_CONSTANT.GET)

    """OpenAPI-修改NS"""

    def ModifyDomainNS_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ModifyDomainNS))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ModifyDomainNS, params, data,
                              VOLC_CONSTANT.POST)

    """OPENAPI开启/关闭域名自动续费"""

    def SetDomainAutoRenew_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.SetDomainAutoRenew))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.SetDomainAutoRenew, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-创建模版"""

    def CreateTemplate_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.CreateTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.CreateTemplate, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-获取模版详情"""

    def GetTemplate_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetTemplate, params, data,
                              VOLC_CONSTANT.GET)

    """OpenAPI-获取模板列表"""

    def ListTemplates_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ListTemplates))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ListTemplates, params, data,
                              VOLC_CONSTANT.GET)

    """OpenAPI-更新模板"""

    def UpdataTemplate_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.UpdateTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.UpdateTemplate, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-实名模板"""

    def ValidateTemplat_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ValidateTemplate))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.ValidateTemplate, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-异步注册域名"""

    def RegisterDomain_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.RegisterDomain))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.RegisterDomain, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-域名异步续费"""

    def RenewDomain_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.RenewDomain))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.RenewDomain, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-域名异步过户"""

    def DomainRegistrationChange_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.DomainRegistrantChange))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.DomainRegistrantChange, params, data,
                              VOLC_CONSTANT.POST)

    """OpenAPI-获取异步任务注册结果"""

    def GetAsyncTask_OPENAPI(self, params={}, data=None):
        params.update(self.openapi_params)
        logging.info("%s %s" % (self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetAsyncTask))
        logging.info(self.client.auth)
        return self.implement(self.client, self.url, VOLC_DOMAIN_CONSTANT_OPENAPI.GetAsyncTask, params, data,
                              VOLC_CONSTANT.GET)
