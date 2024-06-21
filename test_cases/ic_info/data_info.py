# 创建预配置火山订单--
data_post_CreatePreOrder = [
    {
        "comment": "创建-->工商公司订单（在商机处已经校验过了这里的参数，包括错误的）",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "DomesticLimitedSmall",
            "ContactInfo": {
                "Phone": "16612345678"
            },
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "Result": {
            "OrderID": "BO7368819908162502700"
        }
    },
    {
        "comment": "创建-->工商个体户订单",
        "body": {
            "BuyCount": 1,
            "City": "南京市",
            "Class": "SelfEmployed",
            "ContactInfo": {
                "Phone": "16612345678"
            },
            "Price": 680,
            "Product": "Cloud",
            "Province": "江苏省",
            "Service": "ICRegistration"
        },
        "code": 200,
        "Result": {
            "OrderID": "BO7368819908162502700"
        }
    },
]

"""暂存注册资料"""
# 暂存注册资料--成功
data_post_SaveICRegMaterial_succes = [
    {
        "comment": "公司-->暂存注册资料，传入必填字段",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200
    },
    {
        "comment": "公司-->暂存注册资料，传入必填字段+非必填字段（备选名称、注册资本实缴日期、经营范围、收件人、收件人手机号、收件地址、股东注册资本实缴日期、公司主要人员财务-总经理-执行董事）",
        "body": {
            "ICID": "1801158456596918272",
            "BasicInfo": {
                "Name": "天津地义借钱不还没能力有限公司",
                "BackupNames": ["天津", "地义", "借钱", "不还"],
                "CapitalAmount": 100000000,
                "CapitalDate": "2026-06-06",
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "文艺创作；广告制作；广告设计、代理；广告发布；数字内容制作服务（不含出版物发行）；专业设计服务；摄影扩印服务；图文设计制作；摄像及视屏制作服务；动漫游戏开发；平面设计；数字文化创意内容应用服务；咨询策划服务；市场营销策划；会议及展览服务；企业形象策划；个人商务服务；信息咨询服务（不含许可类信息咨询服务）；个人互联网直播服务；其他文化艺术经纪代理；信息咨询服务（不含许可类信息咨询服务）；信息技术咨询服务",
                "RecipientInfo": {
                    "Phone": "16612345678",
                    "Address": "嘿嘿家的哈哈来收",
                    "Name": "嘿嘿"
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%",
                        "CapitalDate": "2024-06-13"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%",
                        "CapitalDate": "2024-06-13"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                },
                {
                    "TemplateID": "1801227218369683456",
                    "TemplateInfo": {
                        "TemplateID": "1801227218369683456",
                        "TemplateType": "Natural",
                        "Name": "长安",
                        "LicenseType": "ID",
                        "LicenseFront": "1801227098093465600",
                        "LicenseBack": "1801227085722148864",
                        "LicenseNum": "342116199410280003",
                        "LicenseAddr": "安徽省合肥市1号",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Accountant",
                        "GeneralManager",
                        "ExecutiveDirector"
                    ]
                }
            ]
        },
        "code": 200
    },
    {
        "comment": "公司-->暂存注册资料，最小传入校验（公司名称2个字、注册资金1元、注册年限5年）",
        "body": {
            "ICID": "1801158456595709952",
            "BasicInfo": {
                "Name": "公司",
                "BackupNames": [],
                "CapitalAmount": 1,
                "CapitalDate": "",
                "OperationYear": "5",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "100.00%",
                        "CapitalDate": ""
                    },
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200
    },
    {
        "comment": "公司-->暂存注册资料，最大传入校验（公司名称50个字、注册资金1亿元、注册年限999年）",
        "body": {
            "ICID": "1801158456597401600",
            "BasicInfo": {
                "Name": "西藏东藏找不到有限责任公司西藏东藏找不到有限责任公司西藏东藏找不到有限责任公司西藏东藏找不到有限责任",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 100000000,
                        "CapitalRatio": "100.00%"
                    },
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200
    },
    {
        "comment": "公司-->暂存注册资料，股东类型选择法人（上面的已经选择了自然人了）",
        "body": {
            "ICID": "1801158456598368256",
            "BasicInfo": {
                "Name": "宁波打的电话已关机械有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Legal",
                "Shareholders": [
                    {
                        "TemplateID": "1801086376748081152",
                        "TemplateInfo": {
                            "TemplateID": "1801086376748081152",
                            "TemplateType": "Legal",
                            "Name": "留坝县辣火老灶火锅店",
                            "LicenseType": "License",
                            "LicenseFront": "1801086080354463744",
                            "LicenseNum": "92610729MA6YP7AN6E",
                            "LicenseAddr": "陕西省汉中市留坝县江口镇江口村三组",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com",
                            "LegalRepresentative": {
                                "Name": "刘康康",
                                "LicenseType": "ID",
                                "LicenseNum": "342201199410280002",
                                "LicenseFront": "1801086117803282432",
                                "LicenseBack": "1801086103253098496",
                                "LicenseAddr": "安徽省安徽省宿州市"
                            }
                        },
                        "TemplateType": "Legal",
                        "CapitalAmount": 100000000,
                        "CapitalRatio": "100.00%",
                        "CapitalDate": ""
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200
    },
    {
        "comment": "公司-->暂存注册资料，股东类型选择-自然人+法人",
        "body": {
            "ICID": "1801158456598171648",
            "BasicInfo": {
                "Name": "义务不扫何以扫天下清洁能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "NaturalAndLegal",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%",
                        "CapitalDate": ""
                    },
                    {
                        "TemplateID": "1801086376748081152",
                        "TemplateInfo": {
                            "TemplateID": "1801086376748081152",
                            "TemplateType": "Legal",
                            "Name": "留坝县辣火老灶火锅店",
                            "LicenseType": "License",
                            "LicenseFront": "1801086080354463744",
                            "LicenseNum": "92610729MA6YP7AN6E",
                            "LicenseAddr": "陕西省汉中市留坝县江口镇江口村三组",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com",
                            "LegalRepresentative": {
                                "Name": "刘康康",
                                "LicenseType": "ID",
                                "LicenseNum": "342201199410280002",
                                "LicenseFront": "1801086117803282432",
                                "LicenseBack": "1801086103253098496",
                                "LicenseAddr": "安徽省安徽省宿州市"
                            }
                        },
                        "TemplateType": "Legal",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%",
                        "CapitalDate": ""
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200
    },
    {
        "comment": "个体户-->暂存注册资料，传入必填字段",
        "body": {
            "ICID": "1801085254920798208",
            "BasicInfo": {
                "Name": "新乡事成但我懒得想智力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "CultureMedia",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "OperatorInfo": {
                "TemplateID": "1801085999194578944",
                "TemplateInfo": {
                    "TemplateID": "1801085999194578944",
                    "TemplateType": "Natural",
                    "Name": "故里",
                    "LicenseType": "ID",
                    "LicenseFront": "1801085783949557760",
                    "LicenseBack": "1801085766993141760",
                    "LicenseNum": "342201199410280001",
                    "LicenseAddr": "安徽省安徽省安徽省",
                    "Phone": "16655886267",
                    "Email": "qq@qq.com"
                }
            }
        },
        "code": 200
    },
    {
        "comment": "个体户-->暂存注册资料，传入必填字段+非必填字段",
        "body": {
            "ICID": "1801085254920798208",
            "BasicInfo": {
                "Name": "新乡事成但我懒得想智力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "CapitalDate": "2026-06-06",
                "OperationYear": "999",
                "Industry": "CultureMedia",
                "Scope": "动画片、专题片、电视综艺；不得制作时政新闻及同类专题、专栏等广播电视节目（广播电视节目制作经营许可证：有效期至2014年9月29日）。设计、制作、代理、发布广告；组织文化艺术交流活动（不含演出）；展览服务；企业策划；电脑图文设计；广告信息咨询",
                "RecipientInfo": {
                    "Phone": "16612345678",
                    "Address": "哈哈家的嘿嘿来收",
                    "Name": "哈哈"
                }
            },
            "OperatorInfo": {
                "TemplateID": "1801085999194578944",
                "TemplateInfo": {
                    "TemplateID": "1801085999194578944",
                    "TemplateType": "Natural",
                    "Name": "故里",
                    "LicenseType": "ID",
                    "LicenseFront": "1801085783949557760",
                    "LicenseBack": "1801085766993141760",
                    "LicenseNum": "342201199410280001",
                    "LicenseAddr": "安徽省安徽省安徽省",
                    "Phone": "16655886267",
                    "Email": "qq@qq.com"
                }
            }
        },
        "code": 200
    },
    {
        "comment": "个体户-->暂存注册资料，最小传入校验（公司名称2个字、注册资金1元、注册年限5年）",
        "body": {
            "ICID": "1801085254920798208",
            "BasicInfo": {
                "Name": "有限",
                "BackupNames": [],
                "CapitalAmount": 1,
                "OperationYear": "5",
                "Industry": "CultureMedia",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "OperatorInfo": {
                "TemplateID": "1801085999194578944",
                "TemplateInfo": {
                    "TemplateID": "1801085999194578944",
                    "TemplateType": "Natural",
                    "Name": "故里",
                    "LicenseType": "ID",
                    "LicenseFront": "1801085783949557760",
                    "LicenseBack": "1801085766993141760",
                    "LicenseNum": "342201199410280001",
                    "LicenseAddr": "安徽省安徽省安徽省",
                    "Phone": "16655886267",
                    "Email": "qq@qq.com"
                }
            }
        },
        "code": 200
    },
    {
        "comment": "个体户-->暂存注册资料，最大传入校验（公司名称50个字、注册资金1亿元、注册年限999年）",
        "body": {
            "ICID": "1801085254920798208",
            "BasicInfo": {
                "Name": "四川后不合适可退服装有限公司四川后不合适可退服装有限公司四川后不合适可退服装有限公司四川后不合适可退",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "CultureMedia",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "OperatorInfo": {
                "TemplateID": "1801085999194578944",
                "TemplateInfo": {
                    "TemplateID": "1801085999194578944",
                    "TemplateType": "Natural",
                    "Name": "故里",
                    "LicenseType": "ID",
                    "LicenseFront": "1801085783949557760",
                    "LicenseBack": "1801085766993141760",
                    "LicenseNum": "342201199410280001",
                    "LicenseAddr": "安徽省安徽省安徽省",
                    "Phone": "16655886267",
                    "Email": "qq@qq.com"
                }
            }
        },
        "code": 200
    },
]

# 暂存注册资料--失败
data_post_SaveICRegMaterial_error = [
    {
        "comment": "公司-->错误的ICID，",
        "body": {
            "ICID": "180085234391394713",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20631,
                "Message": "工商注册信息不存在"
            }
        }
    },
    {
        "comment": "公司-->ICID为空",
        "body": {
            "ICID": "",
            "BasicInfo": {
                "Name": "天津地义借钱不还没能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "ICID不能为空"
            }
        }
    },
    {
        "comment": "公司-->非待补齐资料状态暂存数据",
        "body": {
            "ICID": "1801172632181841920",
            "BasicInfo": {
                "Name": "西藏东藏找不到有限责任公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20600,
                "Message": "只能在补齐资料阶段才能保存数据"
            }
        }
    },
    {
        "comment": "公司-->公司名称为空",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20601,
                "Message": "公司名称只能包含汉字和中文括号，长度必须2-50个字符之间"
            }
        }
    },
    {
        "comment": "公司-->公司名称1个字符",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20601,
                "Message": "【深】公司名称只能包含汉字和中文括号，长度必须2-50个字符之间"
            }
        }
    },
    {
        "comment": "公司-->公司名称51个字符",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司深圳不怕影子斜且不能力有限公司深圳不怕影子斜且不能力有限公司深圳不怕影子",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20601,
                "Message": "【深圳不怕影子斜且不能力有限公司深圳不怕影子斜且不能力有限公司深圳不怕影子斜且不能力有限公司深圳不怕影子】公司名称只能包含汉字和中文括号，长度必须2-50个字符之间"
            }
        }
    },
    {
        "comment": "公司-->公司名称除了中文及中文括号外其他的字符-英文括号",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "(深圳不怕影子斜且不能力有限公司)",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20601,
                "Message": "【(深圳不怕影子斜且不能力有限公司)】公司名称只能包含汉字和中文括号，长度必须2-50个字符之间"
            }
        }
    },
    {
        "comment": "公司-->注册资本为空",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "宁波打的电话已关机械有限公司",
                "BackupNames": [],
                "CapitalAmount": "",
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
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
        "comment": "公司-->注册资本0元",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "嘉兴饼干没有夹心有限公司",
                "BackupNames": [],
                "CapitalAmount": 0,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20603,
                "Message": "注册资本至少1元最多1亿元"
            }
        }
    },
    {
        "comment": "公司-->注册资本1亿零1元",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "新乡事成但我懒得想智力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000001,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20603,
                "Message": "注册资本至少1元最多1亿元"
            }
        }
    },
    {
        "comment": "公司-->经营年限除5、10、20、30、999外其他的年限",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "100",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "经营年限值不合法"
            }
        }
    },
    {
        "comment": "公司-->经营年限为空",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "经营年限值不合法"
            }
        }
    },
    {
        "comment": "公司-->行业为空",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "行业值不合法"
            }
        }
    },
    {
        "comment": "公司-->没有股东信息",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "16612345678",
                    "Address": "嘿嘿家的哈哈来收",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": []
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20606,
                "Message": "股东个数必须在1-50个之间"
            }
        }
    },
    {
        "comment": "公司-->股东模板与模板类型不符（法人类型传入自然人模板）",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "16612345678",
                    "Address": "嘿嘿家的哈哈来收",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Legal",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20609,
                "Message": "股东只能使用法人模板【故里】"
            }
        }
    },
    {
        "comment": "公司-->股东出资金额不正确",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "西藏东藏找不到有限责任公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999998,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20607,
                "Message": "股东出资总金额不等于注册资本"
            }
        }
    },
    {
        "comment": "公司-->股东重复",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "天津地义借钱不还没能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20607,
                "Message": "股东人员不能重复【故里】"
            }
        }
    },
    {
        "comment": "公司-->主要人员信息缺少-法定代表人",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "深圳不怕影子斜且不能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20617,
                "Message": "必须选择一位法人"
            }
        }
    },
    {
        "comment": "公司-->主要人员信息缺少-监事",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "义务不扫何以扫天下清洁能力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20618,
                "Message": "必须选择一位监事"
            }
        }
    },
    {
        "comment": "公司-->公司主要人员重复",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "四川后不合适可退服装有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20613,
                "Message": "公司主要人员选择模板不能重复【故里】"
            }
        }
    },
    {
        "comment": "公司-->公司主要人员主要（法定代表人、监事）职位重复",
        "body": {
            "ICID": "1800852343913947136",
            "BasicInfo": {
                "Name": "新乡事成但我懒得想智力有限公司",
                "BackupNames": [],
                "CapitalAmount": 100000000,
                "OperationYear": "999",
                "Industry": "Live",
                "Scope": "",
                "RecipientInfo": {
                    "Phone": "",
                    "Address": "",
                    "Name": ""
                }
            },
            "ShareholderInfos": {
                "ShareholderType": "Natural",
                "Shareholders": [
                    {
                        "TemplateID": "1801085999194578944",
                        "TemplateInfo": {
                            "TemplateID": "1801085999194578944",
                            "TemplateType": "Natural",
                            "Name": "故里",
                            "LicenseType": "ID",
                            "LicenseFront": "1801085783949557760",
                            "LicenseBack": "1801085766993141760",
                            "LicenseNum": "342201199410280001",
                            "LicenseAddr": "安徽省安徽省安徽省",
                            "Phone": "16655886267",
                            "Email": "qq@qq.com"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 99999999,
                        "CapitalRatio": "100.00%"
                    },
                    {
                        "TemplateID": "1801086905424076800",
                        "TemplateInfo": {
                            "TemplateID": "1801086905424076800",
                            "TemplateType": "Natural",
                            "Name": "李萌",
                            "LicenseType": "ID",
                            "LicenseFront": "1801086884867588096",
                            "LicenseBack": "1801086870214955008",
                            "LicenseNum": "230623200210090646",
                            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                            "Phone": "16612345678"
                        },
                        "TemplateType": "Natural",
                        "CapitalAmount": 1,
                        "CapitalRatio": "0.00%"
                    }
                ]
            },
            "PositionInfos": [
                {
                    "TemplateID": "1801085999194578944",
                    "TemplateInfo": {
                        "TemplateID": "1801085999194578944",
                        "TemplateType": "Natural",
                        "Name": "故里",
                        "LicenseType": "ID",
                        "LicenseFront": "1801085783949557760",
                        "LicenseBack": "1801085766993141760",
                        "LicenseNum": "342201199410280001",
                        "LicenseAddr": "安徽省安徽省安徽省",
                        "Phone": "16655886267",
                        "Email": "qq@qq.com"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                },
                {
                    "TemplateID": "1801086905424076800",
                    "TemplateInfo": {
                        "TemplateID": "1801086905424076800",
                        "TemplateType": "Natural",
                        "Name": "李萌",
                        "LicenseType": "ID",
                        "LicenseFront": "1801086884867588096",
                        "LicenseBack": "1801086870214955008",
                        "LicenseNum": "230623200210090646",
                        "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "Supervisor"
                    ]
                },
                {
                    "TemplateID": "1801227218369683456",
                    "TemplateInfo": {
                        "TemplateID": "1801227218369683456",
                        "TemplateType": "Natural",
                        "Name": "长安",
                        "LicenseType": "ID",
                        "LicenseFront": "1801227098093465600",
                        "LicenseBack": "1801227085722148864",
                        "LicenseNum": "342116199410280003",
                        "LicenseAddr": "安徽省合肥市1号",
                        "Phone": "16612345678"
                    },
                    "Position": [
                        "LegalRepresentative"
                    ]
                }
            ]
        },
        "code": 200,
        "resp": {
            "Error": {
                "Code": "",
                "CodeN": 20617,
                "Message": "法定代表人必须只有一位【故里,长安】"
            }
        }
    }
]

# 提交审核工商注册材料--成功
data_post_SubmitICRegMaterial_success = []

# 提交审核工商注册材料--失败
data_post_SubmitICRegMaterial_error = []

# 获取工商注册列表----------------------------------------------------------该写他了----------------------------------------------------------
data_get_ListInfos = [
    {
        "comment": "根据工商注册唯一ID查看",
        "": {
            "ICID": "",
        }
    }
]

# 获取工商注册资料
data_get_GetICRegMaterial = [
    {
        "comment": "",
        "": {

        }
    }
]

# 获取工商注册基本信息
data_get_GetICInfo = []

# 获取行业和行业范围
data_get_GetIndustryScopes = [
    {
        "comment": "",
        "": {

        }
    }
]
