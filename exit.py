# encoding: utf-8
"""
@author: lyx
@time: 2020/1/21 22:03
@file: exit.py 
"""

from flask_sqlalchemy import BaseQuery, SQLAlchemy

from app.libs.result_tools.error_code import NotFound


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'isDel' not in kwargs.keys():
            kwargs['isDel'] = 0
        return super(Query, self).filter_by(**kwargs)

    # 返回指定主键对应的行，如不存在，返回404
    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            raise NotFound()
        return rv

    # 返回查询的第一个结果，如果未查到，返回404
    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)
