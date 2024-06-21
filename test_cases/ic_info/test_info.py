import pytest
import allure
import logging
from assertpy import assert_that
from test_cases.ic_info.api_info import *
from test_cases.ic_info.data_info import *


@allure.title("创建工商订单-->成功")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "创建工商订单")
@pytest.mark.parametrize("data", data_post_CreatePreOrder)
def test_createProOrder(volc_ic_client, data):
    logging.info("Test Case：--> /data_post_CreatePreOrder，comment：-->%s" % data["comment"])
    statusCode, query_res = IcInfoAPI(client=volc_ic_client).post_CreatePreOrder(data["body"])
    logging.info("code is --%s & Result is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    OrderID = query_res["Result"]["OrderID"]
    assert_that(OrderID).starts_with("BO")


@allure.title("暂存注册资料-->成功")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "暂存注册资料")
@pytest.mark.parametrize("data", data_post_SaveICRegMaterial_succes)
def test_saveICRegMaterial_succes(volc_ic_client, data):
    logging.info("Test Case：--> /data_post_SaveICRegMaterial_succes，comment：-->%s" % data["comment"])
    statusCode, query_res = IcInfoAPI(client=volc_ic_client).post_SaveICRegmaterial(data["body"])
    logging.info("code is --%s & Result is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("暂存注册资料-->成功")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "暂存注册资料")
@pytest.mark.parametrize("data", data_post_SaveICRegMaterial_error)
def test_saveICRegMaterial_error(volc_ic_client, data):
    logging.info("Test Case：--> /data_post_SaveICRegMaterial_succes，comment：-->%s" % data["comment"])
    statusCode, query_res = IcInfoAPI(client=volc_ic_client).post_SaveICRegmaterial(data["body"])
    logging.info("code is --%s & Result is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["resp"]["Error"])
