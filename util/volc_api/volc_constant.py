class VOLC_CONSTANT:
    """Volc  Constant"""

    # URL path
    VOLC_URL_PATH = "/"

    # API Version
    # VERSION = "2021-07-05"

    # Method
    GET = "get"
    POST = "post"


# 这个是工商的
class VOLC_IC_CONSTANT:
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
    SERVICE = "industry_commerce"
    VERSION = "2023-11-11"

    # =============================自然人/法人管理*=============================
    """创建模版"""
    CreateTemplate = "CreateTemplate"
    """查看模版详情"""
    GetTemplate = "GetTemplate"
    """查看模板列表"""
    ListTemplates = "ListTemplates"
    """更新模板"""
    UpdateTemplate = "UpdateTemplate"

    # =============================需求管理*=============================
    """创建需求单"""
    CreateReq = "CreateReq"
    """查询需求单详情"""
    GetReq = "GetReq"
    """查询需求列表"""
    ListReq = "ListReq"
    """关闭商机需求"""
    CloseReq = "CloseReq"

    # =============================工商服务订单*=============================
    """创建预配置工商火山订单"""
    CreatePreOrder = "CreatePreOrder"
    """暂存-注册资料"""
    SaveICRegMaterial = "SaveICRegMaterial"
    """提交审核-注册资料"""
    SubmitRegMaterial = "SubmitRegMaterial"
    """获取工商注册基本信息"""
    GetICInfo = "GetICInfo"
    """获取工商注册资料"""
    GetICRegMaterial = "GetICRegMaterial"
    """获取行业和行业范围"""
    GetIndustryScopes = "GetIndustryScopes"
    """获取工商注册列表"""
    ListICInfos = "ListICInfos"

    # =============================银行开户*=============================
    """创建预配置火山订单-->同上面工商订单的创建"""

    """获取银行开户详情"""
    GetOpenBankInfo = "GetOpenBankInfo"
    """获取银行开户订单列表"""
    ListOpenBankInfos = "ListOpenBankInfos"
    """提交银行开户审核资料"""
    SubmitOpenBankMaterial = "SubmitOpenBankMaterial"

    # =============================税务报道*=============================
    """获取税务报道详情"""
    GetTaxReportingInfo = "GetTaxReportingInfo"
    """获取税务报道订单列表"""
    ListTaxReportingInfos = "ListTaxReportingInfos"
    """提交税务报道审核资料"""
    SubmitTaxReportingMaterial = "SubmitTaxReportingMaterial"

    # =============================企业订单*=============================
    """获取企业认证管家订单详情"""
    GetButlerInfo = "GetButlerInfo"
    """获取企业认证管家订单列表"""
    ListButlerInfos = "ListButlerInfos"

    # =============================资质服务订单*=============================
    """创建资质预配置火山订单"""
    CreateQualificationOrder = "CreateQualificationOrder"
    """获取资质订单基本信息"""
    GetQualificationInfo = "GetQualificationInfo"
    """获取资质订单资料，包括资料/进度条"""
    GetQualificationMaterial = "GetQualificationMaterial"
    """获取资质订单列表"""
    ListQualificationInfos = "ListQualificationInfos"
    """提交资质资料"""
    SubmitQualificationMaterial = "SubmitQualificationMaterial"


# ===================================*目前还没有工商的openApi，所以这个不是真的，后续有的话再按照这个去修改*============================================================================================================================================
class VOLC_IC_CONSTANT_OPENAPI:
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

    # =============================*************域名**************=============================
    """OpenAPI-域名询价"""
    Checkfee = "CheckFee"
