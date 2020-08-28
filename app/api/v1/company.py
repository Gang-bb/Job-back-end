# encoding: utf-8
from flask_restplus import Namespace, Resource, reqparse
from sqlalchemy import and_

from app.libs.result_tools.result_todict import queryToDict
from app.libs.result_tools.success import make_result
from app.libs.time_tools.gettime import get_from_timestamp
from app.models import Company, ComSign
from exit import db

api = Namespace('company', description='公司信息相关接口')

uId_parser = api.parser()
uId_parser.add_argument('id', type=int, help='id', required=True)


@api.route('', doc={"description": "根据ID获取公司信息"})
class GetEduView(Resource):
    @api.expect(uId_parser)
    def get(self):
        """根据ID获取公司信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        parser.add_argument('type', type=int, location='values')
        args = parser.parse_args()
        if args.type == 1:
            com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['id'])). \
                with_entities(Company.cname, Company.cplace, Company.cphone, Company.cemail, Company.ctype,
                              Company.cinfo,Company.pname, Company.pphone, Company.isVerify).first()
            return make_result(com, 20002), 200
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['id'])). \
            with_entities(Company.cname, Company.cplace, Company.cphone, Company.cemail, Company.ctype, Company.cinfo,
                          Company.pname, Company.pphone).first()
        if com:
            return make_result(com, 20002), 200
        if com is None:
            newCom = Company()
            newCom.uId = args['id']
            newCom.isVerify = 0
            newCom.add()
            return {"code": 2001}, 200


@api.route('', doc={"description": "修改公司的信息"})
class ModifyComView(Resource):
    @api.expect(uId_parser)
    def post(self):
        """修改公司的信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('data', type=dict)
        args = parser.parse_args()
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['id'])).first_or_404()
        for key in args.data:
            setattr(com, key, args.data[key])
        com.update()
        return make_result(com), 200


@api.route('/com_sign', doc={"description": "公司提交资料审核"})
class SignComView(Resource):
    @api.expect(uId_parser)
    def post(self):
        """公司提交资料审核"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['id'])).first_or_404()
        form = ComSign()
        form.uId = args['id']
        form.cId = com.id
        form.add()
        return make_result(com), 200


@api.route('/sign_status', doc={"description": "判断是否有申请过"})
class SignComView(Resource):
    @api.expect(uId_parser)
    def get(self):
        """判断是否有申请过"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        form = ComSign.query.filter(and_(ComSign.isDel == 0, ComSign.uId == args['id'])).first()
        if form:
            if form.isVerify == 1:
                return {"code": 100,
                        "msg": "等待审核中"}
            if form.isVerify == 2:
                return {"code": 101,
                        "msg": "通过申请"}
            if form.isVerify == 3:
                return {"code": 102,
                        "msg": "不通过审核"}
        if form is None:
            return {"code": 103,
                    "msg": "未提交过申请"}


@api.route('/verify-com', doc={"description": "管理员查看待审核的企业"})
class ComVerifyView(Resource):
    def get(self):
        """管理员查看待审核的企业"""
        parser = reqparse.RequestParser()
        parser.add_argument('useId', type=int, location='values')
        args = parser.parse_args()
        forms = db.session.query(ComSign.id, ComSign.creatTime, ComSign.uId, ComSign.cId, ComSign.isVerify,
                                 Company.cname). \
            filter(ComSign.isDel == 0). \
            filter(ComSign.cId == Company.id). \
            all()
        newRes = queryToDict(forms)
        print(newRes)
        res1 = [[], [], []]
        for res in newRes:
            res['creatTime'] = get_from_timestamp(res['creatTime'])
            res1[0] = newRes
            if res['isVerify'] == 1:
                res1[1].append(res)
            if res['isVerify'] != 1:
                res1[2].append(res)
        return res1, 200


@api.route('/do-verify', doc={"description": "审核公司信息"})
class VStuView(Resource):
    def post(self):
        """审核公司信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int)
        parser.add_argument('isVerify', type=int)
        args = parser.parse_args()
        print(args)
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['uid'])).first_or_404()
        form = ComSign.query.filter(and_(ComSign.isDel == 0, ComSign.uId == args['uid'])).first_or_404()
        com.isVerify = args['isVerify']
        form.isVerify = args['isVerify']
        form.update()
        com.update()
        return make_result(com), 200
