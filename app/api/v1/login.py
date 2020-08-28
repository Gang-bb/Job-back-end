# encoding: utf-8
from flask_restplus import Namespace, Resource, reqparse

from app.libs.result_tools.error_code import RegisterFailed, LoginError
from app.libs.result_tools.success import make_result
from app.models import User, Company
import requests

api = Namespace('login', path="/", description='登录相关接口')


@api.route('/login', doc={"description": "登录接口"})
class LoginView(Resource):
    # @api.expect(uId_parser)
    def post(self):
        """登录接口"""
        parser = reqparse.RequestParser()
        parser.add_argument('loginName', type=str, required=True)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        data = User.verify(args.loginName, args.password)
        print(data)
        # edus = EduResume.query.filter(and_(EduResume.isDel == 0, EduResume.userId == args['id'])).all()
        return data, 200


@api.route('/login_stu', doc={"description": "学生登录接口"})
class StuLoginView(Resource):
    # @api.expect(uId_parser)
    def post(self):
        """学生登录接口"""
        parser = reqparse.RequestParser()
        parser.add_argument('code', trim=True, type=str)
        args = parser.parse_args()

        # 获取微信小程序所需参数
        appID = 'wx1e6b4b1272d1c0ab'
        appSecret = 'a452e55ca0f5e640024218710a521948'
        code = args.code
        wx_login_api = 'https://api.weixin.qq.com/sns/jscode2session'
        req_params = {
            'appid': appID,
            'secret': appSecret,
            'js_code': code,
            'grant_type': 'authorization_code'
        }
        response_data = requests.get(wx_login_api, params=req_params)  # 向API发起GET请求
        data = response_data.json()
        print(data)
        if 'errcode' in data:
            if data['errcode'] == 40029 or data['errcode'] == 45011 or data['errcode'] == -1:
                raise LoginError(data=data['errmsg'])
            else:
                raise LoginError()
                print(data['errmsg'])
        isExist(data['openid'])
        openid = data['openid']  # 得到用户关于当前小程序的OpenID
        session_key = data['session_key']  # 得到用户关于当前小程序的会话密钥session_key
        user = User.query.filter_by(openId=openid).first_or_404()
        return {"openid": openid,
                "session_key": session_key,
                "uid": user.id}, 200


def isExist(openid):
    user = User.query.filter_by(openId=openid).first()
    if user is None:
        user = User(openId=openid)
        user.add()


@api.route('/register', doc={"description": "注册接口"})
class LoginView(Resource):
    # @api.expect(uId_parser)
    def post(self):
        """注册接口"""
        parser = reqparse.RequestParser()
        parser.add_argument('loginName', type=str, required=True)
        parser.add_argument('password', type=str)
        parser.add_argument('type', type=int)
        args = parser.parse_args()
        if User.query.filter_by(loginName=args.loginName).first():
            raise RegisterFailed()
        user = User()
        user.loginName = args.loginName
        user.password = args.password
        user.type = args.type
        user.add()

        return {}, 200


@api.route('/modify', doc={"description": "修改密码"})
class ModifyView(Resource):
    # @api.expect(uId_parser)
    def post(self):
        """修改密码"""
        parser = reqparse.RequestParser()
        parser.add_argument('uid', type=str, required=True)
        parser.add_argument('password', type=str)
        args = parser.parse_args()
        user = User.query.filter_by(id=args.uid).first_or_404()
        user.password = args.password
        user.update()

        return {}, 200
