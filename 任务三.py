# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]
#
# summoney = 0
# sumage = 0
# con = 0
# man = 0
# woman = 0
# number1 = 0
# number2 = 0
# number3 = 0
# number4 = 0
# put = input("您是否要添加新员工（y/n）:")
# nameput = []
# if put == 'y':
#     for con1 in range(7):
#         name = input("请输入添加的员工信息:")
#         nameput.append(name)
#     names.append(nameput)
# for count in range(len(names)):
#     con += 1
#     for key in range(len(names[count])):
#         if key == 5:
#             summoney += int(names[count][key])
#             avemoney = summoney/con
#         elif key == 1:
#             sumage += int(names[count][key])
#             aveage = sumage / con
#     for sex in names[count]:
#             if sex == '男':
#                 man +=1
#             elif sex == '女':
#                 woman += 1
#     for number in names[count]:
#         if number == '50':
#             number1 +=1
#         elif number =='60':
#             number2 +=1
#         elif number =='10':
#             number3 +=1
#         elif number == '30':
#             number4 +=1
#
#
# print(avemoney)
# print(aveage)
# print(names)
# print("man =",man,"woman =",woman)
#
# print("50 =",number1,"60 =",number2,"10 =",number3,"30 =",number4)




#现在魔法学院有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，所以大家上交作业的次数并不一致。
# [罗恩, 23 ,35 ,44]
# [哈利 ,60, 77 ,68 ,88, 90]
# [赫敏, 97 ,99 ,89 ,91, 95, 90]
# [马尔福 ,100, 85 ,90]
# 求每个人的总成绩？
# name = [["罗恩", 23 ,35 ,44],
#         ["哈利" ,60, 77 ,68 ,88, 90],
#         ["赫敏", 97 ,99 ,89 ,91, 95, 90],
#         ["马尔福", 100, 85, 90]]
#
# achievement = 0
# achievement1 = 0
# achievement2 = 0
# achievement3 = 0
# for names in range(len(name)):
#     for ach in range(len(name[names])):
#         if ach != 0 and names == 0:
#             achievement += name[names][ach]
#         elif ach != 0 and names == 1:
#             achievement1 += name[names][ach]
#         elif ach != 0 and names == 2:
#             achievement2 += name[names][ach]
#         elif ach != 0 and names == 3:
#             achievement3 += name[names][ach]
#
# print("罗恩=",achievement)
# print("哈利=",achievement1)
# print("赫敏=",achievement2)
# print("马尔福=",achievement3)


#冒泡排序
# a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
# len = len(a)
# temp = 0
# print(a)
# for one in range(len-1):
#     for two in range(len-1):
#         if a[two] > a[two+1]:
#             temp = a[two]
#             a[two] = a[two+1]
#             a[two+1] = temp
# print(a)