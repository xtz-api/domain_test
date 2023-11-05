import logging
import random

from assertpy import assert_that

from domain.api_domain_service_base import DomainService
from util import db_check


def setup_domain_addShoppingList(volc_domnain_client, data):
    if data["comment"] == "购物车已满，加购未被注册域名":
        "1. 确保购物车中已有100条域名数据"
        while len(db_check.domain_get_shopingList_db()) < 100:
            cur_size = len(db_check.domain_get_shopingList_db())
            for i in range(100 - cur_size):
                domain = '%s-%s%s' % ('rstest',random.randint(0,10000), ".top" )
                body = {
                    "test_domain": domain,
                    "zone": ".top"}
                _, resp = DomainService(client=volc_domnain_client).domain_add_shoppingList(body)
                assert_that(_).is_equal_to(200)
        assert_that(len(db_check.domain_get_shopingList_db())).is_equal_to(100)
    elif data["comment"] == "购物车未满，加购未被注册域名":
        domain_info = db_check.domain_get_shopingList_by_domain(data["input"]["test_domain"])
        logging.info(domain_info)
        if domain_info != ():
            body = {
                "id" : domain_info[0][0]
            }
            _, resp = DomainService(client=volc_domnain_client).domain_del_shoppingList(**body)
            assert_that(_).is_equal_to(200)
        assert_that(db_check.domain_get_shopingList_by_domain(data["input"]["test_domain"])).is_empty()
        while len(db_check.domain_get_shopingList_db()) ==100:
            DomainService(client=volc_domnain_client).domain_clear_shoppingList()
    elif data["comment"] == "购物车未满，加购已被注册域名":
        while len(db_check.domain_get_shopingList_db()) ==100:
            DomainService(client=volc_domnain_client).domain_clear_shoppingList()
        domain_info = db_check.domain_get_shopingList_by_domain(data["input"]["test_domain"])
        if domain_info != ():
            logging.info("当前数据库已经有该域名存在")
            return
        DomainService(client=volc_domnain_client).domain_add_shoppingList(data["input"])
        assert_that(db_check.domain_get_shopingList_by_domain(data["input"]["test_domain"])).is_not_empty()