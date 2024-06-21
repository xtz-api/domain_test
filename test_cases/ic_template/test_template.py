import pytest
import allure
import logging
from assertpy import assert_that
from test_cases.ic_template.api_template import *
from test_cases.ic_template.data_template import *


@allure.title("创建自然人模板-->成功")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "创建模板")
@pytest.mark.parametrize("data", data_post_CreateTemplate_Natural)
def test_createTemplate_Natural(volc_ic_client, data):
    logging.info("Test Case：-->/data_template/data_post_CreateTemplate_Natural，comment：-->%s" % data["comment"])
    statusCode, query_res = IcTemplateAPI(client=volc_ic_client).post_createTemplate(data["body"])
    logging.info("code is -->%s；Result is-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    TemplateID = query_res["Result"]["TemplateID"]
    assert_that(TemplateID).starts_with("178")


@allure.title("创建法人模板-->成功")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "创建模板")
@pytest.mark.parametrize("data", data_post_CreateTemplate_Legal)
def test_createTemplate_Legal(volc_ic_client, data):
    logging.info("Test Case：-->/data_template/data_post_CreateTemplate_Legal，comment：-->%s" % data["comment"])
    statusCode, query_res = IcTemplateAPI(client=volc_ic_client).post_createTemplate(data["body"])
    logging.info("code is -->%s；Result is-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    TemplateID = query_res["Result"]["TemplateID"]
    assert_that(TemplateID).starts_with("178")


@allure.title("创建法人模板-->失败")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "创建模板")
@pytest.mark.parametrize("data", data_post_CreateTemplate_error)
def test_createTemplate_error(volc_ic_client, data):
    logging.info("Test Case：-->/data_template/data_post_CreateTemplate_error，comment：-->%s" % data["comment"])
    statusCode, query_res = IcTemplateAPI(client=volc_ic_client).post_createTemplate(data["body"])
    logging.info("code is -->%s；Result is-->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
    assert_that(query_res["ResponseMetadata"]["Error"]).is_equal_to(data["ResponseMetadata"]["Error"])


@allure.title("查看模板详情")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "查看模板详情")
@pytest.mark.parametrize("data", data_get_Template)
def test_getTemplate(volc_ic_client, data):
    logging.info("Test Case：-->/data_template/data_get_template，comment：-->%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = IcTemplateAPI(client=volc_ic_client).get_getTemplate(**params)
    logging.info("code is -->%s；Result is -->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("查看模板列表")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "查看模板列表")
@pytest.mark.parametrize("data", data_get_ListTemplate)
def test_LisTemplate(volc_ic_client, data):
    logging.info("Test Case：-->/data_get_ListTemplate，comment：-->%s" % data["comment"])
    params = data["params"]
    statusCode, query_res = IcTemplateAPI(client=volc_ic_client).get_listTemplates(**params)
    logging.info("code is -->%s；Result is -->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])


@allure.title("更新模板信息")
@pytest.mark.executro("陶陶陶")
@pytest.mark.tag("P0", "更新模板信息")
@pytest.mark.parametrize("data", data_post_UpdateTemplate)
def test_UpdateTemaplate(volc_ic_client, data):
    logging.info("Test Case：-->/data_post_UpdateTemplate，comment：-->%s" % data["comment"])
    statusCode, query_res = IcTemplateAPI(client=volc_ic_client).post_updateTemplate(data["body"])
    logging.info("code is -->%s；Result is -->%s" % (statusCode, query_res))

    assert_that(statusCode).is_equal_to(data["code"])
