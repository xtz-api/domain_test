class DnsLineList_Volc:
    line_list = {}


class VOLC_CONSTANT:
    """Volc OpenApi Constant"""

    # URL path
    VOLC_URL_PATH = "/"

    # API Version
    # VERSION = "2021-07-05"

    # Method
    GET = "get"
    POST = "post"


class VOLC_DOMAIN_CONSTANT:
    """
    BOE账号AK、SK
    """
    # gogokid-2100000056
    AK = "AKLTYThmM2IzNzM4ZTg5NGZiMmEzN2MwMzNlNGQ1OTQzNWU"
    SK = "TnpnMk1UazRZemRrWlRVd05ESmxaV0kzTldZd1pUWmpNbVkyTkRkak1qVQ=="
    # auto-tgm-2100266070
    AK_2 = "AKLTYTY3NTM1MDhhYTczNDJlZGFiMGRlY2NmMTI5N2Q2YWM"
    SK_2 = "T0Rka1pEWmlZemd4T1dGaE5HRm1NR0ZpT1Rrd01EZGhPR1kzTXpkaE1tUQ=="
    # lululemon-2000002951
    AK_ONLINE = "AKLTNDU4YmMxNDBiYWYxNDBjZTljYjhlYzRjY2I5N2UzMjk"
    SK_ONLINE = "TjJNeFlUWTBNVFE1TW1SaE5EYzNOamd4TURJek9UUmlPREUyT0RSbE5Uaw=="
    REGION = "cn-north-1"
    SERVICE = "domain_service"
    VERSION = "2021-06-01"

    """**********************************************===注册域名===**********************************************"""
    """域名询价"""
    QuerySingleDomainPrice = "QuerySingleDomainPrice"
    """单个-添加购物车"""
    AddDomainToShoppingList = "AddDomainToShoppingList"
    """批量询价"""
    # 没有批量询价，都是一个个询价的
    """获取购物车列表内容"""
    GetShoppingList = "GetShoppingList"
    """批量添加到购物车"""
    BatchAddDomainToShoppingList = "BatchAddDomainToShoppingList"
    """删除购物车内已添加的单个域名"""
    RemoveDomainFromShoppingList = "RemoveDomainFromShoppingList"
    """清空购物车"""
    ClearShoppingList = "ClearShoppingList"
    """注册域名"""
    RegisterDomain = "RegisterDomain"

    """**********************************************===火山支付--看看后续能不能搞到接口===**********************************************"""

    """**********************************************===WHOIS查询--待补充===**********************************************"""

    """**********************************************===域名操作管理===**********************************************"""
    """开启/关闭域名自动续费"""
    SetAutoRenew = "SetAutoRenew"
    """修改DNS服务器"""
    ModifyDomainNS = "ModifyDomainNS"
    """开启/关闭禁止转移锁"""
    SetTransferProhibition = "SetTransferProhibition"
    """开启/关闭禁止更新锁"""
    SetUpdateProhibition = "SetUpdateProhibition"
    """修改备注"""
    ModifyDomainComments = "ModifyDomainComments"
    """获取域名证书"""
    DownloadDomainCertImage = "DownloadDomainCertImage"
    """账号间转移"""
    DomainInternalTransfer = "DomainInternalTransfer"
    # 自定义DNS Host相关操作
    """获取DNS服务器列表"""
    ListDNSHost = "ListDNSHost"
    """创建DNS服务器"""
    AddDNSHost = "AddDNSHost"
    """修改DNS服务器"""
    UpdateDNSHost = "UpdateDNSHost"
    """删除DNS服务器"""
    DeleteDNSHost = "DeleteDNSHost"
    # 域名转出
    """域名转出"""
    TransferOut = "TransferOut"
    """获取域名转出列表"""
    ListDomainTransferOutInfo = "ListDomainTransferOutInfo"
    """重新获取转移密码"""
    TransferOutAgain = "TransferOutAgain"
    """取消转出"""
    CancelTransferOut = "CancelTransferOut"
    # 会员间Push
    """会员间Push"""
    CreatePush = "CreatePush"
    """获取会员间Push列表"""
    ListPushInfos = "ListPushInfos"
    """取消转移"""
    CancelPush = "CancelPush"
    """持有者过户"""
    ChangeOwnership = "ChangeOwnership"
    """开通隐私保护"""
    OpenPrivacyProtection = "OpenPrivacyProtection"
    """续费隐私保护"""
    RenewPrivacyProtection = "RenewPrivacyProtection"
    """开启/关闭隐私保护自动续费"""
    SetPrivacyProtectionAutoRenew = "SetPrivacyProtectionAutoRenew"
    """域名续费"""
    RenewDomain = "RenewDomain"
    """查看详情"""
    GetDomain = "GetDomain"
    """获取域名列表"""
    ListDomains = "ListDomains"

    """**********************************************===信息模板===**********************************************"""
    """创建模板"""
    CreateTemplate = "CreateTemplate"
    """查看模板详情"""
    GetTemplate = "GetTemplate"
    """获取模板列表"""
    ListTemplates = "ListTemplates"
    """编辑模板"""
    UpdateTemplate = "UpdateTemplate"  # 编辑模板持有者信息
    UploadTemplateAuthenticationInfo = "UploadTemplateAuthenticationInfo"  # 编辑模板证件信息
    """删除模板"""
    DeleteTemplate = "DeleteTemplate"
    """获取邮箱列表"""
    EmailVerifyList = "EmailVerifyList"
    """添加邮箱"""
    EmailVerifyCreate = "EmailVerifyCreate"
    """删除邮箱"""
    EmailVerifyDelete = "EmailVerifyDelete"

    """**********************************************===域名转入===**********************************************"""
    """域名转入列表"""
    ListTransferInDomains = "ListTransferInDomains"
    """立即转入"""
    TransferIn = "TransferIn"
    """取消转入"""
    CancelTransferIn = "CancelTransferIn"

    """**********************************************===批量操作===**********************************************"""
    """批量-持有者过户"""
    BatchRegistrantChange = "BatchRegistrantChange"
    """批量-域名续费"""
    BatchRenew = "BatchRenew"
    """批量-DNS修改"""
    BatchModifyDomainNS = "BatchModifyDomainNS"
    """批量-设置自动续费"""
    BatchSetAutoRenew = "BatchSetAutoRenew"

    """**********************************************===委托购买===**********************************************"""
    """获取委托购买列表"""
    ListEntrust = "ListEntrust"
    """提交委托购买"""
    CreateEntrust = "CreateEntrust"
    """取消委托购买"""
    CancelEntrust = "CancelEntrust"
    """立即支付委托购买"""
    EntrustOrderPay = "EntrustOrderPay"
    """获取委托购买详情"""
    GetEntrustDetail = "GetEntrustDetail"

    """**********************************************===特惠资源包===**********************************************"""
    """获取资源包列表"""
    ListUserResourcePackages = "ListUserResourcePackages"
    """购买资源包"""
    BuyResourcePackage = "BuyResourcePackage"
    """查看资源包详情"""
    GetUserResourcePackage = "GetUserResourcePackage"  # 查看资源包基本信息
    ListUserPackageUsage = "ListUserPackageUsage"  # 查看资源包抵扣详情

    """**********************************************===操作日志===**********************************************"""
    """获取日志列表"""
    ListOperateList = "ListOperateList"
    """查看日志详情"""
    GetOperation = "GetOperation"


