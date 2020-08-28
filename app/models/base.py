# encoding: utf-8
"""
@author: lyx
@time: 2020/1/26 16:09
@file: baseform.py
"""

from app.libs.time_tools.gettime import get_timestamp_now, get_microsecond_timestamp
from exit import db


class Base(db.Model):
    # 表明这个是基类，创建表时不会被创建
    __abstract__ = True
    id = db.Column('id', db.BigInteger, primary_key=True)
    creator = db.Column(db.BigInteger, default=0, comment='创建人')
    creatTime = db.Column(db.Integer, default=get_timestamp_now(), comment='创建时间')
    reviseTime = db.Column(db.Integer, default=get_timestamp_now(), onupdate=get_timestamp_now(), comment='更新时间')
    reviser = db.Column(db.BigInteger, default=0, comment='修改人')
    isDel = db.Column(db.SmallInteger, default=0, comment='是否删除 1-删除 0-未删除')

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        self.isDel = 1
        self.update(self)


def getId(tabnum):
    # 每个表id=表号+当前微秒级别的时间戳
    formId = tabnum + str(get_microsecond_timestamp())
    return int(formId)
