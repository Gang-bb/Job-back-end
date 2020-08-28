# encoding: utf-8
from flask import request
from flask_restplus import Resource, Namespace, fields
from app.libs.result_tools.success import make_result
from app.models import Job
from app.parses.baseParses import IdParse
from app.server.Parse import BaseParse
from app.server.Query import BaseQuery

myapi = Namespace("mybase", description="单表基础服务")

id_parameter = myapi.parser()
id_parameter.add_argument('id', type=int, help='该表的ID', required=True)

base_fields = myapi.model('Resource', {
    'key': fields.String(description='使用json方式传递 与以下参数方式 相等 {"ge_id": 0, "eq_id": 0 }'),
})

test_parser = myapi.parser()
test_parser.add_argument('data', type=dict, location='json', help='使用json方式传递 与以下参数方式'
                                                                  ' 相等 {"ge_id": 0, "eq_id": 0 }')

parser = myapi.parser()
parser.add_argument('is_page', type=bool)

parent2 = myapi.model('Parent', {
    'name': fields.String,
    'class': fields.String(discriminator=True)
})


# @myapi.route('/<string:gt_id>')
# @myapi.response(404, 'Todo not found')
# @myapi.param('gt_id', 'The task identifier')
# @myapi.doc(params={'ge_id': 'An ID', 'eq_id': 'An ID'}, responses={200: '成功哦'})

class serverBase(Resource, BaseParse, BaseQuery):
    __model__ = None

    @myapi.doc(params={'ge_id': 'An ID', 'page_size': 'An ID', 'current_page': 'An ID'}, responses={200: '成功哦'})
    @myapi.expect(parser)
    def get(self):
        """获取该表单项或者全部记录"""
        # 判断是否分页，默认分页
        is_page = request.args.to_dict()['is_page'] if 'is_page' in request.args.to_dict() else False
        # 如果填写了id字段 则优先返回根据id查询的结果
        if IdParse().get_result().id:
            model = self._find_by_id(IdParse().get_result().id)
            return make_result(model)
        # 按条件分页查询
        elif not is_page:
            # 获取 查询条件 和 排序条件
            query, by = self._parse_query_field()
            # 获取分页 默认显示页面（默认为1） 和 页面默认条数（默认为10）
            page, size = self._parse_page_size()
            # 获取分页结果paginate对象
            res = self._find_by_page(page=page, size=size, query=query, by=by)
            return make_result(res)
        # 按条件查询不分页
        else:
            # 获取 查询条件 和 排序条件
            query, by = self._parse_query_field()
            res = self._find_all(query, by)
            return make_result(res)

    @myapi.expect(test_parser)
    def post(self):
        """向该表新增某项或多项纪录"""
        # 获取要操作的数据
        data = self._get_data()
        # 筛选model
        total_count, fail_count, msg, models = self._make_data_to_model(data)
        # 数据库操作，获取结果信息
        total_msg = self._chose_to_do('create', models, total_count, fail_count, msg)
        return make_result(total_msg)

    @myapi.expect(test_parser)
    def delete(self):
        """删除该表的某项或多项纪录"""
        # 获取要操作的数据
        data = self._get_data()
        # 筛选model
        total_count, fail_count, msg, models = self._make_data_to_model(data)
        # 数据库操作，获取结果信息
        total_msg = self._chose_to_do('delete', models, total_count, fail_count, msg)
        return make_result(total_msg)

    @myapi.expect(test_parser)
    def put(self):
        """修改该表的某项或多项纪录"""
        # 获取要操作的数据
        data = self._get_data()
        # 筛选model
        total_count, fail_count, msg, models = self._make_data_to_model(data)
        # 数据库操作，获取结果信息
        total_msg = self._chose_to_do('update', models, total_count, fail_count, msg)
        return make_result(total_msg)

    def _chose_to_do(self, do, models, total_count, fail_count, msg):
        """
        选择相应数据库操作，并返回结果信息
        """
        if models:
            if do == 'create':
                self._create(models)
            elif do == 'update':
                self._update(models)
            elif do == 'delete':
                self._delete(models)
        if fail_count == 0 and total_count != 0:
            total_msg = f"总共{total_count}条数据。操作成功"
        else:
            total_msg = f"总共{total_count}条数据。{request.method}操作失败{fail_count}条数据！" + msg
        return total_msg


api = Namespace("base", description="单表基础接口测试")


@api.route('')
class test(serverBase):
    __model__ = Job

# api.add_resource(test, '/base/test', endpoint='btest')
