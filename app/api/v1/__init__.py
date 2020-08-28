# encoding: utf-8
"""
@file: __init__.py.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/16 23:20   lyx        1.0         None

"""
from flask import Blueprint
from flask_restplus import Api
from app.api.v1.job import api as job_api
from app.api.v1.resume import api as resume_api
from app.api.v1.user import api as user_api
from app.api.v1.login import api as login_api
from app.api.v1.company import api as company_api
from app.api.v1.mytest import api as mytest_api
from app.server.Server import api as base

bp_v1 = Blueprint('v1', __name__)

api = Api(bp_v1,
          title='大学生兼职系统的api',
          version='1.0',
          description='大学生兼职系统系统API的v1版本')


api.add_namespace(job_api)
api.add_namespace(resume_api)
api.add_namespace(user_api)
api.add_namespace(login_api)
api.add_namespace(company_api)
api.add_namespace(mytest_api)
api.add_namespace(base)


#     """
#    用工厂模式
#     """
# def register_views(bp):
#     api = Api(bp,
#               title='大学生兼职系统系统的api',
#               version='1.0',
#               description='大学生兼职系统API的v1版本')
#
#     api.add_namespace(job)
#     api.add_namespace(job2)
#
#
# def create_blueprint_v1():
#     """
#     注册蓝图->v1版本
#     """
#     bp_v1 = Blueprint('v1', __name__)
#     register_views(bp_v1)
#     return bp_v1
