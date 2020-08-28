# encoding: utf-8
# encoding: utf-8
from flask import request
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    # 默认为未知错误
    code = 500
    data = {
        'code': 50000,
        'msg': "服务器未知错误"
    }

    def __init__(self, code=None, msg=None):
        if code:
            self.code = code
        if msg:
            self.data['msg'] = msg
        self.data['request'] = request.method + ' ' + self.get_url_no_param()
        super(APIException, self).__init__()

    @staticmethod
    def get_url_no_param():
        # 拿到接口的完整地址去掉问号
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]