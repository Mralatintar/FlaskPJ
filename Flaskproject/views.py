# from flask import Flask             #引入Flask类，Flask类实现了一个WSGI应用
#
# app=Flask(__name__)                 #app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__
#
# @app.route("/")                     #使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上
#
# def index():
#     return "hello world"
#
# if __name__=="__main__":
#     app.run(host="127.0.0.1",port=8000,debug=True)

import datetime
import os
from flask import render_template,redirect      #调用了 render_template模板,可将变量传入到网页内
from main import *                #引入app（数据库）实例
from models import Curriculum           #引入数据库数据表
from models import User,Leave
import functools
from flask import session
from main import api

import hashlib
import datetime
import functools


def setPassword(password):
    result=hashlib.md5(password.encode()).hexdigest()
    return result

def loginValid(fun):
    @functools.wraps(fun)
    def inner(*args,**kwargs):
        username=request.cookies.get("username")
        id=request.cookies.get("id","0")
        user=User.query.get(int(id))
        session_username=session.get("username")
        if user:
            if user.user_name==username and username==session_username:
                return fun(*args,**kwargs)
            else:
                return redirect("/login/")
        else:
            return redirect("/login/")
    return inner


class Pager:
    """
    flask分页通过sqlalachemy查询进行分页
    offset 偏移，开始查询的位置
    limit 单页条数
    分页器需要具备的功能
    页码
    分页数据
    是否第一页
    是否最后一页
    """

    def __init__(self, data, page_size):
        """

        :param data: 要分页的数据
        :param page_size: 每页多少条
        """
        self.data = data #总数据
        self.page_size = page_size #单页数据
        self.is_start = False
        self.is_end = False
        self.page_count = len(data)
        self.next_page = 0 #下一页
        self.previous_page = 0 #上一页
        self.page_nmuber = self.page_count/page_size
        #(data+page_size-1)//page_size
        if self.page_nmuber == int(self.page_nmuber):
            self.page_nmuber = int(self.page_nmuber)
        else:
            self.page_nmuber = int(self.page_nmuber)+1

        self.page_range = range(1,self.page_nmuber+1)#页码范围
    def page_data(self,page):
        """
        返回分页数据
        :param page: 页码
        page_size = 10
        1    offect 0  limit(10)
        2    offect 10 limit(10)
        page_size = 10
        1     start 0   end  10
        2     start 10   end  20
        3     start 20   end  30
        """
        self.next_page = int(page) + 1
        self.previous_page = int(page) - 1
        if page <= self.page_range[-1]:
            page_start = (page - 1)*self.page_size
            page_end = page*self.page_size
            # data = self.data.offset(page_start).limit(self.page_size)
            data = self.data[page_start:page_end]
            if page == 1:
                self.is_start = True
            else:
                self.is_start = False
            if page == self.page_range[-1]:
                self.is_end = True
            else:
                self.is_end = False
        else:
            data = ["没有数据"]
        return data

#
# class Pager:
#     def __init__(self,data,page_size):         #init方法
#         self.data=data                         #获取参数data
#         self.page_size=page_size                #获取参数page_size
#         self.is_start=False                     #获取is_start默认为False
#         self.is_end=False
#         self.page_count=len(data)               #获取data列表的列表数
#         self.next_page=0                        #下一页为0  假象
#         self.previous_page=0                    #上一页为0  假象
#         self.page_number=self.page_count/page_size  #获取假象 page_number为页码数
#         if self.page_number==int(self.page_number): #如果是整数
#             self.page_number=int(self.page_number)  #获取整的
#         else:                                       #如果不是整数
#             self.page_number=int(self.page_number)+1#获取数+1
#         self.page_range=range(1,self.page_number+1) #page_range是页码的循环
#     def page_data(self,page):                   #
#         self.next_page=int(page)+1
#         self.previous_page=int(page)-1
#         if page<=self.page_range[-1]:
#             page_start=(page-1)*self.page_size
#             page_end=page*self.page_size
#
#             data=self.data[page_start,page_end]
#             if page==1:
#                 self.is_start=True
#             else:
#                 self.is_start=False
#             if page==self.page_range[-1]:
#                 self.is_end=True
#             else:
#                 self.is_end=False
#         else:
#             data=["没有数据"]
#         return data

