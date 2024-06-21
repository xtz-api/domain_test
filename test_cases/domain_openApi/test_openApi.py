import time

import pytest
import logging
import allure
from assertpy import assert_that
from util import db_check
from util.date_util import convert_to_timestamp
from test_cases.domain_openApi.api_openApi import *
from test_cases.domain_openApi.data_openApi import *


# ************************模板操作*********************************
@allure.title("创建模板--成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "CreateTemplate")
@pytest.mark.parametrize("data", data_post_CreateTemplate_success)
def test_CreateTemplate_success(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_post_CreateTemplate_success，comment is：%s" % data["comment"])
    statusCode, query_res = DomainServiceTemplate(client=volc_domain_client_openapi).post_createTemplate(data["body"])
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    # 断言看 tag 是否在输出结果中，如果在则执行下一步获取，并打印出来，如果不在则提醒"断言失败，查看请求是否正确"
    assert 'tag' in query_res["Result"], "断言失败，查看请求是否正确"
    tag = query_res["Result"]["tag"]  # 获取"tag"的值

    print(tag)


@allure.title("创建模板--失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "CreateTemplate")
@pytest.mark.parametrize("data", data_post_CreateTemplate_error)
def test_ListTemplate_error(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_post_CreateTemplate_error，comment is：%s" % data["comment"])
    # params = data["params"]
    statusCode, query_res = DomainServiceTemplate(client=volc_domain_client_openapi).post_createTemplate(data["body"])
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["Resp"]["Error"])


@allure.title("获取模板列表")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "ListTemplates")
@pytest.mark.parametrize("data", data_get_ListTemplates)
def test_ListTemplates(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_templates/data_get_ListTemplates，comment is：%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceTemplate(client=volc_domain_client_openapi).get_listTemplates(**params)
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("获取模板详情-成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "GetTemplate")
@pytest.mark.parametrize("data", data_get_GetTemplate)
def test_GetTemplate(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_Get_GetTemplate_success，comment is：%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceTemplate(client=volc_domain_client_openapi).get_getTemplate(**params)
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


# @allure.title("更新模板")
# @pytest.mark.executor("TaoGangMing")
# @pytest.mark.tag("P1", "UpdateTemplate")
# @pytest.mark.parametrize("data", data_post_UpdateTemplate)
# def test_UpdateTemplate(volc_domain_client_openapi, data):
#     logging.info("Test Case：/data_post_CreateTemplate_error，comment is：%s" % data["comment"])
#     statusCode, query_res = DomainServiceTemplate(client=volc_domain_client_openapi).post_updateTemplate(data["body"])
#     logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))
#     assert_that(statusCode).is_equal_to(data["code"])


# 这个API暂时有些小问题，暂时先不使用了。
# @allure.title("实名模板")
# @pytest.mark.executor("TaoGangMing")
# @pytest.mark.tag("P1", "VlidateTemplate")
# @pytest.mark.parametrize("data", data_Post_ValidateTemplate)
# def test_VlidateTemplate(volc_domain_client_openapi, data):
#     logging.info("Test Case：/data_Post_ValidateTemplate，comment is：%s" % data["comment"])
#     statusCode, query_res = DomainServiceTemplate(client=volc_domain_client_openapi).post_validateTemplate(data["body"])
#     logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))
#     assert_that(statusCode).is_equal_to(data["code"])


# ************************域名操作*********************************


@allure.title("域名询价-->成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "check_fee")
@pytest.mark.parametrize("data", data_get_CheckFee_success)
def test_domain_checkFee_success(volc_domain_client_openapi, data):
    logging.info("Test Case: /data_management/data_domain_check_fee_success, comment is : %s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_checkFee(**params)
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res['Result']).is_equal_to(data["Result"])


@allure.title("域名询价-->失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "check_fee")
@pytest.mark.parametrize("data", data_get_CheckFee_error)
def test_domain_checkFee_error(volc_domain_client_openapi, data):
    logging.info("Test Case: /data_management/data_domain_check_fee_success, comment is : %s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_checkFee(**params)
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res['ResponseMetadata']["Error"]).is_equal_to(data["res"]["Error"])


# ************************异步任务操作*********************************
@allure.title("域名异步注册-成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "域名异步注册")
@pytest.mark.parametrize("data", data_post_RegisterDomain_success)
def test_RegisterDomain_success(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_async/data_post_RegisterDomain_success，comment is：%s" % data["comment"])
    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).post_registerDomain(data["body"])
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    task_no = query_res["Result"]["task_no"]  # 首先：query_res是一个字典，然后将query_res下的Result下的task_no的值，赋值给了task_no
    assert_that(task_no).starts_with("new")  # 使用断言assert_that判断task_no的值是不是以new开头(starts.with)

    no_list = (query_res["Result"]["task_no"])
    print(no_list)


# @allure.title("注册新增.cn的后缀") # 当时是为了测试新添加的cn的后缀时，所添加的Case
# @pytest.mark.parametrize("data",data_newZone_RegisterDomain)
# def test_newZone_RegisterDomain(volc_domain_client_openapi_d2,data):
#     logging.info("Test Case：/data_async/data_post_RegisterDomain_success，comment is：%s" % data["comment"])
#     statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi_d2).post_registerDomain(data["body"])
#     logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))
#     # time.sleep(2)
#
#     assert_that(statusCode).is_equal_to(data["code"])
#     task_no = query_res["Result"]["task_no"]  # 首先：query_res是一个字典，然后将query_res下的Result下的task_no的值，赋值给了task_no
#     assert_that(task_no).starts_with("new")  # 使用断言assert_that判断task_no的值是不是以new开头(starts.with)
#
#     no_list = (query_res["Result"]["task_no"])
#     print(no_list)







@allure.title("域名注册失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "域名异步注册")
@pytest.mark.parametrize("data", data_post_RegisterDomain_error)
def test_RegisterDomain_error(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_async/data_post_RegisterDomain_error，comment is：%s" % data["comment"])
    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).post_registerDomain(data["body"])
    logging.info("query single domain status is --> %s & result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    # 因为断言的域名可能会有差别，所以取返回的CodeN，这个是一致的
    assert_that(query_res["ResponseMetadata"]["Error"]["CodeN"]).is_equal_to(data["ResponseMetadata"]["Error"]["CodeN"])


@allure.title("获取域名列表--成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "获取域名列表")
@pytest.mark.parametrize("data", data_get_ListDomains)
def test_domain_listDomains(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_domain_listDomains，comment is：%s" % data["comment"])
    # data_index = data_get_ListDomains.index(data)
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_listDomains(**data["params"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))
    assert_that(statusCode).is_equal_to(data["code"])
    # if data_index == 0:
    #     print(f'global_domain:{query_res["Result"]["domain_info_list"][0]["domain"]},\nglobal_expired_time:{query_res["Result"]["domain_info_list"][0]["expired_time"]}')


@allure.title("获取域名详情--成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "获取域名详情")
@pytest.mark.parametrize("data", data_get_GetDomain_success)
def test_doamin_getDomain_success(volc_domain_client_openapi, data):
    logging.info("Test Case: /data_management/data_domain_getDomain_success, comment is : %s" % data["comment"])
    # 判断domain_info 库内的最新一条数据是否不等于512，若是不等于512，
    # 则执行domain_customize方法，将库内最新三条的域名状态由256改成512，然后继续执行Case。
    if domain_customize_select("SELECT dn_audit_status FROM domain_info WHERE account_id ='2100266070' AND supplier ='xinNet' ORDER BY `id` DESC")[0][0] != 512:
        print("验证一下上面判断是否成立，成立则打印这句话")
        domain_select_update("", "UPDATE domain_info SET dn_audit_status = '512' WHERE account_id = '2100266070' AND dn_audit_status = '256' AND status = '1' AND verify_status = '4' AND supplier = 'xinNet' ORDER BY `id` DESC LIMIT 3")
    else:
        print("判断条件不成立：不用更新状态码")
    if len(data["sql"]) > 0:  # 判断data中的sql语句是否大于0，如果大于0，则执行下方的语句
        # 更新params中的domain
        data["params"].update({"domain": db_check.domain_select_update(select_sql=data["sql"]["select"], update_sql=data["sql"]["update"])})
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_getDomain(**data["params"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("获取域名详情--失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "获取域名详情")
@pytest.mark.parametrize("data", data_get_GetDomain_error)
def test_doamin_getDomain_error(volc_domain_client_openapi, data):
    logging.info("Test Case: /data_management/data_domain_getDomain_error, comment is : %s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_getDomain(**params)
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])


@allure.title("获取域名证书URL--成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P1", "获取域名证书URL")
@pytest.mark.parametrize("data", data_get_GetDomainCertificateUrl_success)
def test_domain_GetDomainCertificateUrl_success(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_GetDomainCertificateUrl_success，comment is：%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_getDomainCertificateUrl(
        **params)
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))
    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("获取域名证书URL--失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P1", "获取域名证书URL")
@pytest.mark.parametrize("data", data_get_GetDomainCertificateUrl_error)
def test_domain_GetDomainCertificateUrl_error(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_GetDomainCertificateUrl_error，comment is：%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).get_getDomainCertificateUrl(
        **params)
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))
    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])


@allure.title("域名异步续费-->成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "域名异步续费")
@pytest.mark.parametrize("data", data_post_RenewDomain_success)
def test_RennewDomain_success(volc_domain_client_openapi, data):
    logging.info("数据路径：/data_post_RenewDomain_success，用例名称是：%s" % data["comment"])

    data["body"]["domain"] = db_check.domain_customize_select(sql=data["sql1"]["select"])[0][0]
    data["body"]["current_expired_time"] = db_check.domain_customize_select(sql=data["sql2"]["select"])[0][0]
    expired_time = data["body"]["current_expired_time"]  # 将获取到的日期赋值给expired_time
    data["body"]["current_expired_time"] = convert_to_timestamp(expired_time)  # 使用方法，将expired_time转换成时间戳，然后赋值给 data["body"]["current_expired_time"]

    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).post_renewDomain(data["body"])
    logging.info("查询状态码是：-->%s & 返回结果内容是：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    task_no = query_res["Result"]["task_no"]
    assert_that(task_no).starts_with("renew")


@allure.title("域名异步续费-->失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "域名异步续费")
@pytest.mark.parametrize("data", data_post_RenewDomain_error)
def test_RenewDomain_error(volc_domain_client_openapi, data):
    logging.info("数据路径：/data_post_RenewDomain_error，用例名称是：%s" % data["comment"])
    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).post_renewDomain(data["body"])
    logging.info("查询状态码是：-->%s & 返回结果内容是：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["ResponseMetadata"]["Error"])


@allure.title("域名异步过户-成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "域名异步过户")
@pytest.mark.parametrize("data", data_post_Domain_RegistrantChange_success)
def test_DomainRegistrantChange_success(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_post_Domain_RegistrantChange_success,用例名称是：%s" % data["comment"])
    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).post_domainRegistrantChange(data["body"])
    logging.info("查询的状态码是-->%s & 返回结果内容是-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    task_no = query_res["Result"]["task_no"]  # 首先：query_res是一个字典，然后将query_res下的Result下的task_no的值，赋值给了task_no
    assert_that(task_no).starts_with("registrant")  # 使用断言assert_that判断task_no的值是不是以 registrant 开头(starts.with)


@allure.title("域名异步过户-失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "域名异步过户")
@pytest.mark.parametrize("data", data_post_Domain_RegistrantChange_error)
def test_DomainRegistrantChange_error(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_post_Domain_RegistrantChange_error,用例名称是：%s" % data["comment"])
    if len(data["sql"]) > 0:
        data["body"].update({"domain": db_check.domain_select_update(select_sql=data["sql"]["select"], update_sql=data["sql"]["update"])})
    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).post_domainRegistrantChange(data["body"])
    logging.info("查询的状态码是-->%s & 返回结果内容是-->%s" % (statusCode, query_res))
    # data里第二条数据，需要过户中的域名，然后就写了个sql，将某条数据的status=2
    # 然后下面这个sql语句是将那个改成status=2的域名改回status=1，不然就会一直一直一直的lark提醒报错
    db_check.domain_select_update(select_sql="", update_sql="UPDATE domain_info SET status='1' WHERE account_id='2100266070' AND status='2' LIMIT 1")
    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["ResponseMetadata"]["Error"])


@allure.title("查询异步任务详情")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P0", "查询异步任务详情")
@pytest.mark.parametrize("data", data_get_GetAsyncTask)
def test_GetAsyncTask(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_Get_GetAsyncTask_success,用例名称是：%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomainServiceAsync(client=volc_domain_client_openapi).get_getAsyncTask(**params)
    logging.info("查询的状态码是-->%s & 返回结果内容是-->%s" % (statusCode, query_res))
    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("修改域名NS-成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P1", "修改域名NS")
@pytest.mark.parametrize("data", data_post_ModifyDomainNS_success)
def test_domain_listDomains_success(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_ModifyDomainNS_success，comment is：%s" % data["comment"])
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).post_modifyDomainNS(data["body"], )
    # logging.info(data["body"]["domain"], "查看这个域名是什么")
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))
    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("修改域名NS-失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P1", "修改域名NS")
@pytest.mark.parametrize("data", data_post_ModifyDomainNS_error)
def test_domain_listDomains_error(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_ModifyDomainNS_error，comment is：%s" % data["comment"])
    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).post_modifyDomainNS(data["body"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))
    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])


@allure.title("开启自动续费功能-成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P1", "开启/关闭域名自动续费功能")
@pytest.mark.parametrize("data", data_post_SetDomainAutoRenew_success)
def test_domain_SetDomainAutoRenew_success(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_post_SetDomainAutoRenew_success，comment is：%s" % data["comment"])
    domain = domain_customize_select(data["domain_sql"])[0][0]
    # domain = str(domain)
    data["body"]["domain"] = domain

    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).post_setDomainAutoRenew(data["body"], )
    logging.info(data["body"]["domain"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("开启自动续费功能-失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P1", "开启/关闭域名自动续费功能")
@pytest.mark.parametrize("data", data_post_SetDomainAutoRenew_error)
def test_domain_SetDomainAutoRenew_error(volc_domain_client_openapi, data):
    logging.info("Test Case：/data_management/data_post_SetDomainAutoRenew_error，comment is：%s" % data["comment"])

    statusCode, query_res = DomainServiceManager(client=volc_domain_client_openapi).post_setDomainAutoRenew(data["body"], )
    logging.info(data["body"]["domain"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["Resp"]["Error"])
