# encoding: utf-8
from app.models import Base
from exit import db


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = ({'comment': '308 学生信息表'})
    sname = db.Column(db.String(20), comment='学生的名字')
    uId = db.Column(db.BigInteger, comment='关联的用户id')
    age = db.Column(db.Integer, comment='用户的年龄')
    nativePlace = db.Column(db.String(50), comment='所在城市')
    place = db.Column(db.String(50), comment='所在地级市')
    phoneNumber = db.Column(db.String(80), comment='手机号')
    birthday = db.Column(db.String(50), comment='生日')
    height = db.Column(db.String(50), comment='身高')
    eduStatus = db.Column(db.SmallInteger, default=1, comment='教育状态 1-在读 2-已毕业')
    bestEdu = db.Column(db.String(20), default="本科", comment='最高学历')
    email = db.Column(db.String(50), comment='邮箱')
    qqNum = db.Column(db.String(20), comment='QQ')
    weChat = db.Column(db.String(50), comment='微信号')
    sex = db.Column(db.SmallInteger, default=1, comment='性别 1-男 2-女')