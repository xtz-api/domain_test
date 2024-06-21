"""
PS：名称是根据此文件+请求方法+action+成功/失败；
     如：data_Get_CheckFee_success：data->此文件是存放数据的；Get->这个api是Get的请求方式；CheckFee->接口url(action)；success/error->参数正确/错误的
"""
from util.lib import get_uuid16

"""创建需求"""
# 创建需求--成功
data_post_CreateReq_success = [
    {
        "comment": "创建商机-->云上园区注册",
        "body": {
            "Comment": "自动化创建-->云上园区注册",
            "OpportunityService": "CloudICRegistration",
            "Phone": "16655886267",
            "Province": "江苏省"
            # 省市地区可随意修改，如：江苏省、上海市、新疆维吾尔自治区等等
        },
        "code": 200
    },
    {
        "comment": "创建商机-->本地注册",
        "body": {
            "Comment": "自动化创建-->本地注册",
            "OpportunityService": "LocalICRegistration",
            "Phone": "16655886267",
            "Province": "浙江省"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->抖音企业号认证指导",
        "body": {
            "Comment": "自动化创建-->抖音企业号认证指导",
            "OpportunityService": "EnterpriseAccountCertificationGuide",
            "Phone": "16655886267",
            "Province": "上海市"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->工商咨询助理(企业号专属)",
        "body": {
            "Comment": "自动化创建-->企业号专属",
            "OpportunityService": "EnterpriseICConsultingAssistant",
            "Phone": "16655886267",
            "Province": "广西壮族自治区"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->税务报道",
        "body": {
            "Comment": "自动化创建-->税务报道",
            "OpportunityService": "TaxReporting",
            "Phone": "16655886267",
            "Province": "广东省"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->银行开户",
        "body": {
            "Comment": "自动化创建-->银行开户",
            "OpportunityService": "OpenBank",
            "Phone": "16655886267",
            "Province": "山东省"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->资质服务（增值电信业务许可证）",
        "body": {
            "Comment": "自动化创建-->资质服务（增值电信业务许可证）",
            "OpportunityService": "ZZDX",
            "Phone": "16655886267",
            "Province": "西藏自治区"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->资质服务（食品餐饮业务许可证）",
        "body": {
            "Comment": "自动化创建-->资质服务（食品餐饮业务许可证）",
            "OpportunityService": "SPCY",
            "Phone": "16655886267",
            "Province": "新疆维吾尔自治区"
        },
        "code": 200
    },
    {
        "comment": "创建商机-->资质服务（广播/文化/出版类许可证）",
        "body": {
            "Comment": "自动化创建-->资质服务（广播/文化/出版类许可证）",
            "OpportunityService": "WHCB",
            "Phone": "16655886267",
            "Province": "宁夏回族自治区"
        },
        "code": 200
    }

]
# 创建需求--失败
str1 = "默认上限是200个字符，这是201个字符，" + get_uuid16() + get_uuid16() + get_uuid16() + get_uuid16() + get_uuid16()
print(str1)
data_post_CreateReq_error = [
    {
        "comment": "商机中已存在沟通中的免费抖音企业号",
        "body": {
            "Comment": "",
            "OpportunityService": "EnterpriseAccountCertificationGuide",
            "Phone": "16655886267",
            "Province": "北京市",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20639,
                "Message": "当前创建的免费抖音企业号/抖店咨询单总数已超出账号最多1条限制，若有额外需求请提交工单联系人工处理。"
            }
        }
    },
    {
        "comment": "创建不支持的省市地区--台湾省",
        "body": {
            "Comment": "",
            "OpportunityService": "CloudICRegistration",
            "Phone": "16655886267",
            "Province": "台湾省",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Province不合法"
            }
        }
    },
    {
        "comment": "创建不支持的省市地区--香港特别行政区",
        "body": {
            "Comment": "",
            "OpportunityService": "LocalICRegistration",
            "Phone": "16655886267",
            "Province": "香港特别行政区",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Province不合法"
            }
        }
    },
    {
        "comment": "创建不支持的省市地区--澳门特别行政区",
        "body": {
            "Comment": "",
            "OpportunityService": "CloudICRegistration",
            "Phone": "16655886267",
            "Province": "澳门特别行政区",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Province不合法"
            }
        }
    },
    {
        "comment": "备注信息超过最大限制200",
        "body": {
            "Comment": str1,
            "OpportunityService": "ZZDX",
            "Phone": "16655886267",
            "Province": "北京市",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Comment最大长度200个字符"
            }
        }
    },
    {
        "comment": "手机号大于11位",
        "body": {
            "Comment": "",
            "OpportunityService": "CloudICRegistration",
            "Phone": "166558862678",
            "Province": "北京市",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "手机号小于10位",
        "body": {
            "Comment": "",
            "OpportunityService": "CloudICRegistration",
            "Phone": "1665588626",
            "Province": "北京市",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "手机号号段错误-110",
        "body": {
            "Comment": "",
            "OpportunityService": "CloudICRegistration",
            "Phone": "11015588626",
            "Province": "北京市",
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    }
]

"""获取列表"""
# 获取需求列表
data_get_ListReq = [
    {
        "comment": "获取第1页的3条数据",
        "sql": {
        },
        "params": {
            "PageNumber": 1,
            "PageSize": 3
        },
        "code": 200
    },
    {
        "comment": "查看单个需求详情",
        "sql": {
            "update": "",
            "select": "SELECT req_id FROM ic_req WHERE account_id = '2100266070' ORDER BY `id` DESC LIMIT 1"
        },
        "params": {

            "OpportunityID": None
        },
        "code": 200
    },
    {
        "comment": "状态选择：待下单",
        "sql": {
        },
        "params": {

            "Status": "WaitCommunication",
            # 支持选择多个状态，多个状态使用逗号隔开
            # status                状态
            # WaitCommunication     待沟通
            # InCommunication       沟通中
            # WaitPlaceOrder        待下单
            # Completed             已完成
            # Closed                已关闭
            # Rejected              已拒单
            "PageSize": 3
        },
        "code": 200
    },
    {
        "comment": "服务选择：云上园区注册",
        "sql": {
        },
        "params": {
            "OpportunityService": "CloudICRegistration",
            #   OpportunityID                           服务
            #   CloudICRegistration                     云上园区注册（可提供地址）
            #   LocalICRegistration                     本地公司注册（需自备地址）
            #   EnterpriseAccountCertificationGuide     抖音企业号认证指导
            #   EnterpriseBlueVCertificationGuide       企业号蓝V认证指导
            #   DouDianSettlementGuide                  抖店入驻指导
            #   TaxReporting                            税务报道
            #   OpenBank                                银行开户
            #   EnterpriseICConsultingAssistant         工商咨询助理（企业号专属）
            #   ZZDX                                    增值电信（资质服务）
            #   SPCY                                    食品餐饮（资质服务）
            #   WHCB                                    文化出版（资质服务）
            "PageSize": 3
        },
        "code": 200
    },
    {
        "comment": "根据创建时间筛选",
        "sql": {
        },
        "params": {
            "PageSize": 3,
            "CreateTime": "2024-05-25 00:00:00"
            #   过滤等于大于某个创建时间的数据，由于数据过多，所以加了个PageNumber，仅需获取是3条数据
        },
        "code": 200
    },
    {
        "comment": "根据更新时间筛选",
        "sql": {
        },
        "params": {
            "PageSize": 3,
            "UpdateTime": "2024-05-22 00:00:00"
            #   过滤等于大于某个创建时间的数据，由于数据过多，所以加了个PageNumber，仅需获取是3条数据
        },
        "code": 200
    },

]

"""获取详情"""
# 获取需求单详情
data_get_getReq = [
    {
        "comment": "获取需求单详情-->成功",
        "params": {
            "OpportunityID": None
        },
        "code": 200
    },
    {
        "comment": "获取需求单详情失败-->该条商机不属于当前登录账号",
        "params": {
            "OpportunityID": "17830958316774400"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20632,
                "Message": "该条商机不属于当前登录账号，请重新确认火山账号并切换登录"
            }
        }
    },
    {
        "comment": "获取需求单详情失败-->参数为空",
        "params": {
            "OpportunityID": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "ReqID不能为空"
            }
        }
    }
]

"""关闭需求"""
# # 关闭需求单-->成功
# data_post_closeReq_success = [
#     {
#         "comment": "关闭-->免费抖音企业号订单",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id=2100266070 AND req_service='EnterpriseAccountCertificationGuide' ",
#         "body": {
#             "OpportunityID": ""
#         },
#         "code": 200
#     },
#     {
#         "comment": "关闭-->待沟通，且为免费抖音企业号的订单",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id=2100266070 AND status='WaitCommunication' AND req_service!='EnterpriseAccountCertificationGuide' ORDER BY req_id DESC LIMIT 1",
#         "body": {
#             "OpportunityID": None
#         },
#         "code": 200
#     }
# ]
#
# # 关闭需求单-->失败
# data_post_closeReq_error = [
#     {
#         "comment": "关闭失败-->订单重复关闭",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id=2100000056 AND status='Closed' ORDER BY id DESC LIMIT 1",
#         "body": {
#             "OpportunityID": ""
#         },
#         "code": 200,
#         "ResponseMetadata": {
#             "Error": {
#                 "Code": "",
#                 "CodeN": 20413,
#                 "Message": "当前状态无法被流转到期望状态"
#             }
#         }
#     },
#     {
#         "comment": "关闭失败-->非本账号的商机ID",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id !=2100000056 AND status='Closed' ORDER BY req_id DESC LIMIT 1",
#
#         "body": {
#             "OpportunityID": "17834013078150144"
#         },
#         "code": 200,
#         "ResponseMetadata": {
#             "Error": {
#                 "Code": "",
#                 "CodeN": 20632,
#                 "Message": "该条商机不属于当前登录账号，请重新确认火山账号并切换登录"
#             }
#         }
#     },
#     {
#         "comment": "关闭失败-->已完成",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id=2100000056 AND status='Completed' ORDER BY req_id DESC LIMIT 1",
#         "body": {
#             "OpportunityID": ""
#         },
#         "code": 200,
#         "ResponseMetadata": {
#             "Error": {
#                 "Code": "",
#                 "CodeN": 20413,
#                 "Message": "当前状态无法被流转到期望状态"
#             }
#         }
#     },
#     {
#         "comment": "关闭失败-->已关闭",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id=2100000056 AND status='Closed' ORDER BY req_id DESC LIMIT 1",
#         "body": {
#             "OpportunityID": ""
#         },
#         "code": 200,
#         "ResponseMetadata": {
#             "Error": {
#                 "Code": "",
#                 "CodeN": 20413,
#                 "Message": "当前状态无法被流转到期望状态"
#             }
#         }
#     },
#     {
#         "comment": "关闭失败-->已拒单",
#         "opportunityID_sql": "SELECT req_id FROM ic_req WHERE account_id=2100000056 AND status='Rejected' ORDER BY req_id DESC LIMIT 1",
#         "body": {
#             "OpportunityID": ""
#         },
#         "code": 200,
#         "ResponseMetadata": {
#             "Error": {
#                 "Code": "",
#                 "CodeN": 20413,
#                 "Message": "当前状态无法被流转到期望状态"
#             }
#         }
#     },
#     # {
#     #     "comment": "参数为空",  # 这个Case没毛病，但就是使用参数为空的使用sql无法使用下标去过滤，导致一直报错，故为了其他Case的准确性，就先不加这条Case了。
#     #     # "opportunityID_sql": "SELECT req_id FROM ic_req WHERE 1=0",
#     #     "opportunityID_sql": "update ic_req set req_id ='' where account_id=2100000056 ORDER BY req_id DESC",
#     #     "body": {
#     #         "OpportunityID": ""
#     #     },
#     #     "code": 200,
#     #     "ResponseMetadata": {
#     #         "Error": {
#     #             "Code": "",
#     #             "CodeN": 20400,
#     #             "Message": "OpportunityID不能为空"
#     #         }
#     #     }
#     # }
# ]

"""创建预配置工商火山订单"""
# 创建预配置工商火山订单-->成功
data_post_CreatePreOrder_success = [
    {
        "comment": "创建-->1个、云上、公司、订单",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            # PS：这个OpportunityID 本来准备想去查找数据库的形式去参数化传入，但是数据库中的需求类型不一定就是支付时的需求类型（比如：订单的数据类型是工商咨询，但是用户和供应商聊着聊着就可能要企业服务了。
            # 然后供应商流转的可能是企业服务，但是数据库内还是工商咨询，所以这个就对不上。后续有时间再看看这个问题）
            # "OpportunityID": "SELECT req_id FROM ic_req WHERE account_id=2100000056 AND status='WaitPlaceOrder' AND req_service='CloudICRegistration' ORDER BY id AESC LIMIT 1",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200
    },
    {
        "comment": "创建-->20个订单",
        "body": {
            "BuyCount": 20,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            # PS：问题同上，OpportunityID参数化形式传入
            "Price": 13600,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200
    },
    {
        "comment": "创建-->本地订单",
        "body": {
            "BuyCount": 1,
            "City": "杭州市",
            # 省市地区目前仅支持可支付的地区，详情可参照：test_cases-->constant.py
            "Class": "DomesticLimitedSmall",
            # DomesticLimitedSmall--内资有限公司（小规模）
            # DomesticLimitedTaxpayer--内资有限公司（一般纳税人）
            # SelfEmployed--工商个体户
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808609584541696",
            # PS：问题同上，OpportunityID参数化形式传入
            "Price": 750,
            "Product": "Local",
            "Province": "浙江省",
            "Service": "ICRegistration"
        },
        "code": 200
    },
    {
        "comment": "创建-->个体户订单",
        "body": {
            "BuyCount": 1,
            "City": "徐州市",
            "Class": "SelfEmployed",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800809564053811200",
            # PS：问题同上，OpportunityID参数化形式传入
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200
    },
    {
        "comment": "创建-->银行开户订单",
        "body": {
            "BuyCount": 1,
            "City": "青岛市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800812767909863424",
            # PS：问题同上，OpportunityID参数化形式传入
            "Price": 750,
            "Product": "Cloud",
            "Province": "山东省",
            "Service": "OpenBank"
        },
        "code": 200
    },
    {
        "comment": "创建-->将云上订单创建为本地的订单",
        "body": {
            "BuyCount": 1,
            "City": "苏州市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800809555222454272",
            "Price": 750,
            "Product": "Local",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200
    },
    {
        "comment": "创建-->将云上订单创建为银行开户",
        "body": {
            "BuyCount": 1,
            "City": "苏州市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800809555222454272",
            "Price": 750,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "OpenBank"
        },
        "code": 200
    },
    {
        "comment": "创建-->将云上订单创建为抖音企业号认证指导",
        "body": {
            "BuyCount": 1,
            "City": "苏州市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800809555222454272",
            "Price": 1,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "EnterpriseAccountCertificationGuide"
        },
        "code": 200
    },
]

# 创建预配置工商火山订单-->失败
data_post_CreatePreOrder_error = [
    {
        "comment": "创建-->订单个数为0",
        "body": {
            "BuyCount": 0,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 0,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "BuyCount不能为0"
            }
        }
    },
    {
        "comment": "创建-->订单个数为21",
        "body": {
            "BuyCount": 21,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 14280,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20626,
                "Message": "超过最大购买数量"
            }
        }
    },
    {
        "comment": "创建-->订单个数为0",
        "body": {
            "BuyCount": "",
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 0,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "请检查参数是否准确"
            }
        }
    },
    {
        "comment": "创建-->省份与城市不符",
        "body": {
            "BuyCount": 1,
            "City": "合肥市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "City不合法"
            }
        }
    },
    {
        "comment": "创建-->城市名称不完整",
        "body": {
            "BuyCount": 1,
            "City": "南京",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "City不合法"
            }
        }
    },
    {
        "comment": "创建-->城市为空",
        "body": {
            "BuyCount": 1,
            "City": "",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "City不能为空"
            }
        }
    },
    {
        "comment": "创建-->不在售卖范围内的省市地区",
        "body": {
            "BuyCount": 1,
            "City": "盐城市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20627,
                "Message": "选择的省份/城市不在售卖范围"
            }
        }
    },
    {
        "comment": "创建-->注册类型为空",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Class值不合法"
            }
        }
    },
    {
        "comment": "创建-->手机号为空",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": ""
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Phone值不合法"
            }
        }
    },
    {
        "comment": "创建-->错误的手机号号段",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "11055886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Phone值不合法"
            }
        }
    },
    {
        "comment": "创建-->手机号少一位",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "1665588626"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Phone值不合法"
            }
        }
    },
    {
        "comment": "创建-->手机号多一位",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "166558862671"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Phone值不合法"
            }
        }
    },
    {
        "comment": "创建-->错误的OpportunityID",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "180080860482637004",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20632,
                "Message": "该条商机不属于当前登录账号，请重新确认火山账号并切换登录"
            }
        }
    },
    {
        "comment": "创建-->价格为空",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "",
            "Price": "",
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "请检查参数是否准确"
            }
        }
    },
    {
        "comment": "创建-->价格与订单、购买数量不匹配",
        "body": {
            "BuyCount": 2,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 68,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 60005,
                "Message": "价格变动，请刷新后重试 [1360]"
            }
        }
    },
    {
        "comment": "创建-->需求类型为空",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Product值不合法"
            }
        }
    },
    {
        "comment": "创建-->省份为空",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Province不能为空"
            }
        }
    },
    {
        "comment": "创建-->省份名称不完整",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Province不合法"
            }
        }
    },
    {
        "comment": "创建-->不支持售卖的省市地区",
        "body": {
            "BuyCount": 1,
            "City": "天水市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "甘肃省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20627,
                "Message": "选择的省份/城市不在售卖范围"
            }
        }
    },
    {
        "comment": "创建-->服务内容为空",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": ""
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "Service值不合法"
            }
        }
    },
    {
        "comment": "创建-->服务内容为税务报道",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "TaxReporting"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20629,
                "Message": "税务报道不支持单独下单购买"
            }
        }
    },
    {
        "comment": "创建-->本地园区的不支持个体工商户的下单",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "SelfEmployed",
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "OpportunityID": "1800808604826370048",
            "Price": 750,
            "Product": "Local",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20627,
                "Message": "选择的省份/城市不在售卖范围"
            }
        }
    },
]

