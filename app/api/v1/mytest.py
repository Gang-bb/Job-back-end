# encoding: utf-8
from flask import request
from flask_restplus import Namespace, Resource, reqparse, fields
from flask_restplus.fields import String
from sqlalchemy import and_

from app.libs.result_tools.success import make_result
from app.models import Job, Job_Signup, Student
from exit import db

api = Namespace('mytest', description='我自己的各种测试')

test_parser = api.parser()
test_parser.add_argument('data', type=dict, location='json')

# resource_fields = api.model('Resource', {
#     'name': fields.String,
# })

base_fields = api.model('Resource', {
    'key': fields.String(description='使用json方式传递 与以下参数方式 相等 {"ge_id": 0, "eq_id": 0 }'),
})

fields11 = api.model('MyModel', {
    'name': fields.String(description='The name', required=True),
    'type': fields.String(description='The object type', enum=['A', 'B']),
    'age': fields.Integer(min=0),
})
name = 'job'
__type__ = String
items = {
    name: fields.String,
}
job = api.model(name, items)

api.add_model('123', fields11)

test_parser = api.parser()
test_parser.add_argument('data', type=dict, location='json', help='使用json方式传递 与以下参数方式'
                                                                  ' 相等 {"ge_id": 0, "eq_id": 0 }')


@api.expect(test_parser)
@api.route('/dict', doc={"description": "请求发送字典model样例"})
class DictView(Resource):
    @api.expect(job)
    # @api.expect(resource_fields)
    # @api.doc(model=fields)
    # @api.doc(params={'id': 'An ID'})
    def post(self):
        """请求发送字典model样例"""
        parser = reqparse.RequestParser()
        parser.add_argument('payload', location='form')
        args = parser.parse_args()
        a = request.json
        print(args)
        print(a)
        return a, 200

# @api.route('/dict', doc={"description": "测试"})
# class DictView(Resource):
#     def post(self):
#         """请求发送字典model样例"""
#
#         return {}, 200
