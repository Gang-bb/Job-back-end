# encoding: utf-8
"""
@author: lyx
@time: 2020/1/16 17:39
@file: application.py 
"""
import os

from flask import Flask
from app.api import register_blueprints
from flask_cors import CORS
from exit import db


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name, static_folder="apps/static", template_folder="apps/templates")
        # 测试环境下可以先写local 便于测试,部署改为base_setting.py
        self.config.from_pyfile('config/local_setting.py')
        # 根据环境变量按需加载改变配置文件
        if "ops_config" in os.environ:
            print("当前配置文件环境：" + os.environ["ops_config"])  # 获取环境变量的值
            self.config.from_pyfile('config/%s_setting.py' % os.environ['ops_config'], silent=True)

        db.init_app(self)


app = Application(__name__)
register_blueprints(app)
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    """
     如果不使用命令行运行
     则默认：
     端口号：8888
     配置文件：local_setting
    """

    app.run(host='0.0.0.0', port=8888)
