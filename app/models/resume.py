# encoding: utf-8
from app.models import Base
from exit import db


class EduResume(Base):
    __tablename__ = 'resume_edu'
    __table_args__ = ({'comment': '304 教育经历表'})
    userId = db.Column('userId', db.BigInteger, comment='关联userId号')
    school = db.Column(db.String(100), comment='学校')
    major = db.Column(db.String(50), comment='专业')
    degree = db.Column(db.String(50), comment='学历')
    startTime = db.Column(db.String(50), comment='开始时间')
    endTime = db.Column(db.String(50), comment='结束时间')
    experience = db.Column(db.String(500), comment='在校经历')


class WorkResume(Base):
    __tablename__ = 'resume_work'
    __table_args__ = ({'comment': '306 工作经历表'})
    userId = db.Column('userId', db.BigInteger, comment='关联userId号')
    company = db.Column(db.String(100), comment='公司名')
    startTime = db.Column(db.String(50), comment='开始时间')
    endTime = db.Column(db.String(50), comment='结束时间')
    experience = db.Column(db.String(500), comment='在职经历')


class OtherResume(Base):
    __tablename__ = 'resume_other'
    __table_args__ = ({'comment': '306 简历其他项'})
    userId = db.Column('userId', db.BigInteger, comment='关联userId号')
    expectedJobType = db.Column(db.String(50), default='不限', comment='期望工作类型')
    shortJobTime = db.Column(db.String(50), default='不限', comment='短期工作时间')
    ableWorkDay = db.Column(db.String(50), default='均可', comment='可上班时间')
    selfIntroduction = db.Column(db.String(500), comment='自我介绍')
    isFullTime = db.Column(db.SmallInteger, comment='是否支持全职上班 1-是 0-否')