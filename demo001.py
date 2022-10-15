# print("打印__name__:",__name__)
# if __name__ == '__main__':
#     print("999999999999999999999999")
#     print("999999999999999999999999")
#     print("999999999999999999999999")
#
# import sys
# for i in sys.path:
#     print(i)

# class BaseClass(object):
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
# var = input("请输入属性名：")
# value = 8890
# setattr(BaseClass,var,value)
# print(BaseClass.__dict__)
#
# 取余 %
# print(9%5)
#
# #除法取商 //
# print(11//5)
#
# print(5**2)
# a=22
# b = 20
# cc = a % b
# print(cc)
# import  random
# number1 = random.random()
# print(number1)
#
#
# sum1= random.randint(1,1000)+random.random()
# print(sum1)
#
# for i in range(1, 7):
#     print(f"{i}")
#     # for j in range(i):
#     #     print("*",end="")

# # 列表推导式实现
# li2 = []
# for i in range(1, 101):
#     li2.append("page{}".format(i))

# print(li2)

print("----------------li3------------------")
# # 列表推导式实现
# li3 =["page{}".format(i) for i in range(1,101)]
# print(li3)
# li3 =[i for i in range(1,101)]
# print(li3)


import requests
res =requests.get("https://www.baidu.com")
s=res.json


# b ={}
# b =s
# print(b)
# m = {'a':1, 'b':2}
# b=dict(map(lambda t:(t[1],t[0]), m.items()))
# print(b)

dic ={'a':1, 'b':2}
# d = {value: key for key, value in dic.items()}  # 利用推导式
# print(d)

# b =dic
# print(b)
#去重
li =[1,1,1,2,2,3,3,44,4,56,2,14,52,34]
lis =[]
for i in li:

    if i not in lis:
        lis.append(i)
print(lis)
