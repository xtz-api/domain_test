import logging

from test_cases.api_domain_service_base import DomainService
from conf.constant import CONSTANT
import copy
import time
import random
import re


def get_domain_list(volc_domnain_client, num):
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')
    kwargs = {}
    domain_list = []
    time_s = 283824000
    data = {"test_cases": "sdgfuwhdiuehfu.cn",
            "period": 1,
            "zone": ".cn",
            "renew_price": "5000"}
    status = []
    verify_status = []
    resp = DomainService(client=volc_domnain_client).domain_list(**kwargs)
    logging.info(resp)
    for domain_data in resp["Result"]["domain_info_list"]:
        if num != 10:
            if domain_data["status"] in [1, 2, 4] and domain_data["expired_time"] - int(time.time()) <= time_s:
                if not zhmodel.search(domain_data["test_cases"][:len(domain_data["zone"])]):
                    if len(domain_list) == num:
                        break
                    data["test_cases"] = domain_data["test_cases"]
                    data["zone"] = domain_data["zone"]
                    data["renew_price"] = CONSTANT.renewal_fee[domain_data["zone"]]
                    domain_list.append(copy.deepcopy(data))
        else:
            if domain_data["status"] not in status:
                status.append(domain_data["status"])
                if not zhmodel.search(domain_data["test_cases"][:len(domain_data["zone"])]):
                    if len(domain_list) == num:
                        break
                    data["test_cases"] = domain_data["test_cases"]
                    data["zone"] = domain_data["zone"]
                    data["renew_price"] = CONSTANT.renewal_fee[domain_data["zone"]]
                    domain_list.append(copy.deepcopy(data))
            elif domain_data["verify_status"] not in verify_status:
                verify_status.append(domain_data["verify_status"])
                if not zhmodel.search(domain_data["test_cases"][:len(domain_data["zone"])]):
                    if len(domain_list) == num:
                        break
                    data["test_cases"] = domain_data["test_cases"]
                    data["zone"] = domain_data["zone"]
                    data["renew_price"] = CONSTANT.renewal_fee[domain_data["zone"]]
                    domain_list.append(copy.deepcopy(data))
            elif domain_data["status"] == 8:
                if not zhmodel.search(domain_data["test_cases"][:len(domain_data["zone"])]):
                    if len(domain_list) == num:
                        break
                    data["test_cases"] = domain_data["test_cases"]
                    data["zone"] = domain_data["zone"]
                    data["renew_price"] = CONSTANT.renewal_fee[domain_data["zone"]]
                    domain_list.append(copy.deepcopy(data))
    # logging.info(status)
    # logging.info(domain_list)
    return domain_list


def get_domain_data(volc_domnain_client, **kwargs):
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')
    resp = DomainService(client=volc_domnain_client).domain_list(**kwargs)
    # logging.info(resp)
    for j in range(0, 20):
        i = random.randint(0, len(resp["Result"]["domain_info_list"]) - 1)
        domain = resp["Result"]["domain_info_list"][i]["test_cases"]
        if not zhmodel.search(domain):
            return domain
