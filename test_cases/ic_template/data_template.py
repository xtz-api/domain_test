import random
import string
from util.db_check import *

"""下方定义是：生成连个随机的字符串类型的文字，为了创建模板的时候，名称不会重复"""
# 定义包含中文字符的列表
str1 = ["天", "外", "来", "物", "匆", "匆", "那", "年", "我", "你", "他", "她", "它", "们", "的", "是", "在", "有", "不", "和", "与", "为", "对", "中", "华", "人", "民", "共", "和", "国",
        "壹", "佰", "贰", "拾", "叁", "亿", "肆", "仟", "伍", "佰", "陆", "拾", "柒", "万", "捌", "仟", "玖", "佰", "壹", "拾"]
# 生成随机的中文字符串
# random.choice(str1)会在str1列表中随机选择一个字符作为当前迭代的值。for _ in range(2)表示我们要进行两次迭代，即从str1列表中选择两个字符。
# 使用''.join()函数将它们连接成一个字符串。每次运行代码时，将会随机选择两个中文字符并将它们拼接成一个字符串。
random_str1 = ''.join(random.choice(str1) for _ in range(2))
random_str2 = ''.join(random.choice(str1) for _ in range(2))

"""下方定义是：生成随机的5位数字，为了给证件号使用的。"""
random_int = random.randint(10000, 99999)

"""下方定义是：为了获取大写的英文字母，且不包括特定的字母（characters_to_exclude = "IOZSV"），为了给法人的社会统一信用代码使用的。"""
# 定义包含数字和大写字母的字符串：string.digits包含了所有的数字字符，而string.ascii_uppercase包含了所有的大写字母字符
digits_and_letters = string.digits + string.ascii_uppercase
# 将IOZSV赋值给了characters_to_exclude
characters_to_exclude = "IOZSV"
# 从字符集中排除指定的大写字母：就是列表推导式的完整语法，它遍历 digits_and_letters 中的每个字符，并只保留那些不在 characters_to_exclude 中的字符。
allowed_characters = [ch for ch in digits_and_letters if ch not in characters_to_exclude]
# 生成随机字符串：random.choices(allowed_characters)随机选择上述遍历出来的值，k=5，选择5个元素。最后使用''.jion()函数将他们拼接成一个字符串。
random_string1 = ''.join(random.choices(allowed_characters, k=5))

