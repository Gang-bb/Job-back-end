# encoding: utf-8
from app.models import Base
from exit import db


class Search(Base):
    __tablename__ = 'search'
    __table_args__ = ({'comment': '303 热门搜索表'})
    message = db.Column(db.String(20), comment='搜索的信息')
