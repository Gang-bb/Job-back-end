# encoding: utf-8
from flask_restplus import Namespace

from app.libs.db_tools.get_db_info import get_keys_type_dict

api = Namespace('base', description='通用swagger参数')


def getIdParameter(helpMsg='id'):
    id_parameter = api.parser()
    id_parameter.add_argument('id', type=int, help=helpMsg, required=True)
    return id_parameter


def get_info(schema_name):
    # get方法备注信息
    GET_info = '<font color=#333 size=4 face="微软雅黑">输入key值则为按id(=key)查询；输入其他规定键值按其他条件查询，' \
        '查询结果默认分页，以下一些细则：</font>\n<font color=red size=3 face="微软雅黑">gt<大于>、ge<大于等于>、lt<小于>、' \
               'le<小于等于>、ne<不等于>、eq<等于>、' \
        'ic<包含>、ni<不包含>、in<查询多个相同字段的值>、by<排序(0:正序,1:倒序)>\nis_page<结果是否分页 True分页 ' \
        'False不分页>、current_page<分页显示的默认页>、page_size<分页页面记录数></font>\n<font color=#333 size=4 face="微软雅黑">' \
               '例如：查询id大于30，' \
        '年龄小于18的学生：gt_id>30、lt_age<18\n</font>'
    # post方法备注信息
    post_dict = get_keys_type_dict(schema_name)
    post_info = f"单条添加该表记录示例:(需根据类型填入对应类型的值)\n{str(post_dict)}\n" + "多条改为[{},{},{}...]形式\n"
    POST_info = '<font color=#333 size=4 face="微软雅黑">单条添加该表记录示例:(需根据类型填入对应类型的值)\n</font>'\
                + f"{str(post_dict)}\n"
    # put方法备注信息
    put_info = '单条修改该表纪录示例:(修改该表id为10的记录的name字段)\n{"id": 10, "name": "lyx"}\n多条改' \
               '为[{},{},{}...]形式\n'
    # delete方法备注信息
    delete_info = '单条删除该表纪录示例:(删除该表id为10的记录)\n{"id": 10}\n多条改为[{},{},{}...]形式' \
                  '（注意{}中只需也只支持填入id字段）\n'
    total_info = '<font color=#CD853F size=4 face="微软雅黑">*****GET方法的说明：\n</font>'+ \
                 f"{GET_info}" + \
                 '<font color=#CD853F size=4 face="微软雅黑">*****POST方法的说明：\n</font>'+ \
                 f"{POST_info}" + \
                 '<font color=#CD853F size=4 face="微软雅黑">*****PUT方法的说明：\n</font>'+ \
                 f"{put_info}" + \
                 '<font color=#CD853F size=4 face="微软雅黑">*****DELETE方法的说明：\n</font>' + \
                 f"{delete_info}"
    return total_info
