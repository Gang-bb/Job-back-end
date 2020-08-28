# encoding: utf-8
from flask import request
from flask_restplus import Namespace, Resource, reqparse, fields
from sqlalchemy.sql.elements import and_

from app.libs.auth_tools.token_auth import login_required
from app.libs.result_tools.error_code import NoNumberError, HaveSignError
from app.libs.result_tools.result_todict import queryToDict
from app.libs.result_tools.success import make_result
from app.libs.time_tools.gettime import get_from_timestamp
from app.models import Job, Job_Signup, Search, Company, Student
from app.parses.jobParses import JobParse
from exit import db

api = Namespace('job', description='招聘工作相关接口')
job_parser = api.parser()
job_parser.add_argument('Authorization', type=str, help='id', required=True)
job_parser.add_argument('token', type=str, help='token', location='headers', required=True)

fields = api.model('MyModel', {
    'name': fields.String(description='The name', required=True),
    'type': fields.String(description='The object type', enum=['A', 'B']),
    'age': fields.Integer(min=0),
})


@api.route('/jobs', doc={"description": "获取所有可报名工作"})
class GetJobsView(Resource):

    def get(self):
        """获取所有可报名工作"""
        # id = JobParse().get_result().id
        jobs = Job.query.filter(and_(Job.isDel == 0, Job.recruitNum > Job.signNum, Job.status == 2)).all()
        # jobs = Job.query.filter(Job.isDel == 0).all()
        return make_result(jobs), 200


@api.route('/jobs_admin', doc={"description": "管理员获取所有工作"})
class AJobsView(Resource):
    def get(self):
        """管理员获取所有工作"""
        jobs = Job.query.filter(Job.isDel == 0).order_by(Job.id.desc()).all()
        newRes = queryToDict(jobs)
        res1 = [[], [], []]
        for res in newRes:
            res['creatTime'] = get_from_timestamp(res['creatTime'])
            res1[0] = newRes
            if res['status'] == 1:
                res1[1].append(res)
            if res['status'] != 1:
                res1[2].append(res)
        return res1, 200


@api.route('/', doc={"description": "根据ID获取工作"})
class GetJobView(Resource):
    @api.expect(job_parser)
    def get(self):
        """根据ID获取工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int, location='values')
        args = parser.parse_args()
        print(args['id'])
        job = Job.query.filter_by(id=args['id']).first_or_404()
        return make_result(job), 200


@api.route('/signup', doc={"description": "报名工作"})
class SignUpJobView(Resource):
    def post(self):
        """报名工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('userId', type=int)
        parser.add_argument('jobId', type=int)
        parser.add_argument('message', type=str)
        args = parser.parse_args()

        if Job.query.filter(and_(Job.id == args['jobId'], Job.recruitNum <= Job.signNum)).first():
            raise NoNumberError()
        elif Job_Signup.query.filter(
                and_(Job_Signup.jobId == args['jobId'], Job_Signup.userId == args['userId'])).first():
            raise HaveSignError()
        else:
            stu = Student.query.filter(and_(Student.isDel == 0, Student.uId == args['userId'])).first_or_404()
            form = Job_Signup()
            form.userId = args['userId']
            form.stuId = stu.id
            form.jobId = args['jobId']
            form.message = args['message']
            form.add()

            job = Job.query.filter_by(id=args['jobId']).first_or_404()
            job.signNum += 1
            job.update()
        return {"msg": "报名成功"}, 200


@api.route('/hot', doc={"description": "获取热门搜索"})
class GetHotView(Resource):
    def get(self):
        """获取热门搜索"""
        hot = Search.query.filter(Search.isDel == 0).all()
        return make_result(hot), 200


search_parser = api.parser()
search_parser.add_argument('key', type=str, help='key')


