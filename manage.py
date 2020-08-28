# encoding: utf-8
"""
@author: lyx
@time: 2020/1/16 17:34
@file: manage.py 
"""
# import app.models
from flask_script import Server, Manager
from application import app
from flask_migrate import Migrate, MigrateCommand
from exit import db
from app.libs.script_tools.script import db_manage


manager = Manager(app)

# web server
manager.add_command("runserver",
                    Server(host='127.0.0.1', port=app.config['SERVER_PORT'], use_reloader=True))

# database
Migrate(app, db)
manager.add_command("db", MigrateCommand)
manager.add_command('db_tools', db_manage)


def main():
    manager.run()


if __name__ == '__main__':
    # 可以将所有错误打印
    try:
        import sys

        sys.exit(main())
    except Exception as e:
        import traceback

        traceback.print_exc()
