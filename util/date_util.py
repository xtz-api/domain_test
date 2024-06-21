import datetime, time

from datetime import datetime, date


def convert_to_timestamp(date_str):
    """将当前日期转换成时间戳(整数)"""
    date_obj = datetime.strptime(str(date_str), "%Y-%m-%d").date()
    datetime_obj = datetime.combine(date_obj, datetime.min.time())
    timestamp = int(datetime_obj.timestamp())
    return timestamp


# 示例调用
# date_str = "2024-05-31"
# timestamp = convert_to_timestamp(date_str)
# print(timestamp)

"""将当前日期转换成时间戳(整数)"""
date_time = date.today()  # 当天日期：可将 date.today() 换成想要的参数，将获取到的时间参数赋值给date_string

# 由于datetime.strptime只能接受str类型的日期格式，故str(date_string)；
# 通过datetime.strptime函数将 date_string也就是获取到的日期，解析成相对应的日期格式"%Y-%m-%d"
# .date()意思，只有日期格式，如：2025-05-16，如果不加.date()，则会是：2025-05-16 00:00:00
date_obj1 = datetime.strptime(str(date_time), "%Y-%m-%d").date()
# print(f"{date_obj1}有data")

# datetime.combine()方法将一个日期对象和一个时间对象组合在一起，创建一个新的日期时间对象。
# 在这里，我们使用date_obj作为日期部分；datetime.min.time()作为时间部分，默认为午夜时间（00:00:00）
datetime_obj = datetime.combine(date_obj1, datetime.min.time())
# 通过调用 datetime_obj.timestamp() 方法获取 datetime_obj 对象的时间戳，得到一个浮点数形式的时间戳。
# 然后，使用 int() 函数将其转换为正整数形式，存储在 timestamp 变量中。
timestamp1 = int(datetime_obj.timestamp())

# print(timestamp1)

"""将当前日期时间转换成时间戳"""
date_string = datetime.now()  # 当天日期时间
print(date_string)
timestamp = int(date_string.timestamp())

# print(timestamp)


class DateUtil(object):
    """这个前任写的，目前还未被引用，先留着"""

    @classmethod
    def get_today(cls) -> (int, int):
        '''
        获取今日0点和今日24点的时间戳
        :return:
        '''
        begin_time = datetime.date.today()
        end_time = begin_time + datetime.timedelta(days=1)
        begin_time_stamp = int(time.mktime(time.strptime(str(begin_time), '%Y-%m-%d')))
        end_time_stamp = int(time.mktime(time.strptime(str(end_time), '%Y-%m-%d'))) - 1
        return begin_time_stamp, end_time_stamp

    @classmethod
    def get_theweek(cls) -> (int, int):
        '''
        获取本周周始0点和周末24点的时间戳
        :return:
        '''
        today = datetime.date.today()
        week = today.weekday()
        begin_time = today - datetime.timedelta(days=week)
        begin_time_stamp = int(time.mktime(time.strptime(str(begin_time), '%Y-%m-%d')))
        end_time = begin_time + datetime.timedelta(days=5)
        end_time_stamp = int(time.mktime(time.strptime(str(end_time), '%Y-%m-%d'))) - 1
        return begin_time_stamp, end_time_stamp

    @classmethod
    def get_themonth(cls) -> (int, int):
        '''
        获取本月月始0点和月末24点的时间戳
        :return:
        '''
        today = datetime.date.today()
        days = today.day - 1
        begin_time = today - datetime.timedelta(days=days)
        begin_time_stamp = int(time.mktime(time.strptime(str(begin_time), '%Y-%m-%d')))
        end_time = today + datetime.timedelta(days=1)
        end_time_stamp = int(time.mktime(time.strptime(str(end_time), '%Y-%m-%d'))) - 1
        return begin_time_stamp, end_time_stamp

    @classmethod
    def get_now_timestamp(cls) -> int:
        '''
        获取当前时间点的时间戳
        :return:
        '''
        millis = int(round(time.time()) * 1000)
        return millis
