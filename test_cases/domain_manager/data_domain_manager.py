import random

# 开启/关闭自动续费功能--成功
data_post_SetDomainAutoRenew_success = [
    {
        "comment": "自动续费-->开启",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "qwq-test020.top",
            "is_auto_renew": True
        },
        "code": 200
    },
    {
        "comment": "自动续费-->开启",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "qwq-test009.top",
            "is_auto_renew": False
        },
        "code": 200
    }
]

# 开启/关闭自动续费功能--失败
data_post_SetDomainAutoRenew_error = [
    {
        "comment": "域名状态为'已过期'，不支持此操作",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "送证书.com",
            "is_auto_renew": True
        },
        "code": 458,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 458,
                "Message": "【送证书.com】当前域名状态无法进行该操作"
            }
        }
    },
    {
        "comment": "域名状态为'赎回期'，不支持此操作",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "资源包2.com",
            "is_auto_renew": False
        },
        "code": 458,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 458,
                "Message": "【资源包2.com】当前域名状态无法进行该操作"
            }
        }
    },
    {
        "comment": "域名状态为'已废弃'，不支持此操作",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "免费证书.com",
            "is_auto_renew": True
        },
        "code": 458,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 458,
                "Message": "【免费证书.com】当前域名状态无法进行该操作"
            }
        }
    },
    {
        "comment": "域名状态为'已转出'，不支持此操作",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "d-test112.cn",
            "is_auto_renew": True
        },
        "code": 458,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 458,
                "Message": "【d-test112.cn】当前域名状态无法进行该操作"
            }
        }
    },
    {
        "comment": "域名状态为'赎回中'，不支持此操作",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "nkn.com",
            "is_auto_renew": True
        },
        "code": 458,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 458,
                "Message": "【nkn.com】当前域名状态无法进行该操作"
            }
        }
    },
    {
        "comment": "域名状态为'转移中'，不支持此操作",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，导致查看不到详情，建议以可变参数传入，或者重新更改参数。
            "domain": "d-testbbb.com",
            "is_auto_renew": True
        },
        "code": 458,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 458,
                "Message": "【d-testbbb.com】当前域名状态无法进行该操作"
            }
        }
    },
]

from util.lib import get_uuid
from util.lib import get_uuid16

# 域名询价--成功
data_get_QuerySingle_DomainPrice_success = [
    # 找了几个常用的域名后缀进行测试
    {
        "comment": "英文+com域名询价",
        "params": {
            "domain": get_uuid(),
            "zone": ".com"
        },
        "code": 200,
        "Result": {
            "domain": "yiyayiyayi.com",
            "zone": ".com",
            "status": "1",
            "is_limit_domain": False,
            # PS：如若报错了，说明价格有改动，改一下价格即可
            "first_price": "66",
            "renew": "88",
            "restore_price": "",
            "tag_list": [],
            "domain_type": "E",
            "price_type": "0",
            "notice_info": "",
            "use_resource_package": False
        }
    },
    {
        "comment": "英文+cn域名询价",
        "params": {
            "domain": get_uuid(),
            "zone": ".cn"
        },
        "code": 200,
        "Result": {
            "domain": "1433223.cn",
            "zone": ".cn",
            "status": "1",
            "is_limit_domain": False,
            # PS：如若报错了，说明价格有改动，到时候麻烦手动改一下这里的价格，以免看到不一样的容易混乱
            "first_price": "32",
            "renew": "38",
            "restore_price": "",
            "tag_list": [],
            "domain_type": "E",
            "price_type": "0",
            "notice_info": "",
            "use_resource_package": False
        }
    },
    {
        "comment": "中文+top域名询价",
        "params": {
            "domain": "中文" + get_uuid(),
            "zone": ".top"
        },
        "code": 200,
        "Result": {
            "domain": "yiyayiyay中文.top",
            "zone": ".top",
            "status": "1",
            "is_limit_domain": False,
            # PS：如若报错了，说明价格有改动，到时候麻烦手动改一下这里的价格，以免看到不一样的容易混乱
            "first_price": "13",
            "renew": "33",
            "restore_price": "",
            "tag_list": [],
            "domain_type": "G",
            "price_type": "0",
            "notice_info": "",
            "use_resource_package": False
        }
    },
    {
        "comment": "中文+xyz域名询价",
        "params": {
            "domain": "中文" + get_uuid(),
            "zone": ".xyz"
        },
        "code": 200,
        "Result": {
            "domain": "阿三哥电视电话中文.xyz",
            "zone": ".xyz",
            "status": "1",
            "is_limit_domain": False,
            # PS：如若报错了，说明价格有改动，到时候麻烦手动改一下这里的价格，以免看到不一样的容易混乱
            "first_price": "19",
            "renew": "86",
            "restore_price": "",
            "tag_list": [],
            "domain_type": "G",
            "price_type": "0",
            "notice_info": "",
            "use_resource_package": False
        }
    },
    {
        "comment": "纯数字+net域名询价",
        "params": {
            "domain": "1433223",
            "zone": ".net"
        },
        "code": 200,
        "Result": {
            "domain": "1433223.net",
            "zone": ".net",
            "status": "1",
            "is_limit_domain": False,
            # PS：如若报错了，说明价格有改动，到时候麻烦手动改一下这里的价格，以免看到不一样的容易混乱
            "first_price": "95",
            "renew": "102",
            "restore_price": "",
            "tag_list": [],
            "domain_type": "E",
            "price_type": "0",
            "notice_info": "",
            "use_resource_package": False
        }
    }
]

