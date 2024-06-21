import logging
import allure
import pytest
from assertpy import assert_that
from test_cases.domain_manager.api_domain_manager import DomianServiceManager
from test_cases.domain_manager.data_domain_manager import *


@allure.title("开启/关闭域名域名自动续费-->成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P2", "开启/关闭域名域名自动续费")
@pytest.mark.parametrize("data", data_post_SetDomainAutoRenew_success)
def test_domainAutoRenew_success(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_success & comment is -->:%s" % data["comment"])
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).post_SetAutoRenew(data["body"])
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("开启/关闭域名自动续费功能-->失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P2", "开启/关闭域名自动续费功能")
@pytest.mark.parametrize("data", data_post_SetDomainAutoRenew_error)
def test_domainAutoRenew_error(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_error & comment is -->：%s" % data["comment"])
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).post_SetAutoRenew(data["body"])
    logging.info("返回状态码是-->：%s & 返回结果内容是-->：%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]["CodeN"]).is_equal_to(data["ResponseMetadata"]["Error"]["CodeN"])


@allure.title("询价-->成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P1", "域名询价")
@pytest.mark.parametrize("data", data_get_QuerySingle_DomainPrice_success)
def test_QuerySingleDomainPrice_success(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_success & comment is -->:%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).get_QuerySingle_DomainPrice(**params)
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["Result"]["first_price"]).is_equal_to(data["Result"]["first_price"])


@allure.title("询价-->失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P1", "域名询价")
@pytest.mark.parametrize("data", data_get_QuerySingle_DomainPrice_error)
def test_QuerySingleDomainPrice_error(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_error & comment is -->：%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).get_QuerySingle_DomainPrice(**params)
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["Result"]["notice_info"]).is_equal_to(data["Result"]["notice_info"])


@allure.title("添加单个域名到购物车-->成功")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P1", "添加单个域名到购物车")
@pytest.mark.parametrize("data", data_post_AddDomain_ToShoppingList_success)
def test_AddDomain_ToShoppingList_success(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_AddDomain_ToShoppingList_success & comment is -->：%s" % data["comment"])
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).post_AddDomain_ToShoppingList(data["body"])
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    # assert_that(query_res["Result"]["notice_info"]).is_equal_to(data["Result"]["notice_info"])


@allure.title("批量添加100个")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P1", "批量添加域名到购物车")
@pytest.mark.parametrize("data", data_post_BatchAddDomain_ToShoppingList)
def test_BatchAddDomain_ToShoppingList(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_error & comment is -->：%s" % data["comment"])
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).post_BatchAddDomain_ToShoppingList(data["body"])
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("添加单个域名到购物车-->失败")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P1", "添加单个域名到购物车")
@pytest.mark.parametrize("data", data_post_AddDomain_ToShoppingList_error)
def test_AddDomain_ToShoppingList_error(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_error & comment is -->：%s" % data["comment"])
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).post_AddDomain_ToShoppingList(data["body"])
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["Resp"]["Error"])


@allure.title("获取购物车列表")
@pytest.mark.executor("TaoGangMing")
@pytest.mark.tag("P1", "获取购物车列表")
@pytest.mark.parametrize("data", data_get_GetShoppingList)
def test_GetShoppingList1(volc_domain_client, data):
    logging.info("TestCase-->：/data_post_SetDomainAutoRenew_error & comment is -->：%s" % data["comment"])
    statusCode, query_res = DomianServiceManager(client=volc_domain_client).get_GetShoppingList()
    logging.info("domain code is -->：%s，& result1 is --> %s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])

