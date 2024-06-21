"""
PS：名称是根据此文件+请求方法+action+成功/失败；
     如：data_get_CheckFee_success：data->此文件是存放数据的；get->这个api是get的请求方式；CheckFee->接口url(action)；success/error->参数正确/错误的
"""
from test_cases.constant import *
from util.db_check import *
import random
from util import lib  # 引用了lib中的get_uuid的一个随机参数的方法，会随机生成字母+数字8个字符的值

random_int1 = (lib.get_uuid() + "aaa")
aa1 = (lib.get_uuid16() + "39a88ef6069801b3c09b9db039")
# aa = lib.get_uuid()
# print(aa + "aaaaaaa")
# print(random_int)
# print(aa1)
# print(len("openapi6d-c582-44e8-b7c0-39a88ef6069839a88ef6069801b3c09b9db039"))

random_int = random.randint(0000, 9999)
# print(random_int)
# *****************---域名操作---*****************
# 询价成功
data_get_CheckFee_success = [
    {
        "comment": ".com询价",
        "params": {
            "domain": "baidu.com"
        },
        # code：返回的状态码
        "code": 200,
        "Result": {
            "domain": "baidu.com",
            "zone": ".com",
            "status": "0",
            "is_limit_domain": False,
            "new_price": "",
            "renew_price": "88",
            "restore_price": "836",
            "domain_type": "E",
            "price_type": "0",
            "notice_info": ""
        }
    },
    {
        "comment": ".cn询价",
        "params": {
            "domain": "ccttqwq123.cn"
        },
        "code": 200,
        "Result": {
            "domain": "ccttqwq123.cn",
            "zone": ".cn",
            "status": "1",
            "is_limit_domain": False,
            "new_price": "32",
            "renew_price": "38",
            "restore_price": "",
            "domain_type": "E",
            "price_type": "0",
            "notice_info": ""
        }
    },
    {
        "comment": ".net询价",
        "params": {
            "domain": "baidu.net"
        },
        "code": 200,
        "Result": {
            "domain": "baidu.net",
            "zone": ".net",
            "status": "0",
            "is_limit_domain": False,
            "new_price": "",
            "renew_price": "102",
            "restore_price": "845",
            "domain_type": "E",
            "price_type": "0",
            "notice_info": ""
        }
    },
    {
        "comment": ".top询价",
        "params": {
            "domain": "ccttqwq123.top"
        },
        "code": 200,
        "Result": {
            "domain": "ccttqwq123.top",
            "zone": ".top",
            "status": "1",
            "is_limit_domain": False,
            "new_price": "13",
            "renew_price": "33",
            "restore_price": "",
            "domain_type": "E",
            "price_type": "0",
            "notice_info": ""
        }
    },
]

# 询价失败
data_get_CheckFee_error = [
    {
        "comment": "错误域名格式，空",
        "params": {
            # 域名为空
            "domain": ""
        },
        # code：返回的状态码
        "code": 400,
        # res：返回的数据，用于用例中断言判断
        "res": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "错误请求,请检查参数等是否正确"
            }
        }
    },
    {
        "comment": "错误的域名格式",
        "params": {
            "domain": "*****.com"
        },
        "code": 200,
        "res": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "域名格式错误"
            }
        }
    },
    {
        "comment": "只有前缀域名",
        "params": {
            "domain": "testcc"
        },
        "code": 200,
        "res": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "域名格式错误"
            }
        }
    },
    {
        "comment": "域名包含特殊字符",
        "params": {
            "domain": "test？？@#cc.com"
        },
        "code": 200,
        "res": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "域名格式错误"
            }
        }
    },
    {
        "comment": "域名超过63位",
        "params": {
            "domain": "testcctestcctestcctestcctestcctestcctestcctestcctestcctestccttcc.com"
        },
        "code": 200,
        "res": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "域名格式错误"
            }
        }
    },
    {
        "comment": "错误的后缀",
        "params": {
            "domain": "testcc.aabbcc"
        },
        "code": 200,
        "res": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "暂不支持该后缀"
            }
        }
    },
    # {
    #     "comment": "供应商暂不支持的后缀",
    #     "params": {
    #         "domain": "testcc.ai"
    #     },
    #     "code": 200,
    #     "res": {
    #         "domain": "testcc.ai",
    #         "zone": ".ai",
    #         "status": "3",
    #         "is_limit_domain": False,
    #         "new_price": "",
    #         "renew_price": "",
    #         "restore_price": "",
    #         "domain_type": "",
    #         "price_type": "",
    #         "notice_info": "暂不支持该后缀"
    #     }
    # },
]

# 查看详情--成功
data_get_GetDomain_success = [
    {
        "comment": "获取域名详情",
        "sql": {
            "update": "",
            "select": "SELECT domain FROM domain_info WHERE account_id ='2100266070' AND supplier ='xinNet' AND dn_audit_status ='512' ORDER BY `id` DESC "
        },
        "params": {
            "domain": None
        },
        "code": 200
    }
]
"""结果校验："""
# data = data_get_GetDomain_success[0] # 这[0]是针对于列表中有多个字典时使用的
# select_sql = data["sql"]["select"]
# update_sql = data["sql"]["update"]
# select_result = domain_select_update(select_sql, update_sql)
# print(select_result)


