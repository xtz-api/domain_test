import logging
import pytest
import allure
from assertpy import assert_that
from test_domain.domian_test.api_test import DomainServiceTemplate
from test_domain.domian_test.data_api import *


"""/template/list"""
@allure.title("获取模板列表")
@pytest.mark.executor("lanzitong")
@pytest.mark.tag("P1", "template")
@pytest.mark.parametrize("data", data_domain_get_templateList)
def test_domain_getTemplateList(volc_domnain_client, data):
    logging.info("Test Case: /template/list, comment is : %s"%data["comment"] )
    kwargs = data["input"]
    statusCode, template_list = DomainServiceTemplate(client=volc_domnain_client).template_list(**kwargs)
    logging.info("template list is  -> %s"%(template_list))
    assert_that(statusCode).is_equal_to(data["code"])