# encoding: utf-8
from app.models import Base
from exit import db


class Job(Base):
    __tablename__ = 'job'
    __table_args__ = ({'comment': '300 工作表'})
    tittle = db.Column(db.String(50), comment='工作的标题')
    reward = db.Column(db.String(20), comment='报酬')
    place = db.Column(db.String(20), comment='地点')
    settlement = db.Column(db.SmallInteger, nullable=False, default=3, comment='工作结算方式 1-日结 2-周结 3-完工结')
    isBagEating = db.Column(db.SmallInteger, nullable=False, default=2, comment='是否包吃 1-是 2-否')
    encase = db.Column(db.SmallInteger, nullable=False, default=2, comment='是否包住 1-是 2-否')
    isTrafficSubsidy = db.Column(db.SmallInteger, nullable=False, default=2, comment='是否有交通补贴 1-是 2-否')
    royalty = db.Column(db.SmallInteger, nullable=False, default=2, comment='是否有提成 1-是 2-否')
    type = db.Column(db.String(20), comment='工作类型')
    recruitNum = db.Column(db.Integer, default=1, comment='招聘人数')
    sex = db.Column(db.String(20), comment='性别要求 1-男 2-女 3-男女不限')
    browseTimes = db.Column(db.Integer, default=100, comment='浏览次数')
    content = db.Column(db.String(500), comment='工作内容')
    startTime = db.Column(db.String(80), comment='开始时间')
    endTime = db.Column(db.String(80), comment='结束时间')
    detailPlace = db.Column(db.String(20), comment='详细地址')
    fromCompany = db.Column(db.String(80), comment='发布的企业')
    withPeople = db.Column(db.String(20), comment='企业联系人')
    signNum = db.Column(db.Integer, default=0, comment='当前报名人数人数')
    phone = db.Column(db.String(20), comment='企业联系人电话')
    email = db.Column(db.String(20), comment='企业联系人邮箱')
    cId = db.Column(db.BigInteger, comment='企业的id号')
    status = db.Column(db.SmallInteger, default=1, comment='当前状态 1-待审批 2-进行中 3-已结束')
    testUnique = db.Column(db.String(20), unique=True, comment='测试是否唯一')


class Job_Signup(Base):
    __tablename__ = 'job_signup'
    __table_args__ = ({'comment': '302 提交工作记录表'})
    userId = db.Column('userId', db.BigInteger, comment='申请学生的用户id号')
    stuId = db.Column('stuId', db.BigInteger, comment='申请学生的学生id号')
    jobId = db.Column('jobId', db.BigInteger, comment='申请工作的id号')
    message = db.Column(db.String(200), comment='学生给企业的留言')
    status = db.Column(db.SmallInteger, default=1, comment='状态 1-已报名 2-已录用 3-已到岗 4-已结算')