# 域名询价--失败
data_get_QuerySingle_DomainPrice_error = [
    {
        "comment": "空后缀-->域名格式错误",
        "params": {
            "domain": "keaidehuya",
            "zone": ""
        },
        "code": 200,
        "Result": {
            "domain": "keaidehuya",
            "zone": "",
            "status": "0",
            "is_limit_domain": False,
            "first_price": "",
            "renew": "",
            "restore_price": "",
            "tag_list": None,
            "domain_type": "",
            "price_type": "",
            "notice_info": "域名格式错误",
            "use_resource_package": False
        }
    },
    {
        "comment": "空域名-->域名后缀，不能注册",
        "params": {
            "domain": "",
            "zone": ".com"
        },
        "code": 200,
        "Result": {
            "domain": ".com",
            "zone": ".com",
            "status": "0",
            "is_limit_domain": False,
            "first_price": "",
            "renew": "",
            "restore_price": "",
            "tag_list": None,
            "domain_type": "",
            "price_type": "",
            "notice_info": "域名后缀，不能注册",
            "use_resource_package": False
        }
    },
    {
        "comment": "泛域名-->域名格式错误",
        "params": {
            "domain": "*",
            "zone": ".com"
        },
        "code": 200,
        "Result": {
            "domain": "*.com",
            "zone": ".com",
            "status": "0",
            "is_limit_domain": False,
            "first_price": "",
            "renew": "",
            "restore_price": "",
            "tag_list": None,
            "domain_type": "",
            "price_type": "",
            "notice_info": "域名格式错误",
            "use_resource_package": False
        }
    },
    {
        "comment": "域名前+横杠-->域名格式错误",
        "params": {
            "domain": "-baidu",
            "zone": ".com"
        },
        "code": 200,
        "Result": {
            "domain": "-baidu.com",
            "zone": ".com",
            "status": "0",
            "is_limit_domain": False,
            "first_price": "",
            "renew": "",
            "restore_price": "",
            "tag_list": None,
            "domain_type": "",
            "price_type": "",
            "notice_info": "域名格式错误",
            "use_resource_package": False
        }
    },
    {
        "comment": "域名超过63位字符-->域名格式错误",
        "params": {
            "domain": "wxuyaochaoguo63gezifu" + get_uuid16() + get_uuid() + get_uuid(),  # 等于64位字符,刚好超过63位字符
            "zone": ".com"
        },
        "code": 200,
        "Result": {
            "domain": "xuyaochaoguo63gezifu2a56fba8-96a1-493e-bb61-6500437d29032c6a74fe14ee47c5.com",
            "zone": ".com",
            "status": "0",
            "is_limit_domain": False,
            "first_price": "",
            "renew": "",
            "restore_price": "",
            "tag_list": None,
            "domain_type": "",
            "price_type": "",
            "notice_info": "域名格式错误",
            "use_resource_package": False
        }
    },
]

