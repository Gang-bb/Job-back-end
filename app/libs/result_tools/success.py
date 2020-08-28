# encoding: utf-8
from flask_sqlalchemy import Pagination

from app.libs.result_tools.result_todict import queryToDict
from app.libs.result_tools.success_code import Success_Code


def make_result(data=None, code=Success_Code().Success):
    success_dict = {
        "code": code if data else Success_Code().noData_Success,
        "msg": Success_Code.msg[code] if data else Success_Code.msg[20001]
    }
    # 分页情况的结果返回格式
    if isinstance(data, Pagination):
        new_data = dict()
        new_data['currentPage'] = data.page
        new_data['totalPages'] = data.pages
        new_data['pageSize'] = data.per_page
        new_data['totalItems'] = data.total
        new_data['pageList'] = list(data.iter_pages())
        # new_data['has_prev'] = data.has_prev
        # new_data['has_next '] = data.has_next
        new_data['prev_num '] = data.prev_num
        new_data['next_num '] = data.next_num
        new_data['currentItems'] = queryToDict(data.items)
        success_dict['data'] = new_data
    elif isinstance(data, str):
        success_dict['msg'] = data
    else:
        success_dict['data'] = queryToDict(data) if data else ""
    return success_dict



