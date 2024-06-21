import time
import datetime


class DateUtil(object):

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
