# -*- encoding: utf-8 -*-
"""
@File    : Query.py
@Time    : 2020/5/4 22:15
@Author  : LYX
@describe : 
"""
from sqlalchemy import and_

from app.libs.result_tools.error_code import DBError, ParameterFormatError


class BaseQuery(object):
    """
    数据库操作
    """
    __model__ = None

    def _find_all(self, args, by):
        """
        单表服务-数据库实现条件查询
        """
        return self.__model__.query.filter(*args).order_by(*by).all()

    def _find_by_page(self, page, size, query, by):
        """
        单表服务-数据库实现条件分页查询
        """
        # 使用slice(偏移量，取出量)函数实现分页
        # base = self.__model__.query.filter(*query).order_by(*by)
        # cnt = base.count()
        # data = base.slice(page * size, (page + 1) * size).all()

        # 使用paginate(偏移量，取出量)函数实现分页
        try:
            paginate = self.__model__.query.order_by(*by).filter(*query).paginate(page, size, error_out=True)
        except Exception:
            raise ParameterFormatError(msg="请查看页码和页面大小参数是否正确")
        return paginate

    def _find_by_id(self, key):
        """
        单表服务-数据库通过id查询记录
        """
        return self.__model__.query.filter(and_(self.__model__.isDel == 0, self.__model__.id == key)).first_or_404()

    def _create(self, models):
        """
        单表服务-数据库新增单条或多条数据
        :param models:
        :type models:
        """
        for model in models:
            try:
                model.add()
            except Exception:
                raise DBError()

    def _update(self, models):
        """
        单表服务-数据库更新单条或多条数据
        :param models:
        :type models:
        """
        for model in models:
            try:
                model.update()
            except Exception:
                raise DBError()

    def _delete(self, models):
        """
        单表服务-数据库删除单条或多条数据
        :param models:
        :type models:
        """
        for model in models:
            model.isDel = 1
            try:
                model.update()
            except Exception:
                raise DBError()
