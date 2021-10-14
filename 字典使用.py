
#dict = {"k1":"v1","k2":"v2","k3":"v3"}
#1、请循环遍历出所有的key
# dict = {"k1":"v1b","k2":"v2","k3":"v3"}
# for key in dict:
#     print(key)
#
# #2、请循环遍历出所有的value
#     print(dict[key])
#
# # 3、请在字典中增加一个键值对,"k4":"v4"
# dict["K4"] = "V4"
# print(dict)
# for i in range(1,11):
#     number = input("请输入第{}个数".format(i))#或者写为input(f"请输入第{i}个数")

#小明去超市购买水果，账单如下,可以根据水果名称查询购买这个水果的费用
# 苹果  32.8
# 香蕉  22
# 葡萄  15.5
# dict = {"苹果":"32.8","香蕉":"22","葡萄":"15.5"}
#
# while True:
#         name1 = input("请输入您要查询的水果名称:")
#         if name1 in dict:
#             print(name1,"购买花费:",dict[name1],"元")
#         else :print("您查询的水果不存在")


#小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
#
# Fruits = {"苹果":"12.3","草莓":"4.5","香蕉":"6.3","葡萄":"5.8","橘子":"6.4","樱桃":"15.8"}
# info = {"小明": {"fruits":{"苹果":"4","草莓":"13","香蕉":"10"},"money":""},
#          "小刚":{"fruits":{"葡萄":"19","橘子":"12","樱桃":"30"},"money":""}}
# sum = 0
# sum1 = 0
# for key in Fruits:
#     for key1 in info["小明"]["fruits"]:
#         if key == key1:
#             info["小明"]["fruits"][key1] = int(info["小明"]["fruits"][key1])
#             Fruits[key] = float(Fruits[key])
#             money = Fruits[key]*info["小明"]["fruits"][key1]
#             sum += money
#             info["小明"]["money"] = sum
#     for key2 in info["小刚"]["fruits"]:
#         if key == key2:
#             info["小刚"]["fruits"][key2] = int(info["小刚"]["fruits"][key2])
#             Fruits[key] = float(Fruits[key])
#             money1 = Fruits[key] * info["小刚"]["fruits"][key2]
#             sum1 += money1
#             info["小刚"]["money"] = sum1
# print(info["小明"])
# print(info["小刚"])


#编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
# list = [21,56,56,56,56,21,10,56,21,10,56,56,56,10,56]
# count = 0
# count1 = 0
# count2 = 0
# null = {}
# for con1 in list:
#     if con1 ==21:
#         count +=1
#         null[con1] =count
#     elif con1 ==56 :
#         count1 +=1
#         null[con1] = count1
#     elif con1 ==10:
#         count2 +=1
#         null[con1] = count2
# print(count)
# print(null)




#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
#
names = [
    ["刘备","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["张飞", "45", "男", "230", "Tencent", 700 , "10"]]
name = {}

for con in range(4):
    name1 = {}
    key = names[con][0]
    for con1 in range(1,7):
        name1[con1] = names[con][con1]
    name[key] = name1

print(name)

