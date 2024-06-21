import os
import pytest
import logging
import logging.config
from util import lib

# CONFIG_PATH = "conf/conf.yml"
# lg = Logger(__name__)
#
# def pytest_addoption(parser):
#     parser.addoption(
#        "--tag", action="store", default="",
#        help="Specify tags. If given, only execute the testcases with tags. You can use multiple tags, dividing with ','.")
#     parser.addoption(
#        "--no_tag", action="store", default="",
#        help="Specify tags. If given, only execute the testcases without tags. You can use multiple tags, dividing with ','.")
#     parser.addoption(
#        "--executor", action="store", default="",
#        help="Executor name. If given, only execute the testcases with pytest.mark.executor('Executor Name')'.")
#     parser.addoption(
#         "--env", action="store", default="offline", help="env: offline/online"
#     )
#
# @pytest.fixture(scope='session', autouse=True)
# def get_base_config(request):
#     env = request.config.getoption("--env")
#     cfg_json = load_yml(CONFIG_PATH)
#     cur_cfg = cfg_json[env]
#     BaseConfig.set_config(**cur_cfg)
#     lg.info("current base configuration: %s", BaseConfig.__dict__)


"""以下为自定义函数/方法"""


def pytest_addoption(parser):
    parser.addoption("--tag", action="store", default="",
                     help="Specify tags. If given, only execute the testcases with tags. You can use multiple tags, dividing with ','.")
    parser.addoption("--no_tag", action="store", default="robustness",
                     help="Specify tags. If given, only execute the testcases without tags. You can use multiple tags, dividing with ','.")
    parser.addoption("--list", action="store_true", default=False,
                     help="List mode. Will only list out the testcases, and its markers.")
    parser.addoption("--env", action="store", default="autotest",
                     help="Specify the environment, use prod or autotest")
    parser.addoption("--idc", action="store", default="boe",
                     help="Specify idc to run test cases")
    parser.addoption("--server", action="store", default="",
                     help="Specify the server, use ip")
    parser.addoption("--clean", action="store_true", default=False,
                     help="Clean mode. Will set the run for clean.")
    parser.addoption("--gateway", action="store", default="tiagw",
                     help="Specify the gateway, use tiagw or top (top for volcengine).")
    parser.addoption("--project_name", action="store", default="",
                     help="Specify tags. If given, only execute the project_name cases. You can use multiple project_name, dividing with ','.")


def pytest_runtest_setup(item):
    # Print testcase info when execution
    print("")
    print("=====" + item.name + "=====")
    for marker in item.iter_markers():
        print("    " + marker.name + ": ", end=" ")
        if len(marker.args) == 1:
            print(marker.args[0])
        else:
            print(marker.args)


def pytest_collection_modifyitems(items, config):
    # Filter testcases by tag, when collecting testcases
    tag_str = config.getoption("--tag")
    filter_items_by_tag(items, config, tag_str)
    if "robustness" not in tag_str:
        tag_str = config.getoption("--no_tag")
        filter_items_by_no_tag(items, config, tag_str)
    # Filter testcases by project_name, when collecting testcases
    project_name_str = config.getoption("--project_name")
    filter_items_by_project_name(items, config, project_name_str)
    # List the testcase, when --list is given
    list_flag = config.getoption("--list")
    list_items_by_flag(items, config, list_flag)


# 仓库和tag的映射，增加仓库或者tag必须补充此map
tags_of_project_name_map = {
    # DNS回归任务
    "dns_regression": ["dns_check", "Weight_mgmt", "domain_mgmt", "domain_group_mgmt", "domain_record", "batch_ops",
                       "base_info", "zone_sync", "zones", "back_up", "custom_line", "dns_check", "trades", "stats"],
    "dns_clean": ["clean"],  # DNS解析每日清理任务
    "joint_zones": ["joint_zones"]  # 内部调用接口
}


def filter_items_by_project_name(items, config, project_name_str):
    # Print executor info
    if project_name_str == '':
        print("project_name_str: (No project_name specified)")
        return
    print("project_name_str: " + project_name_str)

    tags = ["null"]

    project_names = str.split(project_name_str, ',')
    for project_name in project_names:
        if project_name in tags_of_project_name_map:
            tags.extend(tags_of_project_name_map[project_name])

    tags = list(set(tags))

    # For each testcases, find the value of tag marker
    # Select the items with executor name, deselect the others
    selected_items = []
    deselected_items = []
    for item in items:
        select_flag = False
        for tag_marker in item.iter_markers(name="tag"):
            for item_tag in tag_marker.args:
                for tag in tags:
                    if tag == item_tag:
                        select_flag = True
        if select_flag:
            selected_items.append(item)
        else:
            deselected_items.append(item)
    # Call hook to deselect items
    config.hook.pytest_deselected(items=deselected_items)
    # Re-set the items with selected items
    items[:] = selected_items


# Filter testcases by tag list