class VOLC_DOMAIN_CONSTANT_OPENAPI:
    # gogokid-2100000056
    AK = "AKLTYThmM2IzNzM4ZTg5NGZiMmEzN2MwMzNlNGQ1OTQzNWU"
    SK = "TnpnMk1UazRZemRrWlRVd05ESmxaV0kzTldZd1pUWmpNbVkyTkRkak1qVQ=="

    # auto-tgm-2100266070
    AK_2 = "AKLTYTY3NTM1MDhhYTczNDJlZGFiMGRlY2NmMTI5N2Q2YWM"
    SK_2 = "T0Rka1pEWmlZemd4T1dGaE5HRm1NR0ZpT1Rrd01EZGhPR1kzTXpkaE1tUQ=="

    # Domaintest1
    AK_Domaintest1 = "AKLTZDU3YjgzMTY3NmRmNDVhYjg4MGEwODFkMWFhMGU0NDg"
    SK_Domaintest1 = "WVdJeU5HUmlZalJpTTJRd05ESm1ZMkl6TlRRMFlUQm1aR0V4TVRGaFpqUQ=="

    # domaintest2-2100056829
    AK_Domaintest2 = "AKLTZGNmNmY2Yjk1YWE5NDI1MWFkZjU3NGRhMjQ0NDUyNDA"
    SK_Domaintest2 = "T0RkbE5UVmpNV1JsT0RkbU5HRmxZamcwTXpKa05URmtZVGRrTWpka01UUQ=="

    AK_ONLINE = "AKLTNDU4YmMxNDBiYWYxNDBjZTljYjhlYzRjY2I5N2UzMjk"
    SK_ONLINE = "TjJNeFlUWTBNVFE1TW1SaE5EYzNOamd4TURJek9UUmlPREUyT0RSbE5Uaw=="

    REGION = "cn-north-1"
    SERVICE = "domain_openapi"
    VERSION = "2022-12-12"

    """**********************************************===OpenAPI-域名操作===**********************************************"""
    """OpenAPI-域名询价"""
    Checkfee = "CheckFee"
    """OpenAPI-获取域名详情"""
    GetDomain = "GetDomain"
    """OpenAPI-获取域名列表"""
    ListDomains = "ListDomains"
    """获取域名证书URL"""
    GetDomainCertificateUrl = "GetDomainCertificateUrl"
    """OpenAPI-修改NS"""
    ModifyDomainNS = "ModifyDomainNS"
    """OpenAPI-开启/关闭域名自动续费"""
    SetDomainAutoRenew = "SetDomainAutoRenew"

    """**********************************************===OpenAPI-信息模板===**********************************************"""
    """OpenAPI-创建模版"""
    CreateTemplate = "CreateTemplate"
    """OpenAPI-获取模版详情"""
    GetTemplate = "GetTemplate"
    """OpenAPI-获取模板了列表"""
    ListTemplates = "ListTemplates"
    """OpenAPI-更新模板"""
    UpdateTemplate = "UpdateTemplate"
    """OpenAPI-实名模板"""
    ValidateTemplate = "ValidateTemplate"

    """**********************************************===OpenAPI-异步任务===**********************************************"""
    """OpenAPI-域名异步过户"""
    DomainRegistrantChange = "DomainRegistrantChange"
    """OpenAPI-异步注册域名"""
    RegisterDomain = "RegisterDomain"
    """OpenAPI-查询异步任务详情"""
    GetAsyncTask = "GetAsyncTask"
    """域名异步续费"""
    RenewDomain = "RenewDomain"

    """**********************************************===OpenAPI-TR专用路由===**********************************************"""
    """获取域名信息"""
    # /trafficRoute/GetDomain="/trafficRoute/GetDomain"
    """修改域名NS"""
    # /trafficRoute/ModifyDomainNS="/trafficRoute/ModifyDomainNS"