"""创建预配置资质火山订单"""
# 创建预配置资质火山订单-->成功
data_post_CreateQualificationOrder_success = [
    {
        "comment": "创建-->1个EDI经营许可证",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "EDI",
            "OpportunityID": "1800812772876304384",
            "OrderType": "New",
            "Price": 6250,
            "Province": "上海市"
        },
        "code": 200
    },
    {
        "comment": "创建-->1个食品经营许可证（餐饮业）",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "FBL_CI",
            "OpportunityID": "1800812776890671104",
            "OrderType": "New",
            "Price": 3800,
            "Province": "河南省"
        },
        "code": 200
    },
    {
        "comment": "创建-->1个网络文化经营许可证（动漫、音乐类）",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "NCBL_AM",
            "OpportunityID": "1800812781108649984",
            "OrderType": "New",
            "Price": 12000,
            "Province": "四川省"
        },
        "code": 200
    },
    {
        "comment": "创建-->20个食品经营许可证（餐饮业）",
        "body": {
            "BuyCount": 20,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "FBL_CI",
            "OpportunityID": "1800812776890671104",
            "OrderType": "New",
            "Price": 76000,
            "Province": "河南省"
        },
        "code": 200
    },
    {
        "comment": "创建-->EDI经营许可证的订单创建为-食品经营许可证（预包装，含冷冻冷藏备案）",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "FBL_PP_ICF",
            "OpportunityID": "1800812772876304384",
            "OrderType": "New",
            "Price": 1680,
            "Province": "上海市"
        },
        "code": 200
    },
    {
        "comment": "创建-->EDI经营许可证的订单创建为-广播电视节目制作许可证",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "RTPPL",
            "OpportunityID": "1800812772876304384",
            "OrderType": "New",
            "Price": 2680,
            "Province": "上海市"
        },
        "code": 200
    },
]

# 创建预配置资质火山订单-->失败
data_post_CreateQualificationOrder_error = [
    {
        "comment": "创建-->资质类型为空",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "",
            "OpportunityID": "1800812781108649984",
            "OrderType": "New",
            "Price": 2680,
            "Province": "上海市"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "License值不合法"
            }
        }
    },
    {
        "comment": "创建-->订单类型为空",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "RTPPL",
            "OpportunityID": "1800812781108649984",
            "OrderType": "",
            "Price": 2680,
            "Province": "上海市"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "OrderType值不合法"
            }
        }
    },
    {
        "comment": "创建-->资质类型与价格不符",
        "body": {
            "BuyCount": 1,
            "ContactInfo": {
                "Phone": "16655886267"
            },
            "License": "PBL_RW",
            "OpportunityID": "1800812772876304384",
            "OrderType": "New",
            "Price": 2680,
            "Province": "上海市"
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 60005,
                "Message": "价格变动，请刷新后重试 [4280]"
            }
        }
    }
]
