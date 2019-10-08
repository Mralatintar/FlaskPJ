# import datetime
# result=[]
#
# big_month=[1,3,5,7,8,10,12]
# small_month=[4.,6,9,11]
#
# now=datetime.datetime.now()
# moth=now.month
#
# first_date=datetime.datetime(now.year,now.month,1,0,0)#年月日时分
# print(first_date.weekday())     #0代表周一，6代表周日
#
#
# if moth in big_month:
#     day_range=range(1,32)
# elif moth in small_month:
#     day_range=range(1,31)
# else:
#     day_range=range(1,29)
#
# day_range=list(day_range)
#
# first_week=first_date.weekday()  #获取一号为周几
# line1=[]
# for e in range(first_week):
#     line1.append("empty")
# for d in range(7-first_week):
#     line1.append(str(day_range.pop(0)))
#
# # print(line1)
# result.append(line1)
#
# while day_range:
#     line=[]
#     for i in range(7):
#         if len(line)<7 and day_range:
#             line.append(str(day_range.pop(0)))
#         else:
#             line.append("empty")
#
#     result.append(line)
# # print(result)
# print(" 星期一   星期二   星期三   星期四   星期五   星期六   星期日")
# for line in result:
#     for day in line:
#         day=day.center(6)
#         print(day,end="  ")
#     print()

import datetime
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
            line1.append(str(self.day_range.pop(0)))

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

if __name__ == '__main__':
    c=Calendar()
    c.print_month()
    print(c.return_month())