# 查看详情--失败
data_get_GetDomain_error = [
    {
        "comment": "获取域名详情-失败--域名不在火山引擎",
        "params": {
            "domain": "taotest063qwq.cn"
        },
        "code": 200,
        "resp": {
            "Action": "GetDomain",
            "Version": "2022-12-12",
            "Service": "domain_openapi",
            "Region": "cn-north-1",
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    },
    {
        "comment": "获取域名详情-失败--域名不属于此账号",
        "params": {
            "domain": "tc-080.cn"
        },
        "code": 200,
        "resp": {
            "Action": "GetDomain",
            "Version": "2022-12-12",
            "Service": "domain_openapi",
            "Region": "cn-north-1",
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    }
]

# 查看列表
data_get_ListDomains = [
    {
        "comment": "获取域名列表",
        "params": {
            "page_number": 1,
            "page_size": 3
            # page_number    第几页的数据
            # page_size      每页展示多少条数据
        },
        "code": 200
    },
    {
        "comment": "查看单个域名",
        "params": {
            "domain": RenewDomain_domain()
        },
        "code": 200
    },
    {
        "comment": "已过期的域名",
        "params": {
            "status": "expired",
            # status：                域名状态（多个状态以逗号隔开）
            #     normal                  正常--参考命名审核通过的参数
            #     registrant_change       户中
            #     expired                 已过期
            #     redemption              赎回期
            #     wasted                  已废弃
            #     transfer_out            已转出
            #     redeeming               赎回中
            #     registrant_changing     持有人信息修改中
            "page_size": 3
        },
        "code": 200
    },
    {
        "comment": "实名中的域名",
        "params": {
            "verify_status": "pending_validation",
            # verify_status           实名状态（多个状态以逗号隔开）
            #     not_validation          未实名
            #     pending_validation      实名中
            #     verification_success    实名成功
            #     verification_failed     实名失败
            "page_size": 3
        },
        "code": 200
    },
    {
        "comment": "将在30天后过期的域名",
        "params": {
            "expired_after": 30,
            # expired_after         将在XX天后过期的域名
            # 直接填写过期天数
            "page_size": 3
        },
        "code": 200
    },
    {
        "comment": "已开启自动续费的域名",
        "params": {
            "is_auto_renew": True,
            # is_auto_renew           是否自动续费
            #     True                    是
            #     False                   否
            "page_size": 3
        },
        "code": 200
    },
    {
        "comment": "命名审核通过",
        "params": {
            "domain_name_audit_status": "audit_pass",
            # domain_name_audit_status  命名审核状态（多个状态以逗号隔开）
            #     auditing            命名审核中
            #     audit_pass          命名审核通过
            #     audit_unPass        命名审核未通过
            "page_size": 3
        },
        "code": 200
    },
    {
        "comment": "按最早过期时间排序",
        "params": {
            "order_by": "expired_time",
            # order_aby               按照注册时间的早/晚排序--需以下档的升序/降序联合使用
            #     register_time       注册时间
            #     expired_time        过期时间
            "asc_or_desc": "ASC",
            # asc_or_desc             升序/降序
            #     ASC                 升序
            #     DESC                降序
            "page_size": 3
        },
        "code": 200
    }

]

# 获取域名证书URL--成功
data_get_GetDomainCertificateUrl_success = [
    {
        "comment": "获取域名证书URL--成功",
        "params": {
            "domain": RenewDomain_domain()
        },
        "code": 200
    }
]

# 获取域名证书URL--失败
data_get_GetDomainCertificateUrl_error = [
    {
        "comment": "获取域名证书URL--失败：域名不存在",
        "params": {
            "domain": "taotest063qwq.cn"
        },
        "code": 200,
        "resp": {
            "RequestId": "2024031816382027ADC701F4E69C015233",
            "Action": "GetDomainCertificateUrl",
            "Version": "2022-12-12",
            "Service": "domain_openapi",
            "Region": "cn-north-1",
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    }
]

# 修改域名NS
data_post_ModifyDomainNS_success = [
    {
        "comment": "修改域名NS-2",
        "body": {
            "domain": RenewDomain_domain(),
            # NS列表，提供的NS必须已经在注册商注册过，最少2个，最大6个
            "ns_list": [
                "vip1.ali-gtm-pressure.com",
                "vip2.ali-gtm-pressure.com"
            ]
        },
        "code": 200
    },
    {
        "comment": "修改域名NS-3",
        "body": {
            "domain": RenewDomain_domain(),
            "ns_list": [
                "vip1.ali-gtm-pressure.com",
                "vip2.ali-gtm-pressure.com",
                "vip3.ali-gtm-pressure.com",
            ]
        },
        "code": 200
    },
    {
        "comment": "修改域名NS-6",
        "body": {
            "domain": RenewDomain_domain(),
            "ns_list": [
                "vip1.ali-gtm-pressure.com",
                "vip2.ali-gtm-pressure.com",
                "vip3.ali-gtm-pressure.com",
                "vip4.ali-gtm-pressure.com",
                "vip5.ali-gtm-pressure.com",
                "vip6.ali-gtm-pressure.com",
            ]
        },
        "code": 200
    }
]

# 修改域名NS--失败
data_post_ModifyDomainNS_error = [
    {
        "comment": "修改域名NS-1",
        "body": {
            "domain": RenewDomain_domain(),
            "ns_list": [
                "vip6.ali-gtm-pressure.com"
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 81818,
                "Message": "DNS服务器地址修改失败, 请检查ns数量([2-6])、ns是否有重复、是否是合法ns"
            }
        }
    },
    {
        "comment": "修改域名NS-7",
        "body": {
            "domain": RenewDomain_domain(),
            "ns_list": [
                "vip1.ali-gtm-pressure.com",
                "vip2.ali-gtm-pressure.com",
                "vip3.ali-gtm-pressure.com",
                "vip4.ali-gtm-pressure.com",
                "vip5.ali-gtm-pressure.com",
                "vip6.ali-gtm-pressure.com",
                "vip6.ali-gtm-pressure.com"
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 81818,
                "Message": "DNS服务器地址修改失败, 请检查ns数量([2-6])、ns是否有重复、是否是合法ns"
            }
        }
    },
    {
        "comment": "修改域名NS-错误域名",
        "body": {
            "domain": "domain",
            "ns_list": [
                "vip6.ali-gtm-pressure.com",
                "vip5.ali-gtm-pressure.com",
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    },
    {
        "comment": "修改域名NS-重复NS",
        "body": {
            "domain": RenewDomain_domain(),
            "ns_list": [
                "vip5.ali-gtm-pressure.com",
                "vip5.ali-gtm-pressure.com",
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 81818,
                "Message": "DNS服务器地址修改失败, 请检查ns数量([2-6])、ns是否有重复、是否是合法ns"
            }
        }
    }
]

# 开启/关闭域名自动续费功能-成功
data_post_SetDomainAutoRenew_success = [
    {
        # 开启/关闭自动续费功能成功的域名状态，就是找一个 过户中or命名审核失败的域名，都可以开启/关闭自动续费成功；相反，如若找一个已过期的就不可以了。
        # status
        #     normal                  正常--参考命名审核通过的参数
        #     registrant_change       过户中
        #     registrant_changing     持有人信息修改中
        # domain_name_audit_status  命名审核状态
        #     auditing            命名审核中
        #     audit_pass          命名审核通过
        #     audit_unPass        命名审核未通过
        # verify_status           实名状态
        #     pending_validation      实名中
        #     verification_success    实名成功
        #     verification_failed     实名失败
        "comment": "开启域名自动续费功能-成功",
        "domain_sql": "SELECT domain FROM domain_info WHERE account_id='2100266070' AND supplier = 'xinNet' AND is_auto_renew = '0' ORDER BY `id` DESC",
        "body": {
            "domain": None,
            "operation": "open"
        },
        "code": 200
    },
    {
        "comment": "关闭域名自动续费功能-成功",
        "domain_sql": "SELECT domain FROM domain_info WHERE account_id='2100266070' AND supplier = 'xinNet' AND is_auto_renew = '1' ORDER BY `id` DESC",
        "body": {
            "domain": None,
            "operation": "close"
        },
        "code": 200
    }

]

# 开启/关闭域名自动续费功能-失败
data_post_SetDomainAutoRenew_error = [
    {
        "comment": "开启域名自动续费-失败，域名不存在",
        "body": {
            "domain": "taotest0633.cn",
            "operation": "open"
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    },
    {
        "comment": "关闭域名自动续费功能-失败，域名不存在",
        "body": {
            "domain": "taotest0633.cn",
            "operation": "close"
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    },
    {
        # 开启/关闭自动续费功能失败的域名状态（PS：已开启，再次开启的不算哦）
        # status
        #     expired                 已过期
        #     redemption              赎回期
        #     wasted                  已废弃
        #     transfer_out            已转出
        #     redeeming               赎回中
        "comment": "开启/关闭失败，当前域名状态无法进行该操作",
        "body": {
            "domain": "auto-test8.cn",
            "operation": "open"
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81773,
                "Message": "【auto-test8.cn】当前域名状态无法进行该操作"
            }
        }
    }
]

# *****************---模板操作---*****************
# 获取模板列表
data_get_ListTemplates = [
    {
        "comment": "获取模板列表",
        "params": {
            "page_number": "1",
            "page_size": "3"
        },
        "code": 200
    },
    {
        "comment": "根据持有人名称(中文)，模糊搜索",
        "params": {
            "page_number": "1",
            "page_size": "3",
            # 根据名称模糊搜索
            "registrant_zh": "北"
        },
        "code": 200
    },
    {
        "comment": "搜索注册类型为个人的模板",
        "params": {
            "page_number": "1",
            "page_size": "3",
            # C:企业  P:个人
            "registration_type": "P"
        },
        "code": 200
    },
    {
        "comment": "根据模板tag来搜索",
        "params": {
            "page_number": "1",
            "page_size": "3",
            # tag：模板tag，获取列表可查看tag
            "tag": "tkQNs5Gkr3wPIlfLE8Qreg=="  # 上海源庄数码科技有限公司
        },
        "code": 200
    },
    {
        "comment": "查找实名失败的模板",
        "params": {
            "page_number": "1",
            "page_size": "3",
            # status                模板状态(多个状态可使用逗号隔开)
            # not_validation            未实名
            # pending_validation        实名中
            # verification_success      实名成功
            # verification_failed       实名失败

            "status": "verification_failed"
        },
        "code": 200
    },
]

# 获取模板详情
data_get_GetTemplate = [
    {
        "comment": "获取当前用户的模板详情--成功",
        "params": {
            "tag": "tkQNs5Gkr3wPIlfLE8Qreg=="  # 上海源庄数码科技有限公司
        },
        "code": 200,
        # 下方的Result是用例中断言所用的，但是一个正确的一个错误的，没法使用断言，索性就给注释掉了
        # "Result": {
        #     "status": "verification_failed",
        #     "status_notice": "id_code is invalid",
        #     "tag": "..Wjf..ycMH5E5zDSrcaO6rA==",
        #     "registration_type": "P",
        #     "country_code": "CN",
        #     "post_code": "236000",
        #     "email": "taogangming@bytedance.com",
        #     "registrant_fn": "Meng",
        #     "registrant_ln": "Ji",
        #     "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu",
        #     "city": "suzhoushi",
        #     "state": "anhuisheng",
        #     "registrant": "Ji Meng",
        #     "registrant_fn_zh": "梦",
        #     "registrant_ln_zh": "季",
        #     "address_zh": "安徽省宿州市埇桥区",
        #     "city_zh": "宿州市",
        #     "state_zh": "安徽省",
        #     "registrant_zh": "季梦",
        #     "tel_country_code": "86",
        #     "tel_area_code": "",
        #     "tel_number": "16655886267",
        #     "tel_extension": "",
        #     "id_type": "SFZ",
        #     "id_code": "3****************0",
        #     "created_at": 1709523121,
        #     "updated_at": 1709523367
        # }
    },
    {
        "comment": "获取非当前用户的模板--模板不存在",
        "params": {
            "tag": "..Wjf..ycMH5E5zDSrcaO6rA==1"
        },
        "code": 200,
        # resp：断言所用，暂时先不用了。
        # "resp": {
        #     "Error": {
        #         "Code": "NotFound",
        #         "CodeN": 81710,
        #         "Message": "模板不存在"
        #     }
        # }
    }
]

# 创建模板-成功
data_post_CreateTemplate_success = [
    {
        "comment": "创建模板-->个人",
        "body": {
            "registration_type": "P",  # P代表个人模板
            "post_code": "236000",  # 地方邮编
            "email": "taogangming@bytedance.com",  # 邮箱
            "registrant": "ZiDongHua GeRen",  # 英文 姓名
            "registrant_fn": "GeRen",  # 英文 名
            "registrant_ln": "ZiDongHua",  # 英文 姓
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu " + " " + lib.get_uuid(),  # 英文 地址
            "city": "suzhoushi",  # 英文城市
            "state": "anhuisheng",  # 英文 省份
            "registrant_zh": "自动化个人",  # 中文 姓名
            "registrant_fn_zh": "个人",  # 中文 名
            "registrant_ln_zh": "自动化",  # 中文 姓
            "address_zh": "安徽省宿州市埇桥区" + lib.get_uuid(),  # 中文 地址
            "city_zh": "宿州市",  # 中文 城市
            "state_zh": "安徽省",  # 中文 省份
            "tel_country_code": "86",  # 中国大陆的国际电话区号
            "tel_number": "2395103",  # 座机号+手机号
            "tel_area_code": "0557",  # 区号。注：如果上述为手机号，则不用填写区号。如果为座机号，则需要填写区号
            "tel_extension": "",  # 分机号
            "id_type": "SFZ",  # 证件号类型-这个就是身份证的意思，若是下面的营业执照则是 YYZZ
            "id_code": "341226199410282820",  # 证件号，若是下面的营业执照则需要填写正确的统一社会信用代码
            "id_img": image_file("p_dameng")  # base64编码解码
        },
        "code": 200
    },
    {
        "comment": "创建模板-->企业",
        "body": {
            "registration_type": "C",  # C代表企业模板
            "post_code": "723000",
            "email": "taogangming@bytedance.com",
            "registrant": "ZiDongHua QiYe",
            "registrant_fn": "QiYe",
            "registrant_ln": "ZiDongHua",
            "address": "Bei Jing Shi Bei Jing Shi 1 Hao" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "自动化企业",
            "registrant_fn_zh": "企业",
            "registrant_ln_zh": "自动化",
            "address_zh": "北京市北京市1号" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "YYZZ",
            "id_code": "92610729MA6YP7AN6E",
            "id_img": image_file("c_huoguodian")
        },
        "code": 200
    },
    {
        "comment": "中英文名称最小数--2位",
        "body": {
            "registration_type": "P",  # P代表个人模板
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "G R",
            "registrant_fn": "G",
            "registrant_ln": "R",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "个人",
            "registrant_fn_zh": "人",
            "registrant_ln_zh": "个",
            "address_zh": "安徽省宿州市埇桥区" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "中文名称最大数--64位",
        # 但是新网的不看中文名称，他们只认英文的。
        "body": {
            "registration_type": "P",  # P代表个人模板
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "G R",
            "registrant_fn": "G",
            "registrant_ln": "R",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            # 根据API文档要求可支持传入64个字，但是目前仅能输入23个字。---已提交bug
            "registrant_zh": "校验中文名称数最大支持64位字符最小支持M位字",
            "registrant_fn_zh": "最大支持64位字符最小支持2位字",
            "registrant_ln_zh": "自动化创建模板",
            "address_zh": "安徽省宿州市埇桥区" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282822",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "英文名称最大数--64位",
        "body": {
            "registration_type": "P",  # P代表个人模板
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            # PS：英文的，目前加上空格也才59位字符，所以可能最大支持数可能不对。
            "registrant": "Chuang Jian Mo Ban Zui Xiao Liang Wei Shu Zui Da Liu Shi 64",
            "registrant_fn": "Zui Xiao Liang Wei Shu Zui Da Liu Shi 64",
            "registrant_ln": "Chuang Jian Mo Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "创建模板校验英文名称",
            "registrant_fn_zh": "校验英文名称",
            "registrant_ln_zh": "创建模板",
            "address_zh": "安徽省宿州市埇桥区" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282823",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "中文地址--128位",
        # PS：中文地址，根据OpenAPI文档可支持传入的字符数为128位字符，目前也就传入64位，所以可能最大支持数可能不对。
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Chuang Jian Mo Ban Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_fn": "Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_ln": "Chuang Jian Mo Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "创建模板校验中文地址",
            "registrant_fn_zh": "校验中文地址",
            "registrant_ln_zh": "创建模板",
            # PS：中文地址，根据OpenAPI文档可支持传入的字符数为128位字符，目前也就传入64位，所以可能最大支持数可能不对。--已提交bug
            "address_zh": "中文地址限制字数为128但是实际只能传入64位中文地址限制字数为128但是实际只能传入64位中文地址限制字128" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282824",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "英文地址--128位",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Chuang Jian Mu Ban Jiao Yan Zhong WenDi Zhi",
            "registrant_fn": "Jiao Yan Zhong WenDi Zhi",
            "registrant_ln": "Chuang Jian Mu Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "创建模板校验中文地址",
            "registrant_fn_zh": "校验英文地址",
            "registrant_ln_zh": "创建模板",
            # 中文地址，根据OpenAPI文档可支持传入的字符数为128位字符，目前可以传入200位字符。--已提交bug
            "address_zh": "中文地址限制字数为128但是实际只能传入64位" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282825",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "中文省市地区校验",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Chuang Jian Mo Ban Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_fn": "Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_ln": "Chuang Jian Mo Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建模板中文省市地区校验",
            "registrant_fn_zh": "中文省市地区校验",
            "registrant_ln_zh": "自动化创建模板",
            "address_zh": "中文地址限制字数为128但是实际只能传入64位" + lib.get_uuid(),
            # 也就是这个省市地区下的市是属于这个省的。且省市名称一定要写完整，如：安徽省-宿州市
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282826",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "英文省市地区校验",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Chuang Jian Mo Ban Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_fn": "Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_ln": "Chuang Jian Mo Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            # 也就是这个省市地区下的市是属于这个省的。且省市名称一定要写完整，如：安徽省-宿州市
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建模板中文省市地区校验",
            "registrant_fn_zh": "英文省市地区校验",
            "registrant_ln_zh": "自动化创建模板",
            "address_zh": "中文地址限制字数为128但是实际只能传入64位" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0557",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282827",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "手机号校验",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Chuang Jian Mo Ban Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_fn": "Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_ln": "Chuang Jian Mo Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建模板中文省市地区校验",
            "registrant_fn_zh": "手机号校验",
            "registrant_ln_zh": "自动化创建模板",
            "address_zh": "中文地址限制字数为128但是实际只能传入64位" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282828",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
    {
        "comment": "区号+座机号校验",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Chuang Jian Mo Ban Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_fn": "Zui Xiao Liang Wei Shu Zui Da Liu Shi Si",
            "registrant_ln": "Chuang Jian Mo Ban",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 3" + lib.get_uuid(),
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建模板中文省市地区校验",
            "registrant_fn_zh": "手机号校验",
            "registrant_ln_zh": "自动化创建模板",
            "address_zh": "中文地址限制字数为128但是实际只能传入64位" + lib.get_uuid(),
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            # 如果是区号+座机号，则此处对应的是座机号，如果此处对应的是手机号，则就不需要填写区号
            "tel_number": "4295103",
            "tel_area_code": "0557",
            # # 区号需对应省市地区，如果上述对应的是手机号，则就不需要填写区号
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282829",
            "id_img": image_file("p_dameng")
        },
        "code": 200
    },
]

# print(data_post_CreateTemplate_success[0]["body"]["address"])

# 创建模板-失败
data_post_CreateTemplate_error = [
    {
        "comment": "创建失败，当前模板信息与其他模板相同",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282820",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81795,
                "Message": "当前模板信息与其他模板相同，建议修改/删减部分通讯地址文字重试"
            }
        }
    },
    {
        "comment": "创建失败，证件类型和持有者类型不匹配",
        "body": {
            # 证件类型：C 为企业类型，P 为个人
            "registration_type": "C",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Ji MengYi",
            "registrant_fn": "MengYi",
            "registrant_ln": "Ji",
            "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu",
            "city": "suzhoushi",
            "state": "anhuisheng",
            "registrant_zh": "季梦一",
            "registrant_fn_zh": "梦一",
            "registrant_ln_zh": "季",
            "address_zh": "安徽省宿州市埇桥区",
            "city_zh": "宿州市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_area_code": "",
            "tel_number": "16655886267",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282820",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81843,
                "Message": "证件类型和持有者类型不匹配"
            }
        }
    },
    {
        "comment": "创建失败-->模板类型为空",
        "body": {
            # 模板类型为空
            "registration_type": "",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282820",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->模板类型为小写c",
        "body": {
            "registration_type": "c",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "持有人类型不合法"
            }
        }
    },
    {
        "comment": "创建失败-->模板类型为小写p",
        "body": {
            "registration_type": "p",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "持有人类型不合法"
            }
        }
    },
    {
        "comment": "创建失败-->邮编为空",
        "body": {
            "registration_type": "P",
            "post_code": "",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->邮编少一位",
        "body": {
            "registration_type": "P",
            "post_code": "23600",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81840,
                "Message": "请输入正确的邮编"
            }
        }
    },
    {
        "comment": "创建失败-->邮编多一位",
        "body": {
            "registration_type": "P",
            "post_code": "2360001",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81840,
                "Message": "请输入正确的邮编"
            }
        }
    },
    {
        "comment": "创建失败-->邮箱为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->邮箱无后缀",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81805,
                "Message": "请输入正确的电子邮箱"
            }
        }
    },
    {
        "comment": "创建失败-->中文邮箱",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "中文@qq.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81805,
                "Message": "请输入正确的电子邮箱"
            }
        }
    },
    {
        "comment": "创建失败-->英文姓名、名、姓为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "",
            "registrant_fn": "",
            "registrant_ln": "",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->英文姓名、名、姓为纯数字",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "1234",
            "registrant_fn": "2234",
            "registrant_ln": "3234",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81711,
                "Message": "请检查填写英文信息是否准确(必须包含英文)"
            }
        }
    },
    # {
    #     "comment": "创建失败-->英文姓名小于2个字符",--已提交bug，还未修复，修复完成后再用起来
    #     "body": {
    #         "registration_type": "P",
    #         "post_code": "236000",
    #         "email": "taogangming@bytedance.com",
    #         "registrant": "q",
    #         "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
    #         "registrant_ln": "Zi Dong Hua Chuang Jian",
    #         "address": "An Hui Sheng He Fei Shi 1 Hao",
    #         "city": "hefeishi",
    #         "state": "anhuisheng",
    #         "registrant_zh": "自动化创建--有用勿删勿删勿删",
    #         "registrant_fn_zh": "--有用勿删勿删勿删",
    #         "registrant_ln_zh": "自动化创建",
    #         "address_zh": "安徽省合肥市1号",
    #         "city_zh": "合肥市",
    #         "state_zh": "安徽省",
    #         "tel_country_code": "86",
    #         "tel_number": "2395103",
    #         "tel_area_code": "0551",
    #         "tel_extension": "",
    #         "id_type": "SFZ",
    #         "id_code": "341226199410282821",
    #         "id_img": image_file("p_dameng")
    #     },
    #     "code": 200,
    #     "Resp": {
    #         "Error": {
    #             "Code": "",
    #             "CodeN": 81400,
    #             "Message": "请检查填写信息是否准确"
    #         }
    #     }
    # },
    {
        "comment": "创建失败-->英文地址为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->英文地址为纯数字",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "1234",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81711,
                "Message": "请检查填写英文信息是否准确(必须包含英文)"
            }
        }
    },
    {
        "comment": "创建失败-->英文城市、省份名均为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "",
            "state": "",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->英文城市、省份名均为纯数字",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "1234",
            "state": "1234",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81711,
                "Message": "请检查填写英文信息是否准确(必须包含英文)"
            }
        }
    },
    {
        "comment": "创建失败-->英文城市名称不完整",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefei",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81878,
                "Message": "所选地区识别异常"
            }
        }
    },
    {
        "comment": "创建失败-->英文城市名称与省份不符",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "nanjingshi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81878,
                "Message": "所选地区识别异常"
            }
        }
    },
    {
        "comment": "创建失败-->英文省份不完整",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhui",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81878,
                "Message": "所选地区识别异常"
            }
        }
    },
    {
        "comment": "创建失败-->中文名称、姓、名参数都为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "",
            "registrant_fn_zh": "",
            "registrant_ln_zh": "",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    # {
    #     "comment": "创建失败-->传入1个字",# 最低是两个字，但是1个字也可以，已提交bug，等修复完成后再启用，到时候最下边的Resp也要改一下
    #     "body": {
    #         "registration_type": "P",
    #         "post_code": "236000",
    #         "email": "taogangming@bytedance.com",
    #         "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
    #         "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
    #         "registrant_ln": "Zi Dong Hua Chuang Jian",
    #         "address": "An Hui Sheng He Fei Shi 1 Hao",
    #         "city": "hefeishi",
    #         "state": "anhuisheng",
    #         "registrant_zh": "自",
    #         "registrant_fn_zh": "--有用勿删勿删勿删",
    #         "registrant_ln_zh": "自动化创建",
    #         "address_zh": "安徽省合肥市1号",
    #         "city_zh": "合肥市",
    #         "state_zh": "安徽省",
    #         "tel_country_code": "86",
    #         "tel_number": "2395103",
    #         "tel_area_code": "0551",
    #         "tel_extension": "",
    #         "id_type": "SFZ",
    #         "id_code": "341226199410282821",
    #         "id_img": image_file("p_dameng")
    #     },
    #     "code": 200,
    #     "Resp": {
    #         "Error": {
    #             "Code": "BadRequest",
    #             "CodeN": 81878,
    #             "Message": "所选地区识别异常"
    #         }
    #     }
    # },
    {
        "comment": "创建失败-->中文地址为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    # {
    #     "comment": "创建失败-->中文地址输入大于128个字符",# 目前只能输入64个字符，已提交bug，等修复后再启用
    #     "body": {
    #         "registration_type": "P",
    #         "post_code": "236000",
    #         "email": "taogangming@bytedance.com",
    #         "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
    #         "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
    #         "registrant_ln": "Zi Dong Hua Chuang Jian",
    #         "address": "An Hui Sheng He Fei Shi 1 Hao",
    #         "city": "hefeishi",
    #         "state": "anhuisheng",
    #         "registrant_zh": "自动化创建--有用勿删勿删勿删",
    #         "registrant_fn_zh": "--有用勿删勿删勿删",
    #         "registrant_ln_zh": "自动化创建",
    #         "address_zh": "自动化创建模板最大支持128位字符最小支持1位字符qwq这里是129个字自动化创建模板最大支持128位字符最小支持1位字符qwq这里是129个字自动化创建模板最大支持128位字符最小支持1位字符qwq这里是129个字自动化创建模板最大支持128位字符最小支持1位字符qwq这里是12",
    #         "city_zh": "合肥市",
    #         "state_zh": "安徽省",
    #         "tel_country_code": "86",
    #         "tel_number": "2395103",
    #         "tel_area_code": "0551",
    #         "tel_extension": "",
    #         "id_type": "SFZ",
    #         "id_code": "341226199410282821",
    #         "id_img": image_file("p_dameng")
    #     },
    #     "code": 200,
    #     "Resp": {
    #         "Error": {
    #             "Code": "BadRequest",
    #             "CodeN": 81400,
    #             "Message": "请检查填写信息是否准确"
    #         }
    #     }
    # },
    {
        "comment": "创建失败-->中文城市、省份均为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "请检查填写信息是否准确"
            }
        }
    },
    {
        "comment": "创建失败-->中文城市名不完整",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81887,
                "Message": "创建模板所选地区中的中文城市不存在"
            }
        }
    },
    {
        "comment": "创建失败-->中文城市名与省份不符",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "南京市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81887,
                "Message": "创建模板所选地区中的中文城市不存在"
            }
        }
    },
    {
        "comment": "创建失败-->省份名不完整",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽",
            "tel_country_code": "86",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81886,
                "Message": "创建模板所选地区中的中文省份不存在"
            }
        }
    },
    {
        "comment": "创建失败-->country_code为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->country_code为错误的(香港)",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "85",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->country_code错误(澳门)",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "83",
            "tel_number": "2395103",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->电话号码为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为座机号码时，座机号小于7位数",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "239510",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为座机号码时，座机号大于8位数",  # 规定座机号为7-8位
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "239510311",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为手机号时，小于11位",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "1661234567",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为手机号时，大于11位",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "166123456789",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为座机号，但是区号为空时",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "4295103",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为手机号，但是区号不为空时",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "0551",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "请检查填写固话/手机号信息准确"
            }
        }
    },
    {
        "comment": "创建失败-->当电话号码为座机号时，且区号与地区不符",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "4295013",
            "tel_area_code": "0552",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81838,
                "Message": "填写的固定电话区号和选择地区不匹配，请修改成正确区号"
            }
        }
    },
    {
        "comment": "创建失败-->证件号类型化为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81841,
                "Message": "请输入正确的证件类型"
            }
        }
    },
    {
        "comment": "创建失败-->证件号类型与证件类型不符",  # 个人的传入营业执照的
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "YYZZ",
            "id_code": "341226199410282821",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81843,
                "Message": "证件类型和持有者类型不匹配"
            }
        }
    },
    {
        "comment": "创建失败-->证件号为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81796,
                "Message": "证件号码格式错误"
            }
        }
    },
    {
        "comment": "创建失败-->证件号少一位",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "34122619941028282",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81796,
                "Message": "证件号码格式错误"
            }
        }
    },
    {
        "comment": "创建失败-->证件号多一位",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "3412261994102828212",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81796,
                "Message": "证件号码格式错误"
            }
        }
    },
    {
        "comment": "创建失败-->身份证类型传入营业执照号码",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "92610729MA6YP7AN6E",
            "id_img": image_file("p_dameng")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81796,
                "Message": "证件号码格式错误"
            }
        }
    },
    {
        "comment": "创建失败-->图片错误、为空",
        "body": {
            "registration_type": "P",
            "post_code": "236000",
            "email": "taogangming@bytedance.com",
            "registrant": "Zi Dong Hua Chuang Jian -- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_fn": "-- You Yong Wu Shan Wu Shan Wu Shan",
            "registrant_ln": "Zi Dong Hua Chuang Jian",
            "address": "An Hui Sheng He Fei Shi 1 Hao",
            "city": "hefeishi",
            "state": "anhuisheng",
            "registrant_zh": "自动化创建--有用勿删勿删勿删",
            "registrant_fn_zh": "--有用勿删勿删勿删",
            "registrant_ln_zh": "自动化创建",
            "address_zh": "安徽省合肥市1号",
            "city_zh": "合肥市",
            "state_zh": "安徽省",
            "tel_country_code": "86",
            "tel_number": "16612345678",
            "tel_area_code": "",
            "tel_extension": "",
            "id_type": "SFZ",
            "id_code": "341226199410282821",
            "id_img": image_file("")
        },
        "code": 200,
        "Resp": {
            "Error": {
                "Code": "",
                "CodeN": 81792,
                "Message": "请检查上传文件格式或大小，非JPG或JPEG文件有被压缩可能，请调整大小后尝试提交"
            }
        }
    },
]

