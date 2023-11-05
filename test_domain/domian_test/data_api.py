data_domain_get_templateDetail = [
    {
        "comment": "获取当前用户的某个模板详情",
        "input": {
            "template": 482
        },
        "code": 200,
        "sql": "select count(*) from `domain_template`where `account`=2100000056 and `id`=482"
    },
    {
        "comment": "获取非当前用户的某个模板详情",
        "input": {
            "template": 453
        },
        "code": 472,
        "sql": "select count(*)  from `domain_template`where `account`=2100000056 and `id`=453"
    }
]
data_domain_get_templateList = [{
    "comment": "删除购物车列表中包含的域名",
    "input": {
        "page_size": 10,
        "page_number": 1,
        "registration_type": "C",
        "status_mask": 7
    },
    "code": 200,
    "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` IN (1,2,4) and `registration_type`='C'"
},
    {
        "comment": "查询当前用户下所有的信息模板",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": ""
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` <>0"
    },
    {
        "comment": "查询当前用户下所有企业模板",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "C"
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` <>0 and `registration_type`='C'"
    },
    {
        "comment": "查询当前用户下所有个人模板",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "P"
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` <>0 and `registration_type`='P'"
    },
    {
        "comment": "查询当前用户下所有模板 + 未实名认证",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "",
            "status_mask": 1
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` = 1"
    },
    {
        "comment": "查询当前用户下所有模板 + 未实名认证 + 实名认证中",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "",
            "status_mask": 3
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` IN (1,2)"
    },
    {
        "comment": "查询当前用户下所有模板 + 未实名认证 + 实名认证中 + 实名认证成功",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "",
            "status_mask": 7
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` IN (1,2,4)"
    },
    {
        "comment": "查询当前用户下所有模板 + 未实名认证 + 实名认证中 + 实名认证失败",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "",
            "status_mask": 11
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` IN (1,2,8)"
    },
    {
        "comment": "查询当前用户下存在的模板",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "",
            "name": "test"
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` <>0 and `registrant` LIKE '%test%'"
    },
    {
        "comment": "查询当前用户下不存在的模板",
        "input": {
            "page_size": 10,
            "page_number": 1,
            "registration_type": "",
            "name": "bucunzaidemuban"
        },
        "code": 200,
        "sql": "select count(*) from `domain_template` where `account`=2100000056 and `status` <>0 and `registrant` LIKE '%bucunzaidemuban%'"
    },
    # {
    #     "comment": "查询参数异常",
    #     "input": {
    #         "page_size": -1,
    #         "page_number": -1,
    #         "registration_type": "",
    #     },
    #     "code" : 500
    # }
]
