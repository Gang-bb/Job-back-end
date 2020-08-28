# encoding: utf-8
from app.libs.result_tools.error_code import AuthFailed
from app.models import Base
from exit import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(Base):
    __tablename__ = 'user'
    __table_args__ = ({'comment': '305 用户表'})
    loginName = db.Column(db.String(50), nullable=True, unique=True, comment='登录名')
    _password = db.Column('password', db.String(210), nullable=True, comment='登录密码')
    type = db.Column(db.SmallInteger, default=3, comment='身份类型 1-系统管理员 2-企业 3-学生')
    openId = db.Column(db.String(300), unique=True, comment='微信小程序用户唯一标识id')

    @property
    def password(self):
        return self._password

    # 使用python pdkdf2加盐密码
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 验证密码
    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    # 登录时的验证操作
    @staticmethod
    def verify(loginName, password):
        user = User.query.filter_by(loginName=loginName).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        # scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id}
