# -*- encoding: utf-8 -*-
"""
@File    : get_db_info.py
@Time    : 2020/5/6 14:50
@Author  : LYX
@describe : 
"""
import prettytable
from sqlalchemy import create_engine, MetaData, inspect
from sqlalchemy.ext.automap import automap_base


def get_db_schema(schema_name):
    """
    根据表名，反射出数据库中相应的表
    """
    # 从配置文件中获取
    # ENGINE = create_engine(current_app.config['DB_URI'])
    # DB_NAME = current_app.config['DB_NAME']
    # 建立数据库链接
    ENGINE = create_engine("mysql+mysqlconnector://root:root@localhost:3306/job?charset=utf8")
    DB_NAME = "job"

    metadata = MetaData(bind=ENGINE)
    metadata.reflect(bind=ENGINE, schema=DB_NAME, only=[schema_name])
    Base = automap_base(metadata=metadata)
    Base.prepare()
    schema = getattr(Base.classes, schema_name)
    return schema


def get_primary_key(schema_name):
    """
    根据表名，获取该表主键
    """
    schema = get_db_schema(schema_name)
    primary_key = inspect(schema).primary_key
    # 由于会有多个主键，所以是一个序列。这里我们只有一个主键，所以取第一个，然后拿到名字
    return primary_key[0].name  # id


def get_all_key(schema_name):
    """
    根据表名，获取该表所有字段，返回列表
    """
    schema = get_db_schema(schema_name)
    keys = inspect(schema).c.keys()
    return keys


def get_schema_detail(schema_name):
    """
    根据表名，获取该表详细字段信息
    """
    schema = get_db_schema(schema_name)
    columns = inspect(schema).columns
    return columns


def get_schema_form(schema_name):
    """
    根据表名，获取该表详细表格信息
    """
    schema = get_db_schema(schema_name)
    columns = inspect(schema).columns
    tb = prettytable.PrettyTable()
    tb.field_names = ["字段名", "是否为主键", "字段类型", "是否允许非空", "注释"]
    for col_attr in columns:
        tb.add_row([col_attr.name, col_attr.primary_key, str(col_attr.type), col_attr.nullable, col_attr.comment])
    tb = "数据表信息为：\n" + str(tb)
    return tb


def get_keys_type_dict(schema_name):
    """
    根据表名，获取该表字段和其对应类型，以字典形式返回（去除base表中的基础字段）
    """
    columns = get_schema_detail(schema_name)
    type_dict = dict()
    for col_attr in columns:
        if col_attr.name not in ['id', 'creator', 'creatTime', 'reviseTime', 'reviser', 'isDel']:
            type_dict[col_attr.name] = str(col_attr.type)
    return type_dict

