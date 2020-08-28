# encoding: utf-8
"""
@file: __init__.py.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 23:16   lyx        1.0         None

"""
from app.api.v1 import bp_v1
from flask import Blueprint
route_index = Blueprint("route_index", __name__)


@route_index.route('/')
def index():
    return "大学生兼职系统系统系统API swagger测试地址:  http://127.0.0.1:8888/v1 "


def register_blueprints(app):
    # 注册版本
    app.register_blueprint(bp_v1, url_prefix='/v1')
    app.register_blueprint(route_index)
