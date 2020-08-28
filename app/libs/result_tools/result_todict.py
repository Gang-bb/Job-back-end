# encoding: utf-8
"""
@file: result_todict.py
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/1 17:29   lyx        1.0         None

"""
from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from datetime import date, time
from flask_sqlalchemy import Model
from sqlalchemy import DateTime, Numeric, Date, Time, BigInteger, Integer  # 有时又是DateTime

from app.libs.time_tools.gettime import get_from_timestamp


def queryToDict(models):
    if isinstance(models, list):
        # 如果是空的返回空list
        if len(models) == 0:
            return []
        if isinstance(models[0], Model):
            lst = []
            for model in models:
                gen = model_to_dict(model)
                dit = dict((g[0], g[1]) for g in gen)
                lst.append(dit)
            return lst
        else:
            res = result_to_dict(models)
            return res
    else:
        if isinstance(models, Model):
            gen = model_to_dict(models)
            dit = dict((g[0], g[1]) for g in gen)
            return dit
        else:
            res = dict(zip(models.keys(), models))
            find_datetime(res)
            return res


# 当结果为result对象列表时，result有key()方法
def result_to_dict(results):
    res = [dict(zip(r.keys(), r)) for r in results]
    # 这里r为一个字典，对象传递直接改变字典属性
    for r in res:
        find_datetime(r)
    return res


def model_to_dict(model):  # 这段来自于参考资源
    # 遍历每个字段
    for col in model.__table__.columns:
        # print(type(col.name))
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(model, col.name))
        elif isinstance(col.type, Numeric):
            value = float(getattr(model, col.name))
        # 长ID变成str返回
        elif isinstance(col.type, BigInteger):
            value = str(getattr(model, col.name))
        # 整形时间戳转成%Y-%m-%d %H:%M:%S 格式时间
        elif col.name == 'creatTime' or col.name == 'reviseTime':
            value = get_from_timestamp(getattr(model, col.name))
        else:
            value = getattr(model, col.name)
        yield (col.name, value)


def find_datetime(value):
    for v in value:
        if isinstance(value[v], cdatetime):
            value[v] = convert_datetime(value[v])  # 这里原理类似，修改的字典对象，不用返回即可修改


def convert_datetime(value):
    if value:
        if isinstance(value, (cdatetime, DateTime)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(value, (date, Date)):
            return value.strftime("%Y-%m-%d")
        elif isinstance(value, (Time, time)):
            return value.strftime("%H:%M:%S")
    else:
        return ""