"""创建模板"""
# 创建模板-->自然人
data_post_CreateTemplate_Natural = [
    {
        "comment": "创建自然人-->名称2个字",
        "body": {
            "TemplateType": "Natural",
            "Name": random_str1,
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->名称30个字",
        "body": {
            "TemplateType": "Natural",
            "Name": "自然人的自动化创建的自然人模板名称自动化创建的自然人模板" + random_str2,
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002122" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->地址=8位数",
        "body": {
            "TemplateType": "Natural",
            "Name": "自动化创建的地址等于八个字符",
            "LicenseAddr": "这里刚好8个字符",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002012" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->地址+其他字符=50位数",
        "body": {
            "TemplateType": "Natural",
            "Name": "自动化创建的地址等于五十个字符",
            "LicenseAddr": "超过最大限制五十位这个名称刚好是五十位字符啦，其中还惨杂着其他的，像特殊符号%……、英文q、数字1。",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002022" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->证件号18位数字",
        "body": {
            "TemplateType": "Natural",
            "Name": "自动化创建的证件号十八位纯数字",
            "LicenseAddr": "这里刚好8个字符",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002032" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->证件号17位数字+X",
        "body": {
            "TemplateType": "Natural",
            "Name": "自动化创建的证件号十七位数字加埃克斯",
            "LicenseAddr": "这里刚好8个字符",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "240623200007" + str(random_int) + "X",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->Email为空",
        "body": {
            "TemplateType": "Natural",
            "Name": random_str1,
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002042" + str(random_int),
            "Phone": "16612345678",
            "Email": ""
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建自然人-->Email字段不传",
        "body": {
            "TemplateType": "Natural",
            "Name": random_str1,
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002052" + str(random_int),
            "Phone": "16612345678",
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },

]

# 创建模板-->法人
data_post_CreateTemplate_Legal = [
    {
        "comment": "创建法人-->名称2个字",
        "body": {
            "TemplateType": "Legal",
            "Name": random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseNum": "92441900MA000" + random_string1,
            "LicenseFront": "1785228609754796032",
            "Phone": "16611234567",
            "Email": "qq@qq.com",
            "LegalRepresentative": {
                "LicenseFront": "1785203507324309504",
                "LicenseBack": "1785203480831963136",
                "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                "LicenseNum": "2406232002100" + str(random_int),
                "Name": "法人"
            }
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建法人-->名称30个字",
        "body": {
            "TemplateType": "Legal",
            "Name": "法人自动化创建的法人模板的名称自动化创建的法人模板的名称" + random_str2,
            "LicenseAddr": "北京市北京市1号",
            "LicenseNum": "92441900MA012" + random_string1,
            "LicenseFront": "1785228609754796032",
            "Phone": "16611234567",
            "Email": "qq@qq.com",
            "LegalRepresentative": {
                "LicenseFront": "1785203507324309504",
                "LicenseBack": "1785203480831963136",
                "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                "LicenseNum": "3422011994102" + str(random_int),
                "Name": "法人"
            }
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建法人-->社会统一信用代码=18位纯数字",
        "body": {
            "TemplateType": "Legal",
            "Name": "自动化创建证件号纯数字",
            "LicenseAddr": "北京市北京市1号",
            "LicenseNum": "9244190035000" + str(random_int),
            "LicenseFront": "1785228609754796032",
            "Phone": "16611234567",
            "Email": "qq@qq.com",
            "LegalRepresentative": {
                "LicenseFront": "1785203507324309504",
                "LicenseBack": "1785203480831963136",
                "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                "LicenseNum": "2406232002100" + str(random_int),
                "Name": "法人"
            }
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    },
    {
        "comment": "创建法人-->社会统一信用代码数字+字母",
        "body": {
            "TemplateType": "Legal",
            "Name": "自动化创建证件号数字加字母",
            "LicenseAddr": "北京市北京市1号",
            "LicenseNum": "92441900AM000" + random_string1,
            "LicenseFront": "1785228609754796032",
            "Phone": "16611234567",
            "Email": "qq@qq.com",
            "LegalRepresentative": {
                "LicenseFront": "1785203507324309504",
                "LicenseBack": "1785203480831963136",
                "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3-10号5门302室",
                "LicenseNum": "3406232002100" + str(random_int),
                "Name": "法人"
            }
        },
        "code": 200,
        "Result": {
            "TemplateID": "1785204155540750336"
        }
    }
]

# 创建模板-->失败
data_post_CreateTemplate_error = [
    {
        "comment": "创建失败-->Name字段为必传字段",
        "body": {
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "2406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称有非中文（英文字符）",
        "body": {
            "Name": "创建自然人ziran",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "3406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称有非中文（特殊符号字符）",
        "body": {
            "Name": "创建自然人@##￥",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "4406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称有非中文（数字字符）",
        "body": {
            "Name": "创建自然人666",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "5406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称有非中文（空格字符）",
        "body": {
            "Name": "创建 自然 人",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "6406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称长度不够（小于2位数）",
        "body": {
            "Name": "创",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "7406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称长度超限（大于30位数）",
        "body": {
            "Name": "创建失败名称超过最大限制三十位这个名称已经是三十一位字符啦哈哈",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "8406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->名称参数为空",
        "body": {
            "Name": "",
            "LicenseAddr": "黑龙江省大庆市萨尔图区拥军大街3",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "9406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20419,
                "Message": "姓名只能包括中文，长度必须2-30个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseAddr字段为必传字段",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1406232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20420,
                "Message": "证件地址必须包含中文，长度在8-50个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->地址长度错误（小于8位数）",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1106232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20420,
                "Message": "证件地址必须包含中文，长度在8-50个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->地址长度错误（大于50位数）",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "超过最大限制五十位这个名称刚好是五十位字符啦，其中还惨杂着其他的，像特殊符号%……、英文q、数字1。嘿哈",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1206232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20420,
                "Message": "证件地址必须包含中文，长度在8-50个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->地址错误（未包含中文）",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "qwq1243456",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1306232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20420,
                "Message": "证件地址必须包含中文，长度在8-50个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->地址错误（参数为空）",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1606232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20420,
                "Message": "证件地址必须包含中文，长度在8-50个字符之间"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseBack字段为必传字段",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1706232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "身份证人头面证件缺失"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseBack错误",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "178520348083196313",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1806232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "部分证件照片信息不存在"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseBack为空",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "1906232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "身份证人头面证件缺失"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseFront字段为必传字段",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseNum": "2006232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "身份证徽章面证件缺失"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseFront错误",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "178520350732430950",
            "LicenseNum": "2106232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "部分证件照片信息不存在"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseFront为空",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "",
            "LicenseNum": "2206232002100" + str(random_int),
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "身份证徽章面证件缺失"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseNum字段为必传字段",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20417,
                "Message": "身份证号码格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseNum大于18位",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": str(random_int) + "21997070328201",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20417,
                "Message": "身份证号码格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseNum小于18位",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": str(random_int) + "219970703282",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20417,
                "Message": "身份证号码格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseNum+其他字符",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "qw中文2219970703282",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20417,
                "Message": "身份证号码格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseNum为空",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20417,
                "Message": "身份证号码格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->LicenseNum重复",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230623200210090616",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20471,
                "Message": "已有相同证件号码自然人/法人存在，无需重复创建【李萌】"
            }
        }
    },
    {
        "comment": "创建失败-->Phone字段为必传字段",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230623200210090616",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->Phone小于11位",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "231623200210090616",
            "Phone": "1661234567",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->Phone大于11位",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230633200210090616",
            "Phone": "166123456789",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->Phone错误的号段110开头",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230633200210090616",
            "Phone": "11012345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->Phone参数为空",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230633200210090616",
            "Phone": "",
            "Email": "1353357433@qq.com",
            "TemplateType": "Natural"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20415,
                "Message": "联系电话格式不正确，请重新输入"
            }
        }
    },
    {
        "comment": "创建失败-->TemplateType字段为必传字段",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230633200210090616",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "类型值不合法"
            }
        }
    },
    {
        "comment": "创建失败-->TemplateType参数为空",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230633200210090616",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": ""
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "类型值不合法"
            }
        }
    },
    {
        "comment": "创建失败-->TemplateType自然人类型传入法人值",
        "body": {
            "Name": "自然人" + random_str1,
            "LicenseAddr": "北京市北京市1号",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230633200210090616",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateType": "Legal"
        },
        "code": 200,
        "ResponseMetadata": {
            "Error": {
                "Code": "",
                "CodeN": 20400,
                "Message": "法人身份证徽章面证件缺失"
            }
        }
    }
]

"""查看模板详情"""
data_get_Template = [
    {
        "comment": "查看模板详情",
        "params": {
            "TemplateID": templateID_sql()[0][0]
        },
        "code": 200
    },
    {
        "comment": "查看失败-->模板不存在",
        "params": {
            "TemplateID": "173258873194971955"
        },
        "code": 200
    },
    {
        "comment": "查看失败-->参数为空",
        "params": {
            "TemplateID": ""
        },
        "code": 200
    }
]

"""获取模板列表"""
data_get_ListTemplate = [
    {
        "comment": "获取第1页的前3条数据",
        "params": {
            "PageNumber": 1,
            "PageSize": 3
        },
        "code": 200,
        # "resp": "SELECT template_id FROM ic_template WHERE account_id=2100000056 ORDER BY id DESC LIMIT 3"
    },
    {
        "comment": "根据名称搜索（支持模糊搜索）",
        "params": {
            "Name": "故里"
        },
        "code": 200,
        # "resp": "SELECT * FROM ic_template WHERE account_id=2100000056 and name='故里' LIMIT 1"
    },
    {
        "comment": "根据模板ID搜索",
        "params": {
            "TemplateID": templateID_sql()[0][0]
        },
        "code": 200,
        # "resp": "SELECT template_id FROM ic_template WHERE account_id=2100000056 ORDER BY id DESC LIMIT 1"
    },
    {
        "comment": "根据模板类型搜索",
        "params": {
            "TemplateType": "Natural",
            # Natural       自然人模板
            # Legal         法人模板
            "PageSize": 3
        },
        "code": 200,
        # "resp": "SELECT * FROM ic_template WHERE account_id=2100000056 and template_type='Natural' ORDER BY id DESC LIMIT 3"
    }
]

"""更新模板"""
data_post_UpdateTemplate = [
    {
        "comment": "更新自然人模板信息",
        "body": {
            "TemplateType": "Natural",
            "Name": "故里个人勿删",
            "LicenseAddr": "北京市工商服务管理",
            "LicenseBack": "1785203480831963136",
            "LicenseFront": "1785203507324309504",
            "LicenseNum": "230623200210090610",
            "Phone": "16612345678",
            "Email": "1353357433@qq.com",
            "TemplateID": "1739546379958775808"
        },
        "code": 200
    },
    {
        "comment": "更新法人模板信息",
        "body": {
            "TemplateID": "1729786637431840768",
            "TemplateType": "Legal",
            "Name": "长安公司勿删",
            "LicenseAddr": "北京市北京市1号",
            "LicenseNum": "92611105MA6TJKL572",
            "LicenseFront": "1785228609754796032",
            "Phone": "16611234567",
            "Email": "qq@qq.com",
            "LegalRepresentative": {
                "LicenseFront": "1785203507324309504",
                "LicenseBack": "1785203480831963136",
                "LicenseAddr": "北京市北京市1号",
                "LicenseNum": "230623200210090646",
                "Name": "法人"
            }
        },
        "code": 200
    }
]
