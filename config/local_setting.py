DEBUG = True
SERVER_PORT = 8888
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'job'

DB_URI = 'mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
# 查询时会显示原始SQL语句
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = DB_URI
# 动态追踪修改设置，如未设置只会提示警告
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 设置默认编码
SQLALCHEMY_ENCODING = "utf8mb4"

# 令牌的有效时间
TOKEN_EXPIRATION = 30 * 24 * 3600

SECRET_KEY = '\x88D\xf09\x91\xa0A\x07\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x98*4'
