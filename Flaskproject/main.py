import os                       #导入os模块
from flask import Flask         #导入Flask方法
from flask_sqlalchemy import SQLAlchemy  #导入SQLALchemy方法用来创建app实例数据库

import pymysql
from flask_wtf import CSRFProtect
from flask_restful import Api
from flask_migrate import Migrate

pymysql.install_as_MySQLdb()  #python3不支持mysqldb，用pymysql代替，这样就可以用mysqldb

app=Flask(__name__)             #app是Flask的实例

app.config.from_pyfile("setting.py")
app.config.from_object("setting.Config")

# BASE_DIR=os.path.abspath(os.path.dirname(__file__))
# #其中 os.path.dirname(__file__)函数用于取出settings.py所在文件夹的位置。
#
# app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+os.path.join(BASE_DIR,"ORM.sqlite")
# app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"]=True                #请求结束自动提交
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True               #v1后加入的配置。目的是跟踪修改


models=SQLAlchemy(app)
csrf=CSRFProtect(app)
api=Api(app)

migrate=Migrate(app,models)