# 更新模板
# data_post_UpdateTemplate = [
#     {
#         # 暂时没法更新模板，显示网络异常，估计是XinWang那边的问题
#         # PS：执行这条Case的时候，建议diff以下模板的参数，或者重新填写一下参数，有可能之前的模板给删除了，导致更新失败
#         "comment": "更新模板信息",
#         "body": {
#             "tag": "we4hFUgw3Ki5mgjDz7r6QA==",
#             "post_code": "236000",
#             "email": "taogangming@bytedance.com",
#             "registrant_fn": "MengYao",
#             "registrant_ln": "Ji",
#             "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 1 Hao",
#             "city": "suzhoushi",
#             "state": "anhuisheng",
#             "registrant_fn_zh": "梦瑶",
#             "registrant_ln_zh": "季",
#             "address_zh": "安徽省宿州市埇桥区1号",
#             "city_zh": "宿州市",
#             "state_zh": "安徽省",
#             "tel_country_code": "86",
#             "tel_area_code": "",
#             "tel_number": "16655886267",
#             "tel_extension": ""
#         },
#         "code": 200
#     },
#     {
#         # 我想这应该也算是一条Case吧，没更改任何的信息，会不会显示更新失败呢，等到时候和供应商那边说一下这个问题后再进行尝试，如果没有提示错误，就把这条Case给删掉呗。
#         "comment": "模板更新失败，无信息变化",
#         "body": {
#             "tag": "we4hFUgw3Ki5mgjDz7r6QA==",
#             "post_code": "236000",
#             "email": "taogangming@bytedance.com",
#             "registrant_fn": "MengYao",
#             "registrant_ln": "Ji",
#             "address": "An Hui Sheng Su Zhou Shi Yong Qiao Qu 1 Hao",
#             "city": "suzhoushi",
#             "state": "anhuisheng",
#             "registrant_fn_zh": "梦瑶",
#             "registrant_ln_zh": "季",
#             "address_zh": "安徽省宿州市埇桥区1号",
#             "city_zh": "宿州市",
#             "state_zh": "安徽省",
#             "tel_country_code": "86",
#             "tel_area_code": "",
#             "tel_number": "16655886267",
#             "tel_extension": ""
#         },
#         "code": 200
#     }
# ]