@app.route("/logout/")
def logout():
    response=redirect("/login/")
    response.delete_cookie("username")
    response.delete_cookie("email")
    response.delete_cookie("id")
    session.pop("username")
    return response



@app.route("/index/")
@loginValid
def index():
    return render_template("index.html",**locals())


@app.route("/login/",methods=["get","post"])
def login():
    error=""
    if request.method=="POST":
        form_data=request.form
        email=form_data.get("email")
        password=form_data.get("password")
        user=User.query.filter_by(email=email).first()
        if user:
            db_password=user.password
            if setPassword(password)==db_password:
                response=redirect("/index/")
                response.set_cookie("username",user.user_name)
                response.set_cookie("email",user.email)
                response.set_cookie("id",str(user.id))
                session["username"]=user.user_name
                return response
            else:
                error="密码错误"
        else:
            error="不存在用户名"
    return render_template("login.html",error=error)

@app.route("/base/")
def base():
    return render_template("base.html")


import time
@app.route("/userinfo/")
def userinfo():
    calendar = Calendar().return_month()
    now = datetime.datetime.now()
    return render_template("userinfo.html",**locals())


from flask import request
@app.route("/register/",methods=["GET","POST"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        email=request.form.get("email")
        user=User()
        user.user_name=username
        user.password=setPassword(password)
        user.email=email
        user.save()
    return render_template("register.html",**locals())

@app.route("/holiday_request/",methods=["GET","POST"])
def holiday_request():
    if request.method=="POST":
        data=request.form
        request_user=data.get("request_name")
        request_type=data.get("request_type")
        request_startdate=data.get("request_startdate")
        request_enddate=data.get("request_enddate")
        request_phone=data.get("request_phone")
        request_description=data.get("request_description")

        leave=Leave()
        leave.request_id=request.cookies.get("id")
        leave.request_name=request_user
        leave.request_type=request_type
        leave.request_startdate=request_startdate
        leave.request_enddate=request_enddate
        leave.request_description=request_description
        leave.request_phone=request_phone
        leave.request_status="0"
        leave.save()
        return redirect("/leave_list/")
    return render_template("holiday_request.html",**locals())

@app.route("/leave_list/<int:page>/")
def leave_list(page):
    leaves=Leave.query.all()
    pager = Pager(leaves, 2)
    page_data = pager.page_data(page)
    return render_template("leave_list.html",**locals())

import json
from flask import jsonify

@app.route("/cancel/<int:id>/")
def cancel(id):
    id=request.args.get("id")
    leave=Leave.query.get(int(id))
    leave.delete()
    return jsonify({"data":"删除成功"})

from forms import TaskForm
@app.route("/add_task/",methods=["GET","POST"])
def add_task():
    errors=""
    task=TaskForm()
    if request.method=="POST":
        if task.validate_on_submit():
            formData=task.data
        else:
            errors_list=list(task.errors.keys())
            errors=task.errors
            print(errors)
    return render_template("add_task.html",**locals())

from models import Picture

from setting import STATICFILES_DIR
@app.route("/picture/",methods=["GET","POST"])
@csrf.exempt
def picture():
    p={"picture":"img/1.jpg"}
    if request.method=="POST":
        file=request.files.get("photo")
        file_name=file.filename
        file_path="img/%s"%file_name
        save_path= os.path.join(STATICFILES_DIR,file_path)
        file.save(save_path)
        p=Picture()
        p.picture=file_path
        p.save()
    return render_template("picture.html",**locals())










