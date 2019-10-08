from flask import Flask             #引入Flask类，Flask类实现了一个WSGI应用
from flask import render_template
import datetime

app=Flask(__name__)                 #app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__



class Calendar:
    """
    当前类实现日历功能
    返回列表潜逃列表的日历
    安装日历格式打印日历
    """
    def __init__(self,month="now"):
        self.result=[]
        big_month = [1, 3, 5, 7, 8, 10, 12]
        small_month = [4, 6, 9, 11]
        now = datetime.datetime.now()

        if month=="now":
            month=now.month


            first_date = datetime.datetime(now.year, now.month, 1, 0, 0)  # 年月日时分
        else:
            # assert int(month) in range(1,13)
            first_date=datetime.datetime(now.year,month, 1, 0, 0)

        if month in big_month:
            day_range = range(1, 32)
        elif month in small_month:
            day_range = range(1, 31)
        else:
            day_range = range(1, 29)

        self.day_range = list(day_range)
        first_week=first_date.weekday()
        line1=[]
        for e in range(first_week):
            line1.append("empty")
        for d in range(7 - first_week):
            line1.append(self.day_range.pop(0))

        self.result.append(line1)
        while self.day_range:
            line = []
            for i in range(7):
                if len(line) < 7 and self.day_range:
                    line.append(str(self.day_range.pop(0)))
                else:
                    line.append("empty")

            self.result.append(line)
    def return_month(self):
        return self.result
    def print_month(self):
        print(" 星期一   星期二   星期三   星期四   星期五   星期六   星期日")
        for line in self.result:
            for day in line:
                day = day.center(6)
                print(day, end="  ")
            print()


@app.route("/")
def xixi():
    return "hello world"

# @app.route("/list/")
# def list():
#     return "你好list"





# @app.route("/xdd/<moth>/<day>/")
# def diji(moth,day):
#     listday=[31,28,31,30,31,30,31,31,30,31,30,31]
#     listone=0
#     moth=int(moth)-1
#     day=int(day)
#     listday=listday[0:moth]
#     for i in listday:
#         listone+=i
#     countday=listone+day
#     return "你的生日是%s月%s日是今年的第%s天" %(moth+1,day,countday)


@app.route("/index/")
def index():
    return render_template("index.html",**locals())



@app.route("/login/")
def login():
    return render_template("login.html")

@app.route("/base/")
def blank():
    return render_template("base.html")


import time
@app.route("/userinfo/")
def userinfo():
    calendar=Calendar().return_month()
    now=datetime.datetime.now()
    return render_template("userinfo.html",**locals())

if __name__=="__main__":
    app.run(host="127.0.0.1",port=8000,debug=True)