# # 实名模板
# # 这个API暂时有些小问题，暂时先不使用了。
# data_post_ValidateTemplate = [
#     {
#         "comment": "实名模板",
#         "body": {
#             "tag": "..Wjf..ycMH5E5zDSrcaO6rA==",
#             "id_type": "SFZ",
#             "id_code": "341226199410282820",
#             "id_img":image_file("p_dameng")
#         }
#     }
# ]

# *****************---异步任务操作---*****************


# 域名异步注册--成功
data_post_RegisterDomain_success = [
    {
        "comment": "域名异步注册-->英文1年",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": ["ns1.volcdns.com", "ns2.volcdns.com"],
            "is_auto_renew": True,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "域名异步注册-->英文2年",
        "body": {
            "domain": "openapi1" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 2,
            "ns_list": ["ns1.volcdns.com", "ns2.volcdns.com"],
            "is_auto_renew": True,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "域名异步注册-->中文1年",
        "body": {
            "domain": "openapi中文" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": ["ns1.volcdns.com", "ns2.volcdns.com"],
            "is_auto_renew": True,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "域名异步注册-->中文10年",
        "body": {
            "domain": "openapi中文" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 10,
            "ns_list": ["ns1.volcdns.com", "ns2.volcdns.com"],
            "is_auto_renew": True,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "注册时间填写0年,默认注册为1年",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 0,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "NS等于2个，且开启自动续费功能",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": True,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "域名异步注册，且关闭自动续费功能",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".cn",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200
    },
    {
        "comment": "已被注册的域名(请求会成功，但是异步任务定时轮询会失败)",
        "body": {
            "domain": "baidu.com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200
    }
]

# 域名异步注册--失败
data_post_RegisterDomain_error = [
    {
        "comment": "错误的域名，无后缀",
        "body": {
            "domain": "openapi" + lib.get_uuid(),
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "【openapi009】域名格式错误"
            }
        }
    },
    {
        "comment": "域名为空",
        "body": {
            "domain": "",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 400,
        "ResponseMetadata": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81400,
                "Message": "错误请求,请检查参数等是否正确"
            }
        }
    },
    {
        "comment": "域名字符超过最长限制63为字符",
        "body": {
            "domain": "openapi1121a" + lib.get_uuid() + lib.get_uuid() + lib.get_uuid16() + ".com",  # lib.get.uuid()=8哥字符；  .uuid16()=36个字符
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "【openapi6d-c582-44e8-b7c0-39a88ef6069839a88ef6069801b3c09b9db0391.com】域名格式错误"
            }
        }
    },
    {
        "comment": "供应商不支持的后缀域名",
        "body": {
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，还一种可能是供应商支持这个后缀了，需更改成别的不支持的后缀
            "domain": "baidu.ai",
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81783,
                "Message": "暂不支持该后缀"
            }
        }
    },
    {
        "comment": "注册时间大于10年",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 11,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81744,
                "Message": "openapi009.cn域名有效期不能超过10年"
            }
        }
    },

    {
        "comment": "只有一个NS",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81819,
                "Message": "openapi009.comDNS服务器校验失败, 请检查ns数量([2-6])、ns是否有重复、是否是合法ns"
            }
        }
    },
    {
        "comment": "两个重复的NS",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns1.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81819,
                "Message": "openapi009.comDNS服务器校验失败, 请检查ns数量([2-6])、ns是否有重复、是否是合法ns"
            }
        }
    },
    {
        "comment": "注册时超过2个NS",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",  # 上海源庄数码科技有限公司
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com",
                "ns3.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81836,
                "Message": "域名注册时配置的NS个数不能超过2个"
            }
        }
    },
    {
        "comment": "错误的tag",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "v0xhX7gWU72g7nZfXMpBgQ1==",
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81710,
                "Message": "模板不存在"
            }
        }
    },
    {
        "comment": "非实名成功的模板",
        "body": {
            "domain": "openapi" + lib.get_uuid() + ".com",
            # PS：执行这条Case如果报错的话，可能是模板被删除了，需重新更新一下template_tag，或者是ns不能用了，或者重新更改参数。
            "template_tag": "50JcZq7wvvjFl6bUNnbeuA==",  # 自动化创建--有用勿删勿删勿删
            "period": 1,
            "ns_list": [
                "ns1.ali-gtm-pressure.com",
                "ns2.ali-gtm-pressure.com"
            ],
            "is_auto_renew": False,
            "package_id": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81794,
                "Message": "当前模板状态无法进行该操作"
            }
        }
    },
]

