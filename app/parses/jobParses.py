# encoding: utf-8
from app.parses.baseParses import baseParse


class JobParse(baseParse):
    def __init__(self):
        self.parse.add_argument('id', trim=True, type=int, required=True, help='ID验证失败', location='args')