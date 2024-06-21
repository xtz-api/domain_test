import copy
import ipaddress
import random
import logging
import uuid
import json
import requests
import datetime
import time


def get_tiagw_auth(idc, change_id=False):
    if idc == "boe":
        url = 'https://cloud-boe.bytedance.net/auth/api/v1/jwt'
    else:
        url = 'https://cloud.bytedance.net/auth/api/v1/jwt'
    if change_id:
        headers = {'Authorization': 'Bearer 52407769b02bc69d008de1efbbe02293'}
    else:
        headers = {'Authorization': 'Bearer 52407769b02bc69d008de1efbbe02293'}
    r = requests.get(url, headers=headers)
    resp_headers = r.headers
    auth = "Bearer " + resp_headers["X-Jwt-Token"]
    return auth


# Return a 8 byte uuid
def get_uuid():
    r = str(uuid.uuid4())
    return r.split('-')[0]


def get_uuid16():
    r = str(uuid.uuid4())
    return r


def response_message(response):
    if 'message' in response:
        if response["message"] is not None and response["message"].strip():
            return "实际响应：" + json.dumps(response) + "\nMessage：" + response["message"].encode("utf-8").decode("utf-8")
    if 'errors' in response:
        if 'message' in response["errors"]:
            return "实际响应：" + json.dumps(response) + "\nMessage：" + response["errors"]["message"].encode("utf-8").decode(
                "utf-8")
        if response["errors"][0]["message"] is not None:
            if response['errors'][0]["message"] == '内部错误':
                if response['errors'][0]['extensions']['message'] is not None:
                    return "实际响应：" + json.dumps(response) + "\nMessage：" + response['errors'][0]['extensions'][
                        'message'].encode("utf-8").decode("utf-8")
            return "实际响应：" + json.dumps(response) + "\nMessage：" + response["errors"][0]["message"].encode(
                "utf-8").decode("utf-8")

    return "实际响应：" + json.dumps(response)


def not_in_error(item, container):
    return "期望结果包含：" + json.dumps(item) + "\n实际结果：" + json.dumps(container)


def bytes2json(body):
    """bytes转json

    Python3的字符串的编码语言用的是unicode编码，由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干字节。
    如果要在网络上传输，或保存在磁盘上就需要把str变成以字节为单位的bytes。
    收到的返回是b’xxxxxx’时，需要进行这种转换
    """
    return json.loads(str(body, 'utf-8'))


def ipv6():
    key = str(ipaddress.IPv6Address(random.randint(0, 2 ** 128 - 1)))
    return key


def ipv4():
    key = str(ipaddress.IPv4Address(random.randint(0, 2 ** 32 - 1)))
    return key


def ramdom_value(Type):
    # 根据类型返回随机value
    if Type == "A":
        return ipv4()
    if Type == "AAAA":
        return ipv6()


def getDiff2(arr1, arr2):
    set_1 = ()
    set_2 = ()

    # 将列表转换为集合set()
    set_1 = set(arr1)
    set_2 = set(arr2)

    set_more1 = ()
    set_more2 = ()

    # 集合运算
    set_1_2 = set_1 & set_2
    set_more1 = set_1 - set_1_2
    set_more2 = set_2 - set_1_2
    logging.info(set_more1)
    logging.info(set_more2)
    return set_more1, set_more2


def local_time():
    """获取当前时间格式 2021-08-08"""
    now_t = datetime.datetime.now().strftime("%Y-%m-%d")
    return now_t


def past_time(days):
    """以当天时间为基准，向前推 days 天  输出格式：2021-08-08"""
    past_t = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
    return past_t

def day_time_time():
    """获取当天零点时间戳"""
    day_time = time.mktime(datetime.date.today().timetuple())
    day_time_int = int(day_time)
    return day_time_int

def record_to_records_lists(num, data_create_batch, r="random"):
    """
    构建多条 record 内容，用于批量创建
    r 为 random 时，rr使用随机名称。r 为 fixed 时，rr使用相同名称
    """
    data_create_batch["input"]["records"][0].update({"rr": get_uuid()})
    new_data_create_batch = copy.deepcopy(data_create_batch)
    del new_data_create_batch["input"]["records"][1:]
    if num == 501:
        new_data_create_batch["expect"].update({"code": 300046})
    if r == "random":
        new_data_create_batch["input"]["records"][0].update({"rr": get_uuid(), "value": ramdom_value(new_data_create_batch["input"]["records"][0]["type"])})
    elif r == "fixed":
        new_data_create_batch["input"]["records"][0].update({"value": ramdom_value(new_data_create_batch["input"]["records"][0]["type"])})
    while True:
        if len(new_data_create_batch["input"]["records"]) == num:
            new_data_create_batch.update({"comment": "批量新增" + str(num) + "条解析记录"})
            break
        new_records = copy.deepcopy(new_data_create_batch["input"]["records"][0])
        if r == "random":
            new_records.update({"rr": get_uuid(), "value": ramdom_value(new_records["type"])})
        elif r == "fixed":
            new_records.update({"value": ramdom_value(new_records["type"])})
        new_data_create_batch["input"]["records"].append(new_records)
    return new_data_create_batch


