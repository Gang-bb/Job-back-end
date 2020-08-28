# encoding: utf-8
"""
@author: lyx
@time: 2020/1/27 11:35
@file: gettime.py
"""

from datetime import *
import time


# 1.获取当前时间的时间戳 输出示例 1585552473
def get_timestamp_now():
    return int(datetime.now().timestamp())


# 2.转换时间戳为%Y-%m-%d %H:%M:%S 格式时间  输出示例 2020-03-30 15:14:33
def get_from_timestamp(timestamp):
    if isinstance(timestamp, int):
        dateArray = datetime.fromtimestamp(timestamp)
        otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
        return otherStyleTime
    return timestamp


# 3.获取当前日期%Y-%m-%d 输出示例 2020-03-30
def get_day_now():
    return date.today()


# 4.获取前n天日期%Y-%m-%d 输出示例 2020-03-20
def get_day_before(n):
    return (date.today() + timedelta(days=-n)).strftime("%Y-%m-%d")


# 5.获取后n天的日期%Y-%m-%d 输出示例 2020-04-09
def get_day_after(n):
    return (date.today() + timedelta(days=n)).strftime("%Y-%m-%d")


# 6.获取当前日期 x年x月x日 输出示例 2020年03月30日
def get_day_now_zh_CN():
    return datetime.now().strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')


# 获得当前微秒级时间戳
def get_microsecond_timestamp():
    return round(time.time() * 1000000)
