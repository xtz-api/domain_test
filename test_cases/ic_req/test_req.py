import logging
import pytest
import allure
from assertpy import assert_that

from util import db_check
from util.db_check import *
from test_cases.ic_req.api_req import *
from test_cases.ic_req.data_req import *


@allure.title("创建需求-成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "创建需求")
@pytest.mark.parametrize("data", data_post_CreateReq_success)
def test_createReq_success(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_post_CreateReq_success，comment is %s" % data["comment"])
    statusCode, query_res = IcReqAPI(client=volc_ic_client).post_createReq(data["body"])
    # 捕获并处理异常，他的作用是在try块中尝试执行可能会引发异常的代码，如果没有发生异常，则只执行try中的代码；如果捕获到异常，则跳转到相应的except块来处理异常。
    try:
        # 首先判断这个断言是否正确，如果有不正确的则走 下方的except
        assert_that(query_res["Result"]).starts_with("OpportunityID")
    except:
        # 这个logging.error其实是为了针对try中断言失败所用的
        logging.error("断言失败：请查看相关的错误提示并进行排查")
        assert_that(query_res["ResponseMetadata"]["Error"]["Message"]).is_equal_to("当前创建的免费抖音企业号/抖店咨询单总数已超出账号最多1条限制，若有额外需求请提交工单联系人工处理。")


    finally:
        logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

        assert_that(statusCode).is_equal_to(data["code"])

    # try:
    #     # if query_res.get("Result") is not None:
    #     assert_that(query_res["Result"]).starts_with("OpportunityI")
    #     print(11111)
    # except:
    #     assert_that(query_res["ResponseMetadata"]["Error"]["Message"]).is_equal_to("当前创建的免费抖音企业号/抖店咨询单总数已超出账号最多1条限制，若有额外需求请提交工单联系人工处理。")
    #     print(222222)
    # finally:
    #     logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))
    #     assert_that(statusCode).is_equal_to(data["code"])


@allure.title("创建需求-失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "创建需求")
@pytest.mark.parametrize("data", data_post_CreateReq_error)
def test_createReq_error(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_post_CreateReq_error，comment is %s" % data["comment"])
    statusCode, query_res = IcReqAPI(client=volc_ic_client).post_createReq(data["body"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])


@allure.title("获取需求列表数据")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "获取需求列表")
@pytest.mark.parametrize("data", data_get_ListReq)
def test_listReq(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_get_ListReq，comment is %s" % data["comment"])
    # 判断：如果data中的sql的数据大于0：则执行下面一句的SQL语句；如果没有sql则不执行下一句
    if len(data["sql"]) > 0:
        # 使用sql语句将data中的params的参数OpportunityID更新为最新的参数
        data["params"].update({"OpportunityID": db_check.ic_select_update(select_sql=data["sql"]["select"], update_sql=data["sql"]["update"])})

    statusCode, query_res = IcReqAPI(client=volc_ic_client).get_listReq(**data["params"])
    logging.info("返回的结果状态码：--> %s ； 返回的结果内容：--> %s" % (statusCode, query_res))

    # 断言每条数据的code=200
    assert_that(statusCode).is_equal_to(data["code"])
    # 断言'OpportunityID'字段在返回的["Result"]["Data"][0]第一条数据中，否则断言失败
    assert "OpportunityID" in query_res["Result"]["Data"][0]
    # OpportunityID=query_res["Result"]["Data"][0]["OpportunityID"]
    # print(OpportunityID)


@allure.title("获取需求单详情内容")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "获取需求单详情")
@pytest.mark.parametrize("data", data_get_getReq)
def test_getReq(volc_ic_client, data):
    logging.info("测试用例数据搁这儿呢：/data_req/data_get_getReq，comment is %s" % data["comment"])

    if data["params"]["OpportunityID"] is None:
        data["params"].update({"OpportunityID": customize_sql("select req_id from ic_req where account_id='2100266070' order by `id` desc")[0][0]})
        # 方法二
        # OpportunityID=customize_sql("select req_id from ic_req where account_id='2100266070' order by `id` desc")[0][0]
        # data["params"]["OpportunityID"]=OpportunityID
        # print(data["params"]["OpportunityID"])

    statusCode, query_res = IcReqAPI(client=volc_ic_client).get_getReq(**data["params"])
    logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


# @allure.title("关闭需求单--成功")
# @pytest.mark.executor("陶陶陶")
# @pytest.mark.tag("P0", "关闭需求单")
# @pytest.mark.parametrize("data", data_post_closeReq_success)
# def test_closeReq_success(volc_ic_client, data):
#     logging.info("测试用例数据搁这儿呢：/data_req/data_get_getReq_success，comment is %s" % data["comment"])
#     # 用sql语句从数据库中查出最新的OpportunityIDID
#     OpportunityID = customize_sql(data["opportunityID_sql"])[0][0]
#     # 然后将上述查找出来的ID转换成str类型的
#     OpportunityID = str(OpportunityID)
#     logging.info(OpportunityID)
#     data["body"]["OpportunityID"] = OpportunityID
#     logging.info(data["body"]["OpportunityID"])
#
#     statusCode, query_res = IcReqAPI(client=volc_ic_client).post_closeReq(data["body"])
#     logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))
#
#     assert_that(statusCode).is_equal_to(data["code"])


# @allure.title("关闭需求单--失败")
# @pytest.mark.executor("陶陶陶")
# @pytest.mark.tag("P0", "关闭需求单")
# @pytest.mark.parametrize("data", data_post_closeReq_error)
# def test_closeReq_error(volc_ic_client, data):
#     logging.info("Test Case：/data_req/data_get_getReq_error，comment is %s" % data["comment"])
#     # 用sql语句从数据库中查出最新的OpportunityIDID
#     OpportunityID = customize_sql(data["opportunityID_sql"])[0][0]
#     # 然后将上述查找出来的ID转换成str类型的
#     OpportunityID = str(OpportunityID)
#     logging.info(OpportunityID)
#     data["body"]["OpportunityID"] = OpportunityID
#     logging.info(data["body"]["OpportunityID"])
#
#     statusCode, query_res = IcReqAPI(client=volc_ic_client).post_closeReq(data["body"])
#     logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))
#
#     assert_that(statusCode).is_equal_to(data["code"])
#     assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["ResponseMetadata"]["Error"])


@allure.title("创建工商预配置火山订单-->成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "创建工商预配置火山订单")
@pytest.mark.parametrize("data", data_post_CreatePreOrder_success)
def test_createPreOrder_success(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_post_CreatePreOrder_success，comment is %s" % data["comment"])
    statusCode, query_res = IcReqAPI(client=volc_ic_client).post_CreatePreOrder(data["body"])
    logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    OrderID = query_res["Result"]["OrderID"]
    assert_that(OrderID).starts_with("BO")


@allure.title("创建工商预配置火山订单-->失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "创建工商预配置火山订单")
@pytest.mark.parametrize("data", data_post_CreatePreOrder_error)
def test_createPreOrder_error(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_post_CreatePreOrder_error，comment is %s" % data["comment"])
    statusCode, query_res = IcReqAPI(client=volc_ic_client).post_CreatePreOrder(data["body"])
    logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])


@allure.title("创建资质预配置火山订单-->成功")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "创建资质预配置火山订单")
@pytest.mark.parametrize("data", data_post_CreateQualificationOrder_success)
def test_createQualificationOrder_success(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_post_CreateQualificationOrder_success，comment is %s" % data["comment"])
    statusCode, query_res = IcReqAPI(client=volc_ic_client).post_CreateQualificationOrder(data["body"])
    logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    OrderID = query_res["Result"]["OrderID"]
    assert_that(OrderID).starts_with("BO")


@allure.title("创建资质预配置火山订单-->失败")
@pytest.mark.executor("陶陶陶")
@pytest.mark.tag("P0", "创建资质预配置火山订单")
@pytest.mark.parametrize("data", data_post_CreateQualificationOrder_error)
def test_createQualificationOrder_error(volc_ic_client, data):
    logging.info("Test Case：/data_req/data_post_CreateQualificationOrder_success，comment is %s" % data["comment"])
    statusCode, query_res = IcReqAPI(client=volc_ic_client).post_CreateQualificationOrder(data["body"])
    logging.info("返回的结果状态码：-->%s；返回的结果内容：-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])