# 域名异步过户-->成功
data_post_Domain_RegistrantChange_success = [

    {
        # 下方有"相同异步任务正在执行中"的Case，所以先别运营后台先别执行这个域名的请求
        "comment": "异步过户成功，并关闭'60天内禁止该域名被转出'",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，建议以可变参数传入，也有可能是模板被删除了，导致找不到template_tag，或者重新更改参数。
            "domain": domain_one(),
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",
            "is_transfer_limited_opened": False
        },
        "code": 200
    },
    {
        # 下方有"相同异步任务正在执行中"的Case，所以先别运营后台先别执行这个域名的请求
        "comment": "异步过户成功，并关闭'60天内禁止该域名被转出'",
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，建议以可变参数传入，也有可能是模板被删除了，导致找不到template_tag，或者重新更改参数。
            "domain": RenewDomain_domain(),
            "template_tag": "d..wfvW455V0h8JCUbSwXAw==",
            "is_transfer_limited_opened": True
        },
        "code": 200
    }
]

# 域名过户-->失败
data_post_Domain_RegistrantChange_error = [
    {
        "comment": "已有相同的异步任务在进行-->过户失败",
        "sql": {

        },
        "body": {
            "domain": RenewDomain_domain(),
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81731,
                "Message": "已有相同的异步任务在进行"
            }
        }
    },
    {
        "comment": "域名处于过户中-->过户失败",
        "sql": {
            "select": "SELECT domain FROM domain_info WHERE status='2' AND account_id='2100266070' LIMIT 1",
            "update": "UPDATE domain_info SET status='2' WHERE account_id='2100266070' AND status='1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1"
        },
        "body": {
            "domain": None,
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81773,
                "Message": "当前域名状态无法进行该操作"
            }
        }
    },
    {
        "comment": "域名已过期-->过户失败",
        "sql": {

        },
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，建议以可变参数传入，也有可能是模板被删除了，导致找不到template_tag，或者重新更改参数。
            "domain": "auto-test11.cn",
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81773,
                "Message": "当前域名状态无法进行该操作"
            }
        }
    },
    {

        "comment": "域名错误-->过户失败",
        "sql": {

        },
        "body": {
            "domain": "taotest00000.cn",
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "域名不存在"
            }
        }
    },
    {
        "comment": "域名为空-->过户失败",
        "sql": {

        },
        "body": {
            "domain": " ",
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81797,
                "Message": "【 】域名格式错误"
            }
        }
    },
    {
        "comment": "域名开启了禁止更新锁-->过户失败",
        "sql": {

        },
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，建议以可变参数传入，也有可能是模板被删除了，导致找不到template_tag，或者重新更改参数。
            "domain": "auto-test14.cn",
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81761,
                "Message": "域名禁止更新锁开启，如需操作，请先关闭更新锁"
            }
        }
    },
    {
        "comment": "未完成实名认证-->过户失败",
        "sql": {

        },
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，建议以可变参数传入，也有可能是模板被删除了，导致找不到template_tag，或者重新更改参数。
            "domain": "auto-test6.cn",
            "template_tag": "d..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81756,
                "Message": "未完成实名认证、禁止更新锁开启、过户中、持有者信息修改中或已过期的域名不支持该操作"
            }
        }
    },
    {
        "comment": "模板不存在-->过户失败",
        "sql": {

        },
        "body": {
            # PS：此域名可能会被手动更改状态、删除等操作，建议以可变参数传入，也有可能是模板被删除了，导致找不到template_tag，或者重新更改参数。
            "domain": "taotest094.cn",
            "template_tag": "dd..wfvW455V0h8JCUbSwXAw=="
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81710,
                "Message": "模板不存在"
            }
        }
    }
]

