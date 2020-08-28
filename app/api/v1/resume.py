# encoding: utf-8
from flask_restplus import Namespace, Resource, reqparse
from sqlalchemy import and_

from app.libs.result_tools.result_todict import queryToDict
from app.libs.result_tools.success import make_result
from app.models import EduResume, WorkResume, OtherResume

api = Namespace('resume', description='简历相关接口')

uId_parser = api.parser()
uId_parser.add_argument('id', type=int, help='用户id', required=True)


@api.route('/edus', doc={"description": "获取教育经历"})
class GetEduView(Resource):
    @api.expect(uId_parser)
    def get(self):
        """获取教育经历"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        args = parser.parse_args()
        edus = EduResume.query.filter(and_(EduResume.isDel == 0, EduResume.userId == args['id'])).all()
        return make_result(edus), 200


@api.route('/works', doc={"description": "获取工作经历"})
class GetWorkView(Resource):
    @api.expect(uId_parser)
    def get(self):
        """获取工作经历"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        args = parser.parse_args()
        works = WorkResume.query.filter(and_(WorkResume.isDel == 0, WorkResume.userId == args['id'])).all()
        return make_result(works), 200


@api.route('/others', doc={"description": "获取简历其他项"})
class GetOtherView(Resource):
    @api.expect(uId_parser)
    def get(self):
        """获取简历其他项"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        args = parser.parse_args()
        otherInfoList = []
        edus = EduResume.query.filter(and_(EduResume.isDel == 0, EduResume.userId == args['id'])).all()
        otherInfoList = make_item(otherInfoList, '教育经历', queryToDict(edus))
        works = WorkResume.query.filter(and_(WorkResume.isDel == 0, WorkResume.userId == args['id'])).all()
        otherInfoList = make_item(otherInfoList, '工作经历', queryToDict(works))
        others = OtherResume.query.filter(and_(OtherResume.isDel == 0, OtherResume.userId == args['id'])).all()
        otherInfoList = make_item(otherInfoList, '工作期望', queryToDict(others))
        if others and others[0].selfIntroduction:
            otherInfoList = make_item(otherInfoList, '自我评价', others[0].selfIntroduction)
        else:
            otherInfoList = make_item(otherInfoList, '自我评价', [])

        return otherInfoList, 200


def make_item(arr, itemTittle, dataList):
    myarr = arr
    item = {
        "oClass": 'none',
        "itemTittle": itemTittle,
        "experienceList": dataList
    }
    if dataList:
        item['oClass'] = 'item',
    myarr.append(item)
    return myarr


@api.route('/percentage', doc={"description": "获取简历完整百分比"})
class PercentageView(Resource):
    @api.expect(uId_parser)
    def get(self):
        """获取简历完整百分比"""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int, location='values')
        args = parser.parse_args()
        percentage = 0
        w = WorkResume.query.filter(and_(WorkResume.isDel == 0, WorkResume.userId == args['uid'])).first()
        if w:
            percentage = getPercentage(w, percentage)

        o = OtherResume.query.filter(and_(WorkResume.isDel == 0, WorkResume.userId == args['uid'])).first()
        if o:
            percentage = getPercentage(o, percentage)

        e = EduResume.query.filter(and_(WorkResume.isDel == 0, WorkResume.userId == args['uid'])).first()
        if e:
            percentage = getPercentage(e, percentage)
        return {"percentage": percentage}, 200


def getPercentage(data, percentage):
    for key in queryToDict(data):
        if queryToDict(data)[key]:
            percentage += 3.5
    return percentage


@api.route('/add', doc={"description": "添加学生的信息"})
class ModifyResumeView(Resource):
    def post(self):
        """添加公司的信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('data', type=dict)
        parser.add_argument('type', type=int)
        args = parser.parse_args()
        print(args)
        if args.type == 1:
            edu = EduResume()
            setData(edu, args)
        if args.type == 2:
            work = WorkResume()
            setData(work, args)


def setData(new, args):
    for key in args.data:
        setattr(new, key, args.data[key])
        new.add()
    return make_result(), 200


@api.route('/id', doc={"description": "根据ID获取其他项简历"})
class GetIdView(Resource):
    def get(self):
        """根据ID获取其他项简历"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        parser.add_argument('type', type=int, location='values')
        args = parser.parse_args()
        print(args['id'])
        info = {}
        if args['type'] == 1:
            info = EduResume.query.filter_by(id=args['id']). \
                with_entities(EduResume.school, EduResume.major, EduResume.degree, EduResume.startTime,
                              EduResume.endTime, EduResume.experience).first_or_404()
        if args['type'] == 2:
            info = WorkResume.query.filter_by(id=args['id']). \
                with_entities(WorkResume.company, WorkResume.startTime, WorkResume.endTime, WorkResume.experience). \
                first_or_404()
        if args['type'] == 3:
            info = OtherResume.query.filter_by(userId=args['id']).first()
            if info is None:
                return {"code": 10001}
        if args['type'] == 4:
            info = OtherResume.query.filter_by(userId=args['id']).first()
            if info is None:
                return {"code": 10001}
        return make_result(info), 200


@api.route('/modify', doc={"description": "修改学生的信息"})
class ModifyResumeView(Resource):
    def post(self):
        """修改学生的信息"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('data', type=dict)
        parser.add_argument('type', type=int)
        parser.add_argument('self', type=str)
        args = parser.parse_args()
        print(args)
        if args.type == 1:
            edu = EduResume.query.filter_by(id=args['id']).first_or_404()
            modifyData(edu, args)
        if args.type == 2:
            work = WorkResume().query.filter_by(id=args['id']).first_or_404()
            modifyData(work, args)
        if args.type == 3:
            other = OtherResume.query.filter_by(userId=args['id']).first_or_404()
            if other:
                other.selfIntroduction = args.self
                modifyData(other, args)
            if other is None:
                newOther = OtherResume()
                setData(newOther, args)
        if args.type == 4:
            other = OtherResume.query.filter_by(userId=args['id']).first()
            if other:
                other.selfIntroduction = args.self
                other.update()
                make_result(other), 200
            if other is None:
                newOther = OtherResume()
                newOther.selfIntroduction = args.self
                newOther.userId = args.id
                newOther.add()
                make_result(newOther), 200


def modifyData(new, args):
    for key in args.data:
        setattr(new, key, args.data[key])
        new.update()
    return make_result(new), 200
