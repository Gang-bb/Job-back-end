# encoding: utf-8
"""
@file: yuansheng.py 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/3/1 22:03   lyx        1.0         None

"""
from exit import db


def fetch_to_dict(sql, params={}, fecth='all', bind=None):
    '''
    dict的方式返回数据
    :param sql: select * from xxx where name=:name
    :param params:{'name':'zhangsan'}
    :param fecth:默认返回全部数据，返回格式为[{},{}],如果fecth='one',返回单条数据，格式为dict
    :param bind:连接的数据，默认取配置的SQLALCHEMY_DATABASE_URL，
    :return:
    '''
    resultProxy = db.session.execute(sql, params, bind=db.get_engine(bind=bind))
    if fecth == 'one':
        result_tuple = resultProxy.fetchone()
        if result_tuple:
            result = dict(zip(resultProxy.keys(), list(result_tuple)))
        else:
            return None
    else:
        result_tuple_list = resultProxy.fetchall()
        if result_tuple_list:
            result = []
            keys = resultProxy.keys()
            for row in result_tuple_list:
                result_row = dict(zip(keys, row))
                result.append(result_row)
        else:
            return None
    return result


# 分页
def fetch_to_dict_pagetion(sql, params={}, page=1, page_size=15, bind=None):
    sql_count = """select count(*) as count from (%s) _count""" % sql
    total_count = get_count(sql_count, params, bind=bind)
    sql_page = '%s limit %s,%s' % (sql, (page - 1) * page_size, page_size)
    print('sql_page:', sql_page)
    result = fetch_to_dict(sql_page, params, 'all', bind=bind)
    result_dict = {'results': result, 'count': total_count}
    return result_dict


# 执行单条语句（update,insert）
def execute(sql, params={}, bind=None):
    print('sql', sql)
    db.session.execute(sql, params, bind=db.get_engine(bind=bind))
    db.session.commit()


def get_count(sql, params={}, bind=None):
    return int(fetch_to_dict(sql, params, fecth='one', bind=bind).get('count'))


# 执行多条语句，失败自动回滚
def execute_many(sqls):
    print(sqls)
    if not isinstance(sqls, (list, tuple)):
        raise Exception('type of the parameters must be list or tuple')
    if len(sqls) == 0:
        raise Exception("parameters's length can't be 0")
    for statement in sqls:
        if not isinstance(statement, dict):
            raise Exception("parameters erro")
    try:
        for s in sqls:
            db.session.execute(s.get('sql'), s.get('params'), bind=db.get_engine(bind=s.get('bind', None)))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise Exception("execute sql fail ,is rollback")
