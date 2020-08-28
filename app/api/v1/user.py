# encoding: utf-8
from flask_restplus import Namespace, Resource, reqparse
from sqlalchemy import and_

from app.libs.result_tools.success import make_result
from app.models import User, Student

api = Namespace('user', description='用户相关接口')

user_parser = api.parser()
user_parser.add_argument('id', type=int, help='id', required=True)


@api.route('/', doc={"description": "编辑简历页 根据ID获取用户信息"})
class GetResumesView(Resource):
    @api.expect(user_parser)
    def get(self):
        """编辑简历页 根据ID获取用户信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        args = parser.parse_args()
        stu = Student.query.filter_by(uId=args['id']).first()
        if stu:
            return make_result(stu), 200
        if stu is None:
            return make_result(), 200


@api.route('/modify', doc={"description": "修改学生的信息"})
class ModifyStuView(Resource):
    def post(self):
        """修改公司的信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('data', type=dict)
        args = parser.parse_args()
        print(args.data)
        stu = Student.query.filter(and_(Student.isDel == 0, Student.uId == args['id'])).first_or_404()
        for key in args.data:
            setattr(stu, key, args.data[key])
        stu.update()
        return make_result(stu), 200
