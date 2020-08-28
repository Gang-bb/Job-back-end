# encoding: utf-8
from app.libs.snow import IdWorker
from app.models import Base
from exit import db


class Company(Base):
    __tablename__ = 'company'
    __table_args__ = ({'comment': '307 公司信息表'})
    cname = db.Column(db.String(20), comment='公司的名字')
    uId = db.Column(db.BigInteger, comment='关联的用户id')
    cplace = db.Column(db.String(50), comment='所在城市')
    cphone = db.Column(db.String(80), comment='企业电话')
    cemail = db.Column(db.String(50), comment='企业邮箱')
    ctype = db.Column(db.String(50), comment='所属行业')
    cinfo = db.Column(db.String(500), comment='简介')
    pphone = db.Column(db.String(80), comment='联系人手机号')
    pname = db.Column(db.String(20), comment='联系人姓名')
    isVerify = db.Column(db.SmallInteger, default=1, comment='是否通过审核 1-待审核 2-通过 3-未通过')


class ComSign(Base):
    __tablename__ = 'com_sign'
    __table_args__ = ({'comment': '309 公司信息提交审核记录表'})
    uId = db.Column(db.BigInteger, comment='关联的公司用户id')
    cId = db.Column(db.BigInteger, comment='关联的公司id')
    isVerify = db.Column(db.SmallInteger, default=1, comment='是否通过审核 1-提交待审核 2-通过 3-不通过')


def getId(tabNum):
    snow_id = IdWorker().get_id()
    my_id = tabNum + str(snow_id)
    return int(my_id[:-3])


# 用雪花算法生成ID
def getSnowId(tabNum):
    snow_id = IdWorker().get_id()
    my_id = tabNum + str(snow_id)
    return int(my_id[:-3])


class Base2(db.Model):
    # 表明这个是基类，创建表时不会被创建
    __abstract__ = True
    __tablenum__ = "100"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=False, default=getSnowId(__tablenum__),
                   comment='主键id')

    def add(self):
        self.id = getSnowId(self.__tablenum__)
        db.session.add(self)
        db.session.commit()


class ComSign2(Base2):
    __tablename__ = 'com_sign2'
    __tablenum__ = "101"
    __table_args__ = ({'comment': '309 公司信息提交审核记录表'})
    name = db.Column(db.String(80), comment='名字')
