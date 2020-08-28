# -*- encoding: utf-8 -*-
"""
@File    : Parse.py
@Time    : 2020/5/3 18:46
@Author  : LYX
@describe : 
"""
from flask import request
from sqlalchemy import and_
from app.libs.result_tools.error_code import ParameterFormatError, NoDataError
from app.parses.baseParses import PageParse


class BaseParse(object):
    """
        解析参数
    """
    __model__ = None
    __request__ = request
    # frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
    by = frozenset(['by'])
    query = frozenset(['gt', 'ge', 'lt', 'le', 'ne', 'eq', 'ic', 'ni', 'in'])

    def __new__(cls, *args, **kwargs):
        cls._operator_funcs = {
            'gt': cls.__gt_model,
            'ge': cls.__ge_model,
            'lt': cls.__lt_model,
            'le': cls.__le_model,
            'ne': cls.__ne_model,
            'eq': cls.__eq_model,
            'ic': cls.__ic_model,
            'ni': cls.__ni_model,
            'by': cls.__by_model,
            'in': cls.__in_model,
        }
        return super().__new__(cls)

    def _parse_page_size(self):
        """
        获取页码和获取每页数据量
        :return: page 页码
             page_size 每页数据量
        """
        # default_page = current_app.config['DEFAULT_PAGE_INDEX']
        # default_size = current_app.config['DEFAULT_PAGE_SIZE']
        default_page = PageParse().get_result().current_page or 1
        default_size = PageParse().get_result().page_size or 10
        page = self.__request__.args.get("page", default_page)
        page_size = self.__request__.args.get("size", default_size)
        page = int(page)
        page_size = int(page_size)
        return page, page_size

    def _parse_query_field(self):
        """
        解析查询字段
        :return: query_field 查询字段
                 by_field 排序字段
        """
        # 从请求的 the query string 中获取查询条件
        args = self.__request__.args.to_dict()
        query_field = list()
        # 默认过滤软删除的数据
        query_field.append(getattr(self.__model__, 'isDel') == 0)
        by_field = list()
        for query_key, query_value in args.items():
            # 裁剪参数 key_split 为一个列表 例：['gt', 'id']
            key_split = query_key.split('_', 1)
            # 如果不为指定格式抛出错误
            if len(key_split) != 2:
                raise ParameterFormatError()
            operator, key = key_split
            # 判断该model中是否有该字段, 无则抛出异常
            if not self._check_key(key=key):
                continue
            # 根据前缀添加查询条件
            if operator in self.query:
                data = self._operator_funcs[operator](self, key=key, value=query_value)
                # 如果有要求isDel字段，则改变默认过滤软删除
                if key == 'isDel':
                    query_field[0] = data
                    continue
                print(data)
                query_field.append(data)
            elif operator in self.by:
                data = self._operator_funcs[operator](self, key=key, value=query_value)
                by_field.append(data)
        return query_field, by_field

    def _get_data(self):
        """
        获取请求中的data
        """
        # 获取要操作的数据
        data = request.get_json(force=True)['data'] if 'data' in request.json else request.get_json(force=True)
        if not data:
            raise NoDataError()
        if isinstance(data, dict):
            data = [data]
        return data

    def _match_model(self, index, fail_count, item, model, models, fail_msg):
        """
        匹配item与数据库中的段
        """
        is_no_fail = True
        for k, v in item.items():
            # 判断item的每个字段，只修改model中与之能对应的字段
            if hasattr(self.__model__, k):
                setattr(model, k, v)
            else:
                is_no_fail = False
                fail_msg += f"第{index}项:" \
                                f"{self.__model__.__tablename__}表中无{k}字段，操作失败。" + " "
                fail_count += 1
                break
        # 如果没有任何错误添加该model
        if is_no_fail:
            models.append(model)
        return models, fail_count, fail_msg

    def _make_data_to_model(self, data):
        """
        从请求的data中筛选出可进行数据库操作的model
        :return: fail_count, fail_msg, models
        :rtype: str, str, list
        """
        fail_msg = ''
        fail_count = 0
        models = list()
        total_count = len(data)
        # 新增时
        if request.method == 'POST':
            for item in data:
                # 去掉item中的id项
                if 'id' in item:
                    del item['id']
                model = self.__model__()
                models, fail_count, fail_msg = self._match_model(data.index(item) + 1, fail_count, item, model,
                                                                 models, fail_msg)
        # 修改和删除时
        elif request.method in ['PUT', 'DELETE']:
            for item in data:
                # 判断item是否有id字段
                if 'id' in item:
                    model = self.__model__.query.filter(and_(self.__model__.isDel == 0,
                                                             self.__model__.id == item['id'])).first()
                else:
                    fail_msg += f"第{data.index(item) + 1}项:没有id字段，操作失败。" + " "
                    fail_count += 1
                    continue
                # 判断item的id是否匹配到数据库记录
                if model:
                    # 如果是删除，就直接返回model
                    if request.method == 'DELETE':
                        models.append(model)
                        continue
                    # 修改
                    else:
                        models, fail_count, fail_msg = self._match_model(data.index(item) + 1, fail_count, item, model,
                                                                         models, fail_msg)
                # 如果匹配不到model
                elif not model:
                    fail_msg += f"第{data.index(item) + 1}项:id没有匹配数据库中记录，操作失败。" + " "
                    fail_count += 1
                    continue
        return total_count, fail_count, fail_msg, models

    def _check_key(self, key):
        """
        检查model是否存在key中的字段
        :param key:
        :return:
        """
        if hasattr(self.__model__, key):
            return True
        else:
            return False

    def __gt_model(self, key, value):
        """
        大于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) > value

    def __ge_model(self, key, value):
        """
        大于等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) >= value

    def __lt_model(self, key, value):
        """
        小于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) < value

    def __le_model(self, key, value):
        """
        小于等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) <= value

    def __eq_model(self, key, value):
        """
        等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) == value

    def __ne_model(self, key, value):
        """
        不等于
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key) != value

    def __ic_model(self, key, value):
        """
        包含
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key).like('%{}%'.format(value))

    def __ni_model(self, key, value):
        """
        不包含
        :param key:
        :param value:
        :return:
        """
        return getattr(self.__model__, key).notlike('%{}%'.format(value))

    def __by_model(self, key, value):
        """
        :param key:
        :param value: 0:倒序,1:正序
        :return:
        """
        try:
            value = int(value)
        except ValueError as e:
            return getattr(self.__model__, key).asc()
        else:
            if value == 1:
                return getattr(self.__model__, key).asc()
            elif value == 0:
                return getattr(self.__model__, key).desc()
            else:
                return getattr(self.__model__, key).asc()

    def __in_model(self, key, value):
        """
        查询多个相同字段的值
        :param key:
        :param value:
        :return:
        """
        value = value.split('|')
        return getattr(self.__model__, key).in_(value)
