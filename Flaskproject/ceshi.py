# list1=["1","2","3","4","5","6","7","8","9","1","3","5","9"]
# xdd=["9","5","2"]
# pdd=''
# xixi=[]
# for i in xdd:
#     pdd=pdd+i
# print(pdd)
# for j in list1:
#     if j in pdd:
#         xixi.append(pdd)
#     else:
#         xixi.append(j)
# print(xixi)
def openx(pdd):
    list1=["1","2","3","4","5","6","7","8","9","1","3","5","9"]
    xdd=list(pdd)
    print(xdd)
    xixi=[]
    for j in list1:
        if j in pdd:
            xixi.append(pdd)
        else:
            xixi.append(j)
    print(xixi)
ooc=input("请输入:")
openx(ooc)