@api.route('/search', doc={"description": "搜索工作"})
class SearchJobView(Resource):
    @api.expect(search_parser, validate=False)
    def get(self):
        """搜索工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('key', type=str, location='values')
        parser.add_argument('type', type=int, location='values')
        args = parser.parse_args()
        if args['key'] is None:
            args['key'] = ""
        jobs = Job.query.filter(and_(Job.isDel == 0, Job.tittle.like('%' + args['key'] + '%'))).all()
        if jobs is None:
            jobs = Job.query.filter(and_(Job.isDel == 0, Job.recruitNum > Job.signNum)).all()
        if args.type == 1:
            newjobs = queryToDict(jobs)
            res = [[], [], [], []]
            for job in newjobs:
                job['creatTime'] = get_from_timestamp(job['creatTime'])
                res[0] = newjobs
                for i in range(3):
                    if job['status'] == i + 1:
                        res[i + 1].append(job)
            return res, 200
        return make_result(jobs), 200


mysign_parser = api.parser()
mysign_parser.add_argument('useId', type=int, help='useId')


@api.route('/mysign', doc={"description": "查看我的申请"})
class MySignUpView(Resource):
    @api.expect(mysign_parser)
    def get(self):
        """查看我的申请数字"""
        parser = reqparse.RequestParser()
        parser.add_argument('useId', type=int, location='values')
        args = parser.parse_args()
        res = Job_Signup.query.filter(and_(Job_Signup.isDel == 0, Job_Signup.userId == args['useId'])).all()
        return make_result(res), 200


@api.route('/mysign-list', doc={"description": "学生查看我的申请列表"})
class MySignUpListView(Resource):
    @api.expect(mysign_parser)
    def get(self):
        """学生查看我的申请列表"""
        parser = reqparse.RequestParser()
        parser.add_argument('useId', type=int, location='values')
        args = parser.parse_args()
        res = db.session.query(Job.id, Job.tittle, Job.place, Job.reward, Job_Signup.status). \
            filter(Job.isDel == 0). \
            filter(Job_Signup.jobId == Job.id). \
            filter(and_(Job_Signup.isDel == 0, Job_Signup.userId == args['useId'])). \
            all()
        return make_result(res), 200


mysignList_parser = api.parser()
mysignList_parser.add_argument('useId', type=int, help='useId')
mysignList_parser.add_argument('jobId', type=int, help='jobId')


@api.route('/mysign-detail', doc={"description": "学生查看我的申请详情"})
class MySignUpDetailView(Resource):
    @api.expect(mysignList_parser)
    def get(self):
        """查看我的申请详情"""
        parser = reqparse.RequestParser()
        parser.add_argument('useId', type=int, location='values')
        parser.add_argument('jobId', type=int, location='values')
        args = parser.parse_args()
        res = db.session.query(Job.id, Job.tittle, Job.place, Job.reward, Job_Signup.status). \
            filter(Job.isDel == 0). \
            filter(and_(Job_Signup.jobId == Job.id, Job_Signup.jobId == args['jobId'])). \
            filter(and_(Job_Signup.isDel == 0, Job_Signup.userId == args['useId'])). \
            all()
        return make_result(res), 200


@api.route('/mysign-com', doc={"description": "商家查看申请我工作的学生"})
class MySignUpDetailView(Resource):
    @api.expect(mysignList_parser)
    def get(self):
        """查看申请我工作的学生"""
        parser = reqparse.RequestParser()
        parser.add_argument('useId', type=int, location='values')
        args = parser.parse_args()
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['useId'])).first_or_404()
        resForm = db.session.query(Job_Signup.creatTime, Job_Signup.status, Job.startTime, Job.endTime, Job.tittle,
                                   Job.id.label("jid"), Student.sname, Student.uId.label("uid")). \
            join(Job, Job_Signup.jobId == Job.id). \
            join(Student, Job_Signup.stuId == Student.id). \
            filter(Job.cId == com.id).order_by(Job_Signup.id.desc()).all()
        newRes = queryToDict(resForm)
        res1 = [[], [], []]
        for res in newRes:
            res['creatTime'] = get_from_timestamp(res['creatTime'])
            res1[0] = newRes
            if res['status'] == 1:
                res1[1].append(res)
            if res['status'] != 1:
                res1[2].append(res)
        return res1, 200


@api.route('/release', doc={"description": "商家发布工作"})
class GetEduView(Resource):
    def post(self):
        """商家发布工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('data', type=dict)
        args = parser.parse_args()
        print(request.json)
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['id'])).first_or_404()
        job = Job()
        for key in args.data:
            if key == 'swelfare':
                swelfare = args.data['swelfare']
                for key2 in swelfare:
                    setattr(job, key2, swelfare[key2])
            else:
                setattr(job, key, args.data[key])
        job.cId = com.id
        job.fromCompany = com.cname
        job.add()
        return {}, 200


@api.route('/myjob', doc={"description": "商家查看我发布的所有工作"})
class MySignUpDetailView(Resource):
    @api.expect(mysignList_parser)
    def get(self):
        """商家查看我发布的所有工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int, location='values')
        args = parser.parse_args()
        com = Company.query.filter(and_(Company.isDel == 0, Company.uId == args['uid'])).first_or_404()
        jobs = Job.query.filter(and_(Job.isDel == 0, Job.cId == com.id)). \
            with_entities(Job.id, Job.tittle, Job.place, Job.creatTime, Job.status).all()
        newjobs = queryToDict(jobs)
        res = [[], [], [], []]
        for job in newjobs:
            job['creatTime'] = get_from_timestamp(job['creatTime'])
            res[0] = newjobs
            for i in range(3):
                if job['status'] == i + 1:
                    res[i + 1].append(job)
        return res, 200


@api.route('/end', doc={"description": "结束工作"})
class EndJobView(Resource):
    @api.expect(job_parser)
    def post(self):
        """结束工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('type', type=int)
        args = parser.parse_args()
        print(args)
        if args.type == 1:
            sign = Job_Signup.query.filter_by(jobId=args['id']).first_or_404()
            if sign.status == 3:
                return {"code": 111,
                        "msg": "您已经操作过了哦"}
            sign.status = 3
            sign.update()
            return {"code": 120,
                    "msg": "操作成功"}
        job = Job.query.filter_by(id=args['id']).first_or_404()
        sign = Job_Signup.query.filter_by(jobId=args['id']).first_or_404()
        # 有时间还要把学生申请表的所有状态改为4
        sign.status = 4
        sign.update()
        job.status = 3
        job.update()
        return {}, 200


def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


@api.route('/vstu', doc={"description": "审核学生"})
class VStuView(Resource):
    @api.expect(job_parser)
    def post(self):
        """审核学生"""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=int)
        parser.add_argument('jid', type=int)
        parser.add_argument('status', type=int)
        args = parser.parse_args()
        print(args)
        form = Job_Signup.query.filter(and_(Job_Signup.jobId == args['jid'], Job_Signup.userId == args['uid'])) \
            .first_or_404()
        print(form)
        form.status = args['status']
        form.update()
        return {}, 200


@api.route('/job_v', doc={"description": "审核工作"})
class VJobView(Resource):
    def post(self):
        """审核工作"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('status', type=int)
        args = parser.parse_args()
        print(args)
        job = Job.query.filter_by(id=args['id']).first_or_404()
        job.status = args.status
        job.update()
        return make_result(job), 200
