from app.libs.result_tools.error import APIException


class NotFound(APIException):
    code = 404
    data = {
        'code': 40001,
        'msg': "数据库找不到该资源"
    }


class ParseError(APIException):
    code = 400
    data = {
        'code': 40002,
        'msg': "请求参数验证失败"
    }


class NoNumberError(APIException):
    code = 400
    data = {
        'code': 40003,
        'msg': "报名失败，该工作名额已满"
    }


class HaveSignError(APIException):
    code = 400
    data = {
        'code': 40004,
        'msg': "报名失败，该用户已报名过该工作"
    }


class AuthFailed(APIException):
    code = 403
    data = {
        'code': 40005,
        'msg': "密码验证错误"
    }


class RegisterFailed(APIException):
    code = 400
    data = {
        'code': 40006,
        'msg': "该用户已经注册过了哦"
    }


class LoginError(APIException):
    code = 403
    data = {
        'code': 40007,
        'msg': "学生端登录错误"
    }


class ModelKeyError(APIException):
    code = 400
    data = {
        'code': 40008,
        'msg': "单表服务异常-该model中无该字段"
    }


class ParameterFormatError(APIException):
    code = 400
    data = {
        'code': 40009,
        'msg': "单表服务异常-请求参数格式错误"
    }


class NoDataError(APIException):
    code = 400
    data = {
        'code': 400010,
        'msg': "单表服务异常-没有要操作的数据"
    }


class DBError(APIException):
    code = 400
    data = {
        'code': 400011,
        'msg': "数据库操作失败，请联系管理员"
    }