# 查询异步任务--详情
data_get_GetAsyncTask = [
    {
        "comment": "获取异步任务详情",
        "params": {
            "task_no": domain_async_task()
        },
        "code": 200
    },
    {
        "comment": "task_no记录不存在，获取异步任务详情-失败",
        "params": {
            "task_no": "registrant-6568be3eb8ea3222"
        },
        "code": 200
    },
    {
        "comment": "task_no为空",
        "params": {
            "task_no": " "
        },
        "code": 200
    }
]

# 域名异步续费--成功
data_post_RenewDomain_success = [
    {
        "comment": "异步续费1年",
        "sql1": {
            "select": "SELECT domain FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01'  "
                      "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 0,1"
        },
        "sql2": {
            "select": "SELECT expired_time FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' "
                      "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 0,1"
        },
        "body": {

            "domain": None,
            "period": 1,
            "current_expired_time": None
        },
        "code": 200
    },
    {
        "comment": "异步续费0年-->默认为1年",
        "sql1": {
            "select": "SELECT domain FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01'  "
                      "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1,2"
        },
        "sql2": {
            "select": "SELECT expired_time FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' "
                      "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 1,2"
        },
        "body": {
            "domain": None,
            "period": 0,
            "current_expired_time": None
        },
        "code": 200
    },
    {
        "comment": "异步续费9年-->最大续费年限",
        "sql1": {
            "select": "SELECT domain FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01'  "
                      "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 2,3"
        },
        "sql2": {
            "select": "SELECT expired_time FROM domain_info WHERE account_id = '2100266070' AND expired_time < '2034-01-01' "
                      "AND status = '1' AND verify_status = '4' AND dn_audit_status = '512' LIMIT 2,3"
        },
        "body": {
            "domain": None,
            "period": 9,
            "current_expired_time": None
        },
        "code": 200
    },
]

# 域名异步续费--失败
data_post_RenewDomain_error = [
    {
        "comment": "域名错误",
        "body": {
            "domain": "qwq-test0021.top",
            "period": 1,
            "current_expired_time": 1743609600
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "NotFound",
                "CodeN": 81707,
                "Message": "【qwq-test0021.top】域名不存在"
            }
        }
    },
    {
        "comment": "续费年限超过域名规定有效期年限(10年)",
        "body": {
            # PS：domain、current_expired_time暂时是写死的，
            "domain": "openapi6f8b8be2.cn",
            "period": 1,
            "current_expired_time": 2031408000
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 81744,
                "Message": "【openapi6f8b8be2.cn】域名有效期不能超过10年"
            }
        }
    },
    {
        "comment": "到期时间错误",
        "body": {
            "domain": "openapi中文31dd1f73.cn",
            "period": 1,
            "current_expired_time": 1762876800
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "BadRequest",
                "CodeN": 81857,
                "Message": "【openapi中文31dd1f73.cn】请求的域名过期时间和火山域名过期时间不一致"
            }
        }
    }
]