def draw_value(datas):
    """
    datas 为 传入的参数数据
    例如：
    [{
        "type": CONSTANT.Type_AAAA,
        "value": lib.ipv6(),
        "line": "DEFAULT",
        "ttl": "600",
    },
    {
        "type": CONSTANT.Type_AAAA,
        "value": lib.ipv6(),
        "line": "DEFAULT",
        "ttl": "600",
    },
    ]
    """
    values = []
    for record_data in datas:
        values.append(record_data["value"])
    return values


def check_value(initial_values, result_values):
    """
    initial_value,result_value 都是 dict
    """
    i = 0
    for value in initial_values:
        if value in result_values:
            i += 1
        else:
            pass
    if i != 0 and len(initial_values) == len(result_values):
        return True
    elif i == len(result_values):
        return True
    else:
        return False


def backups_compare(backups_before_data, restore_after_data):
    pass_num = 0
    ispass_num = []
    data_before_list = backups_before_data["response"]["domain_records"]
    data_after_list = restore_after_data["response"]["domain_records"]
    assert len(data_before_list) == len(data_after_list), "Assert Error:%s \nAssert Error:%s" % (
        backups_before_data, restore_after_data)
    for len_i in range(0, len(data_before_list)):
        for len_j in range(0, len(data_before_list)):
            key_num = 0
            if len_j not in ispass_num:
                for key in data_before_list[len_i].keys():
                    key_num += 1
                    if key in ["id", "record_id", "last_operator", "last_operation", "created_at", "updated_at"]:
                        pass
                    else:
                        if data_before_list[len_i][key] != data_after_list[len_j][key]:
                            if key == "line":
                                if data_before_list[len_i][key] in ["DEFAULT", "default", "1", "784"] and data_after_list[len_j][key] in ["DEFAULT", "default", "1", "784"]:
                                    pass
                                else:
                                    break
                            else:
                                break
                if key_num == len(data_before_list[len_i]):
                    pass_num += 1
                    ispass_num.append(len_j)
                    break
            else:
                pass
    # logging.info(ispass_num)
    assert len(data_before_list) == pass_num, "Assert Error:%s \nAssert Error:%s" % (
        backups_before_data, restore_after_data)


def gtm_top_or_tiagw_assert(client, resp, code):
    if client.gateway == "top":
        assert judge_code(resp, code), "预期Code=%s,%s" % (code, response_message(resp))
    elif client.gateway == "tiagw":
        assert resp.get("code", None) == code, "预期Code=%s,%s" % (code, response_message(resp))


def judge_code(resp, code):
    if "ResponseMetadata" in resp:
        if code == 0 and "CodeN" not in str(resp):
            return True
        else:
            if "Error" in str(resp):
                if code == resp["ResponseMetadata"]["Error"]["CodeN"]:
                    return True
                else:
                    return False
            else:
                if "CodeN" in str(resp):
                    if code == resp["Result"]["check_result"][0]["ret_code"]["CodeN"]:
                        return True
                    else:
                        return False
                else:
                    return False
    else:
        return False


def ip_segment():
    """生成随机ip段，如 20.184.221.0/24"""
    ip = str(ipaddress.IPv4Address(random.randint(0, 2 ** 32 - 1)))
    ip_s = str(ipaddress.IPv4Network(ip + "/24", strict=False))  # 例：20.184.221.0/24
    return ip_s


def ip_segment_ipv6():
    """生成随机ipv6段，如 1541:cf15:a37c:af:a7c8:1d77:d60d:0/112"""
    ip = str(ipaddress.IPv6Address(random.randint(0, 2 ** 128 - 1)))
    ip_s = str(ipaddress.IPv6Network(ip + "/112", strict=False))  # 例：1541:cf15:a37c:af:a7c8:1d77:d60d:0/112
    return ip_s


def custom_line_find(name, custom_line_resp):
    for line_data in custom_line_resp["response"]["lines"]:
        if line_data["name"] == name:
            return line_data["value"]


def class_to_dict(obj):
    # 嵌套对象转化为字典
    if not hasattr(obj, "__dict__"):
        return obj
    result = {}
    for key, val in obj.__dict__.items():
        if key.startswith("_"):
            continue
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(class_to_dict(item))
        else:
            element = class_to_dict(val)
        result[key] = element
    return result


def dict_to_class(class_name, config, class_map):
    # dict转为类
    for config_param in config:
        if isinstance(config[config_param], dict):
            config[config_param] = dict_to_class(config_param, config[config_param], class_map)
        if isinstance(config[config_param], list):
            for i in range(len(config[config_param])):
                if isinstance(config[config_param][i], dict):
                    config[config_param][i] = dict_to_class(config_param, config[config_param][i], class_map)
    return class_map[class_name](**config)


def open_file(Type="consistent"):
    """小于规则传入 small ，符合条件 consistent  ，大于规则传入 big。 默认为 consistent
        格式暂时有 gif png 直接传入即可
    """
    path = "data/file/img_base64_data_small"
    if Type == "big":
        path = "data/file/img_base64_data"
    if Type == "small":
        path = "data/file/img_base64_data_small"
    if Type == "consistent":
        path = "data/file/img_base64_data_consistent"
    if Type == "gif":
        path = "data/file/img_base64_data_gif"
    if Type == "png":
        path = "data/file/img_base64_data_png"
    with open(path, "r+") as f:
        data = f.read()
    return data
