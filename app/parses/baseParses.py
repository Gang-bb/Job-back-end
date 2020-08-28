# encoding: utf-8
"""
@file: baseParses.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/2 10:31   lyx        1.0         None

"""
from flask_restplus import reqparse
from app.libs.result_tools.error_code import ParseError


class baseParse(object):
    # bundle_errors=True 捆绑返回每个字段的验证信息不单独返回每个
    parse = reqparse.RequestParser(bundle_errors=True)

    def __init__(self, api):
        self.parse = api.parser()

    # 解析表单并进行表单验证
    def get_result(self):
        try:
            # 获取验证结果，如果验证出错则抛出异常
            result = self.parse.parse_args()
        except Exception as e:
            print(e)
            if isinstance(e, ValueError):
                raise ParseError(msg='请检查您的传入数据是否完整')
            if hasattr(e, 'data'):
                raise ParseError(msg=e.data)
            else:
                raise ParseError()

        return result

    def get_parse(self):
        return self.parse


class IdParse(baseParse):
    def __init__(self):
        self.parse.add_argument('id', trim=True, type=int, help='ID验证失败')


class DataParse(baseParse):
    def __init__(self):
        self.parse.add_argument('data', type=list, location='json')


class PageParse(baseParse):
    def __init__(self):
        self.parse.add_argument('current_page', type=int)
        self.parse.add_argument('page_size', type=int)
        self.parse.add_argument('is_page', type=bool)