# 添加单个域名到购物车--成功
data_post_AddDomain_ToShoppingList_success = [
    {
        "comment": "添加单个.cn 域名到购物车",
        "body": {
            "domain": "congcongnanian.cn",
            "zone": ".cn"
        },
        "code": 200
    },
    {
        "comment": "添加单个.com 域名到购物车",
        "body": {
            "domain": "congcongnanian.com",
            "zone": ".com"
        },
        "code": 200
    },
    {
        "comment": "添加单个.net 域名到购物车",
        "body": {
            "domain": "congcongnanian.net",
            "zone": ".net"
        },
        "code": 200
    },
    {
        "comment": "添加单个.top 域名到购物车",
        "body": {
            "domain": "congcongnanian.top",
            "zone": ".top"
        },
        "code": 200
    },
    {
        "comment": "添加单个.xyz 域名到购物车",
        "body": {
            "domain": "congcongnanian.xyz",
            "zone": ".xyz"
        },
        "code": 200
    },

]

# 添加批量域名到购物车--成功
data_post_BatchAddDomain_ToShoppingList = [
    {
        "comment": "购物车内数据未满，批量添加30个",
        "body": [
            {
                "domain": f"tztest{i}.cn",
                "zone": ".cn"
            } for i in range(1, 101)
        ],
        "code": 200
    },
    {
        "comment": "购物车内有数据，添加重复域名到购物车",
        "body": [
            {
                "domain": f"tztest{i}.cn",
                "zone": ".cn"
            } for i in range(1, 31)
        ],
        "code": 200
    }
    # ,
    # # 此方法与上述作用一致，都是批量添加所用
    # {
    #     "comment": "批量添加域名",
    #     "body": {
    #         "domain": "%s-%s%s" % ("tztast", random.randint(1, 101), "xyz"),
    #         "zone": "xyz"
    #     }
    #
    # }
]

# 添加域名到购物车--失败
data_post_AddDomain_ToShoppingList_error = [
    {
        "comment": "购物车已达上限，继续添加域名带购物车-0",
        "body": {
            "domain": "cctest.cn",
            "zone": ".cn"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "购物车达到上线啦"
            }
        }
    },
    {
        "comment": "购物车已达上限，继续添加域名带购物车-1",
        "body": {
            "domain": "tz-test1.cn",
            "zone": ".cn"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "购物车达到上线啦"
            }
        }
    },
    {
        "comment": "购物车已达上限，继续添加域名带购物车-2",
        "body": {
            "domain": "tz-test2.cn",
            "zone": ".cn"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "购物车达到上线啦"
            }
        }
    },
    {
        "comment": "添加域名--无域名",
        "body": {
            "domain": ".com",
            "zone": ".com"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "invalid domain: .com"
            }
        }
    },
    {
        "comment": "添加域名--无后缀",
        "body": {
            "domain": "baidu.com",
            "zone": ""
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "invalid request parameter"
            }
        }
    },
    {
        "comment": "添加域名--泛域名",
        "body": {
            "domain": "*.com",
            "zone": ".com"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "invalid domain: *.com"
            }
        }
    },
    {
        "comment": "添加域名--超过63为字符的",
        "body": {
            "domain": "wxuyaochaoguo63geziyawxuyaochaoguo63geziyawxuyaochaoguo63geziyaw.com",
            "zone": ".com"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "domain is too long: wxuyaochaoguo63geziyawxuyaochaoguo63geziyawxuyaochaoguo63geziyaw.com"
            }
        }
    },
    {
        "comment": "添加域名--域名前带横杠",
        "body": {
            "domain": "-baidu123.com",
            "zone": ".com"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "invalid domain: -baidu123.com"
            }
        }
    },
    {
        "comment": "购物车已满，添加域名",
        "body": {
            "domain": "gangming123.com",
            "zone": ".com"
        },
        "code": 400,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 400,
                "Message": "购物车达到上线啦"
            }
        }
    }
]

# 清空购物车---无需填写参数
data_get_ClearShoppingList = []

# 获取购物车列表内容
data_get_GetShoppingList = [
    {
        "comment": "获取购物车列表内容",
        "code": 200
    }
]
