import os

BASE_DIR=os.path.abspath(os.path.dirname(__file__))
STATICFILES_DIR=os.path.join(BASE_DIR,"static")
# SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite")
# SQLALCHEMY_COMMIT_ON_TEARDOWN=True                #请求结束自动提交
# SQLALCHEMY_TRACK_MODIFICATIONS=True
#
# DEBUG=True
class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "ORM.sqlite")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 请求结束自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY='1234556'
class RunConfig(Config):
    DEBUG = False