def filter_items_by_tag(items, config, tag_str):
    # Print executor info
    if tag_str == '':
        print("Tag: (No tag specified)")
        return
    print("Tag: " + tag_str)

    tags = str.split(tag_str, ',')
    # For each testcases, find the value of tag marker
    # Select the items with executor name, deselect the others
    selected_items = []
    deselected_items = []
    for item in items:
        select_flag = False
        for tag_marker in item.iter_markers(name="tag"):
            for item_tag in tag_marker.args:
                for tag in tags:
                    if tag == item_tag:
                        select_flag = True
        if select_flag:
            selected_items.append(item)
        else:
            deselected_items.append(item)
    # Call hook to deselect items
    config.hook.pytest_deselected(items=deselected_items)
    # Re-set the items with selected items
    items[:] = selected_items


# List items only, if list_flag is True


def filter_items_by_no_tag(items, config, tag_str):
    # Print executor info
    if tag_str == '':
        print("No_Tag: (No tag specified)")
        return
    print("No_Tag: " + tag_str)

    tags = str.split(tag_str, ',')
    # For each testcases, find the value of tag marker
    # Select the items with executor name, deselect the others
    selected_items = []
    deselected_items = []
    for item in items:
        select_flag = False
        for tag_marker in item.iter_markers(name="tag"):
            for item_tag in tag_marker.args:
                for tag in tags:
                    if tag == item_tag:
                        select_flag = True
        if select_flag:
            deselected_items.append(item)
        else:
            selected_items.append(item)
    # Call hook to deselect items
    config.hook.pytest_deselected(items=deselected_items)
    # Re-set the items with selected items
    items[:] = selected_items


def list_items_by_flag(items, config, list_flag):
    if list_flag:
        total = 0
        for item in items:
            total = total + 1
            print("=====" + item.name + "=====")
            for marker in item.iter_markers():
                print("    " + marker.name + ": ", end=" ")
                if len(marker.args) == 1:
                    print(marker.args[0])
                else:
                    print(marker.args)

        print("")
        print("==== total " + str(total) + " ====")

        # If list_flag, all items is deselected
        config.hook.pytest_deselected(items=items)
        items[:] = []


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "tag(tags): mark some tags for the testcase, can be a tag list.")
    config.addinivalue_line("markers", "title: testcase title.")
    config.addinivalue_line(
        "markers", "executor(executor_name): this testcase is assigned to executor_name.")
    config.addinivalue_line(
        "markers", "manual: this testcase is manually executed, and will accept console input.")


"""以下为fixture"""


@pytest.fixture(scope="session", autouse=True)
def log_config():
    path = "log"
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s][%(levelname)s][%(thread)d][%(module)s:%(funcName)s:%(lineno)d]>>>%(message)s'
            }
        },
        'filename': 'cache_agent.log',
        'filemode': 'a',
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'log/mplog.log',
                'mode': 'a+',
                'formatter': 'default',
            },
            'foofile': {
                'class': 'logging.FileHandler',
                'filename': 'log/mplog-foo.log',
                'mode': 'w',
                'formatter': 'default',
            },
            'errors': {
                'class': 'logging.FileHandler',
                'filename': 'log/mplog-errors.log',
                'mode': 'w',
                'level': 'ERROR',
                'formatter': 'default',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            }
        },
        'loggers': {
            'foo': {
                'handlers': ['foofile']
            }
        },
        'root': {
            'handlers': ['console', 'file', 'errors'],
            'level': "INFO"
        }
    }
    logging.config.dictConfig(config)


# @pytest.fixture(scope="function")
# def uuid():
#     uuid = lib.get_uuid()
#     return uuid

#
# @pytest.fixture(scope="function")
# def test_name(request):
#     test_name = request.node.name
#     return test_name

#
# @pytest.fixture(scope="session")
# def server(request, gateway, idc):
#     server = request.config.getoption("--server")
#     if server is None or server == "":
#         if idc == "lf" and gateway == "tiagw":
#             server = "10.29.33.214"
#         if idc == "lf" and gateway == "top":
#             # server = "ns1.volcdns.com"
#             # server = "180.184.68.1"
#             server = "122.193.250.18"
#         if idc == "boe" and gateway == "tiagw":
#             server = "10.225.121.231"
#         if idc == "boe" and gateway == "top":
#             server = "10.225.121.231"
#     else:
#         pass
#     return server


@pytest.fixture(scope="session")
def idc(request):
    idc = request.config.getoption("--idc")
    if idc is None or idc == "" or idc == "boe":
        idc = "boe"
        logging.info("被测idc为：%s" % idc)
    # else:
    #     assert False, "请勿线上测试"
    return idc


@pytest.fixture(scope="session")
def env(request):
    env = request.config.getoption("--env")
    if env is None or env == "":
        env = "autotest"
    logging.info("被测env为:%s" % env)
    return env


@pytest.fixture(scope="session")
def gateway(request):
    gateway = request.config.getoption("--gateway")
    if gateway is None or gateway == "":
        gateway = "tiagw"
    logging.info("被测gateway为:%s" % gateway)
    return gateway
