# encoding: utf-8
"""
@author: lyx
@time: 2020/1/26 19:56
@file: script.py 
"""
import time

from flask_script import Manager

from app.models import *
from app.models.job import Job
from exit import db

db_manage = Manager()


@db_manage.command
def addJob():
    i = 1
    while i <= 3:
        job = Job()
        job.tittle = '我是第二批测试用的工作' + str(i)
        job.reward = '80/周'
        job.place = '朝阳'
        job.settlement = 2
        job.isBagEating = 1
        job.encase = 2
        job.isTrafficSubsidy = 2
        job.royalty = 1
        job.content = '这是测试工作的内容：1.必须按时报到。2.工作前续联系负责人获取工作群号'
        job.detailPlace = '朝阳广场附近'
        job.startTime = "2020-03-15"
        job.endTime = "2020-03-19"
        job.fromCompany = "中国电信南宁分公司"
        job.recruitNum = 1
        job.sex = 3
        job.type = "其他"
        job.withPeople = "王女士"
        db.session.add(job)
        db.session.commit()
        i += 1


@db_manage.command
def addUser():
    user = User()
    user.name = "韦杨琳"
    user.age = 20
    user.nativePlace = "广东省 广州市 白云区"
    user.place = "广州市"
    user.phoneNumber = "18276869988"
    user.birthday = "1999-01-01"
    user.height = "160cm"
    user.eduStatus = 1
    user.bestEdu = "本科"
    user.email = "949526365@qq.com"
    user.qqNum = "9495263656"
    user.weChat = "helloWYL"
    user.loginName = "wyl"
    user.password = "123456"
    db.session.add(user)
    db.session.commit()


@db_manage.command
def addEdu():
    edu = EduResume()
    edu.userId = 1
    edu.school = '广西民族大学'
    edu.major = '软件工程'
    edu.degree = '本科'
    edu.startTime = '2016-09'
    edu.endTime = '2020-06'
    edu.experience = '我在学校表现得很好很好哦'
    db.session.add(edu)
    db.session.commit()


@db_manage.command
def addWork():
    work = WorkResume()
    work.userId = 1
    work.company = '阿里巴巴'
    work.startTime = '2016-09'
    work.endTime = '2020-06'
    work.experience = '我在公司表现得很好很好哦'
    db.session.add(work)
    db.session.commit()


@db_manage.command
def addExpect():
    other = OtherResume()
    other.userId = 1
    other.expectedJobType = "短期兼职"
    other.shortJobTime = "不限"
    other.ableWorkDay = '每周一天'
    other.isFullTime = 1
    db.session.add(other)
    db.session.commit()


@db_manage.command
def addSnow():
    i = 1
    while i <= 3:
        snow = ComSign2()
        snow.name = "000"
        snow.add()
        i += 1
