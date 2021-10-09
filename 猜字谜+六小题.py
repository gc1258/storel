import random
import time
ran = random.randint(10,90) #随机生成一个10=90的整数
print("您进行的是10-90的随机猜字游戏")
loop = 0 #循环次数归0

while True:
    if loop < 3:
        number = int(input("请输入一个10-90之间的整数:"))
        if number == ran :
            print("恭喜您！猜对了")
            loop+=1
            exit()
        elif number > ran :
            print("您输入的数大了")
            loop+=1
        elif number < ran :
            print("您输入的数小了")
            loop+=1
    else :
        print("请等待10s...")
        time.sleep(10)  # 程序睡眠10秒
        loop = 0

#三角形
import math
first = float(input("请输入三角形第一条边长:"))
second = float(input("请输入三角形第二条边长:"))
third = float(input("请输入三角形第三条边长:"))

if first+second >third and first+third >second and second+third >first:
    He = (first + second + third) / 2           #海伦公式
    Per = first + second + third                #三角形的周长
    area = (He*((He - first) * (He - second) * (He - third))) #三角形的面积，X**0.5,**是次幂
    num_area = math.sqrt(area)
    print("三角形的周长为:", Per)
    print("三角形的面积为:", '%.2f'%num_area)    #第二种小数点显示方法，‘%.2f’%x
else :
    print("您输入的三条边长无法构成三角形")


#学生成绩

while True:
    score = float(input("请输入学生成绩:"))
    if score >= 90:
        print("学生成绩为:A")
    elif score >=80 and score < 90:
        print("学生成绩为:B")
    elif score >=70 and score < 80:
        print("学生成绩为:C")
    elif score >=60 and score < 70:
        print("学生成绩为:D")
    elif score <60:
        print("学生成绩为:E")


#温度转换
Fah = float(input("请输入一个华氏温度:"))
Cen = (Fah - 32) / 1.8
print("转换后的摄氏温度为:",round(float(Cen),3))


#圆的计算
ra = float(input("请输入一个圆的半径:"))
Per = (2*3.14)*ra
area = 3.14*(ra*ra)

print("圆的周长为:",Per)
print("圆的面积为:",area)


#长度转换
while True:
    length = float(input("请输入需要换算的长度:"))
    unit = input("请输入换算单位(cm/in):")

    if unit == 'in':
        inch = length *2.54
        print("您输入的长度单位是英寸，转换公制单位厘米为:",inch,"cm")
    elif unit == 'cm':
        centimeter = length *0.3937008
        print("您输入的长度单位是厘米，转换英制单位英寸为:",centimeter,"in")
    else :
        print("仅支持英寸与厘米的转换")
        break

#闰年判断
while True:
    year = int(input("请输入一个年份:"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("您输入的是闰年")
    else:
        print("您输入的不是闰年")


