#从键盘输入10个数，求他们的和
# sum = 0
# for num in range(10):
#     number = int(input("请输入一个数字："))
#     sum += number
# print(sum)


#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
# list = []
# sum = 0
# max = 0
# for num in range(10):
#     number = int(input("请输入一个数（连续10次）:"))
#     list.append(number)
#     sum += number
#     for count in range(len(list)):
#         if list[count] > max :
#             max = list[count]
#         elif list[count] < max:
#             max = max
#         elif list[count] == max:
#             max = list[count]
# average = sum/10
#
# print("输入10个数之和为:",sum)
# print("输入的10个数中最大的值为:", max)
# print("输入的10个数的平均值为:",average)


#使用random模块，如何产生 50~150之间的数？
# import random
# ran = random.randint(50,150)
# print(ran)


#从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
# frist = float(input("请输入第一条边:"))
# second = float(input("请输入第二条边:"))
# third = float(input("请输入第三条边:"))
#
# if frist + second > third and frist + third > second and second + third > frist :
#     if frist == second and frist == third and second == third:
#         print("您输入的三条边，构成等边三角形^_^")
#     elif frist == second or frist == third or second == third:
#         print("您输入的三条边，构成等腰三角形^_^")
#     elif (frist*frist)+(second*second) == third*third:
#         print("您输入的三条边，构成直角三角形^_^")
#     else : print("您输入的三条边构成普通三角形^_^")
# else : print("您输入的三条边不构成三角形")



'''
#有以下两个数，使用+，-号实现两个数的调换。
print("-----------------------------------------")
print("当前有两个数:A=56 / B=78 ,使用+ -号实现数的调换")
print("-----------------------------------------")

A = 56
B = 78
while True:
    exchange = input("请输入+ 或者 - :")
    if exchange == '+':
        TS = A
        A = B
        B = TS
        print("调换后:")
        print("A =",A)
        print("B =",B)
    elif exchange == '-':
        TS = A
        A = B
        B = TS
        print("调换后:")
        print("A =",A)
        print("B =",B)
'''



# #实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
# import time
# count = 0
# print("------------登录-------------")
# user = input("请输入用户名:")
# password = input("请输入密码:")
# print("-----------------------------")
# while True:
#     if count == 2:
#         print("用户名或密码错误三次，暂时冻结")
#         time.sleep(100)
#     elif user == 'root' and password == 'admin':
#         print("登录成功!")
#         break
#     elif user != 'root' or password != 'admin':
#         print("用户名或密码错误，请重新输入")
#         print("------------登录-------------")
#         user = input("请输入用户名:")
#         password = input("请输入密码:")
#         print("-----------------------------")
#         count +=1
#


#图形打印

# for i in range(8):
#     for j in range(0, 8 - i):
#         print(end=" ")
#     for k in range(8 - i, 8):
#         print("*", end=" ")
#
#     print("")



#使用while循环实现99乘法表的打印。
# a = 1
# while a <=9 :
#     b = 1
#     while b <= a:
#         c = a*b
#         print("",b,"x","",a,"=",c,end="  ")
#         b += 1
#     a += 1
#     print("")


#编程实现99乘法表的倒叙打印

# a = 9
# while a >= 1:
#     b = 1
#     while b <= a:
#         c = a*b
#         print("",b,"x","",a,"=",c,end=" ")
#         b += 1
#     a -= 1
#     print("")


#一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。

# #白天开始爬
# day = 0
# day1 = 0
# day2 = 0
# summetre = 0
# while summetre != 20:
#     summetre += 3
#     day1 += 0.5
#     if summetre != 20:
#         summetre -= 2
#         day2 += 0.5
#     day = day1 + day2
# else :
#     print("day = ",day)


#猜字游戏完善
# import random
# import time
# ran = random.randint(10,90) #随机生成一个10=90的整数
# print("您进行的是10-90的随机猜字游戏")
# loop = 0 #循环次数归0
# jinbi = 1000
# while True:
#     if loop < 3:
#         number = int(input("请输入一个10-90之间的整数:"))
#         if number == ran :
#             print("恭喜您！猜对了")
#             loop+=1
#             jinbi += 1000
#         elif number > ran :
#             print("您输入的数大了")
#             loop+=1
#         elif number < ran :
#             print("您输入的数小了")
#             loop+=1
#
#     elif jinbi >= 100:
#         print("当前金币数量:",jinbi)
#         count = input("请问您是否消耗100金币购买次数y/n:")
#         if count == 'y':
#             loop -= 1
#             jinbi -= 100
#         elif count == 'n':
#             time.sleep(10)
#             exit()
#         else :
#             print("错误！请重新输入")
#             continue




#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
list = []
product = 1
sum = 0
number = int(input("请输入您要求的阶乘:"))
for num in range(1,number+1):
    list.append(num)
for start in range(len(list)):
    product = product*list[start]
    sum += product

print("sum = ",sum)