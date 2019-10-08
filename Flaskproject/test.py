# import time
# month = int(5)
# day = int(28)
# d = time.localtime(
#     time.mktime(
#         time.struct_time((2019, month, day, 0, 0, 0, 0, 0, 0))
#     )
# ).tm_yday
#
# print("生日快乐!你的生日是%s月%s日,是一年中的第%s天" % (month, day, d))


# import calendar
# while True:
#     # 输入指定年月
#     yy = int(input("输入年份: "))
#     mm = int(input("月"))
#     # 显示日历
#     print(calendar.month(yy, mm))

# import datetime
#
# now=datetime.datetime.now()
# print(now)
# xdd=now.weekday()
# print(xdd)
# first_date=datetime.datetime(now.year,now.month,now.day)
# print(first_date)
# first_week=first_date.weekday()
# print(first_week)  #0是周一,6是周日

# import datetime
# input_moth=input("请输入月份:")
# ttime=datetime.datetime.now()
# print(ttime.month)
# print(ttime)

# print(input_moth)


#
# import sys
# print(sys.path)
# import os
# print(os.getcwd())


# def j_sort(a):
#     l = len(a)
#     temp = 0                                    # a = [10, 2, 5, 1, 3, 7, 3]
#     for j in range(0, l - 1):
#         count = j  # 记录最小元素下标
#         # 每次找出最小元素
#         for i in range(j, l - 1):
#             if a[count] > a[i + 1]:
#                 count = i + 1
#         # 交换最小元素和待排序元素中最前一个
#         a[j], a[count] = a[count], a[j]  # 实现跟上述代码一样
#     for i in range(0, l):
#         print(a[i])
# if __name__ == "__main__":
#     a = [10, 2, 5, 1, 3, 7, 3]
#     j_sort(a)


import random
def bubble_sort(li):
   for i in range(len(li) - 1):
      exchange = False
      for j in range(len(li) - i -1):  #内层for循环执行一次，选出一个最大值，将可以调换位置的数调整
         if li[j] > li[j + 1]:
            li[j],li[j+1] = li[j+1],li[j]
            exchange = True
      if not exchange:                # 如果上一趟没有发生交换就证明已经排序完成
         break
data =[2,31,11,57,44,33,66,6,77,99,88]
random.shuffle(data)                  #将有序列表打乱
bubble_sort(data)
print(data)





