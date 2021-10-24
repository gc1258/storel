'''
全年的销售总额
每件衣服的销售（件数）占比
每件衣服的月销售占比
每件衣服的销售额占比

最畅销的衣服是那种
每个季度最畅销的衣服
全年销量最低的衣服
    rows = st.nrows#获取有多少行
    cols = st.ncols# 获取有多少列
    # 选择一个选项卡
st = wb.sheet_by_name("员工管理")
'''



import xlrd
wd = xlrd.open_workbook(filename=r"C:\Users\Admin\Desktop\作业\day7\任务\2020年每个月的销售情况.xlsx",encoding_override=True)
wd_len = len(wd.sheets())

#全年销售数量
def sales_volumes():
    volumes = 0
    for con in range(wd_len):
        st = wd.sheet_by_index(con)
        rows = st.nrows
        for i in range(1,rows):
            data = st.row_values(i)
            volumes += data[4]
    return volumes

#全年总销售额
def yearsum():
    year_sum = 0
    for con in range(wd_len):
        st = wd.sheet_by_index(con)
        rows = st.nrows
        for i in range(1,rows):
            data = st.row_values(i)
            year_sum += (data[2]*data[4])
    return year_sum

# #每件衣服的销售（件数）占比
clothes_type = {}
for con in range(wd_len):
    st = wd.sheet_by_index(con)
    rows = st.nrows#获取有多少行
    cols = st.ncols# 获取有多少列
    for i in range(1,rows):
        data = st.row_values(i)

        name = data[1]
        number = data[4]
        if name not in clothes_type:
            clothes_type[name] = number
        elif name in clothes_type:
            clothes_type[name] = clothes_type[name]+number

for clothes_name,clothes_quantity in clothes_type.items():
    sum = sales_volumes()
    print(clothes_name,"占全年销售比例:",'%.7f'%(clothes_quantity / sum))
print("-------------------------")
#月销售量
Monthly_sales = {}
month_clothes = {}
spring = {}
summer = {}
autumn = {}
winter = {}
for con in range(wd_len):
    sales_sum = 0
    st = wd.sheet_by_index(con)
    cols = st.ncols
    rows = st.nrows
    data = st.col_values(4)
    data2 = st.row_values(con)
    Monthly_sales[con] = data
    for sa in range(1,len(Monthly_sales[con])):
        sales_sum = sales_sum + Monthly_sales[con][sa]
    print("-------------------------")
    print(con+1,"月销售总量为",sales_sum)
    for i in range(1,rows):
        data1 = st.row_values(i)
        name = data1[1]
        if name not in month_clothes:
            month_clothes[name] = data1[4]
        elif name in month_clothes:
            month_clothes[name] += data1[4]
    for clothes_name,clothes_quantity in month_clothes.items():
        print(clothes_name,"销售占比:",'%.5f'%(clothes_quantity / sales_sum))

    if con==1 or con==2 or con==3:
        for i in range(1, rows):
            data1 = st.row_values(i)
            name = data1[1]
            if name not in spring:
                spring[name] = data1[4]
            elif name in spring:
                spring[name] += data1[4]
    if con==4 or con==5 or con==6:
        for i in range(1, rows):
            data1 = st.row_values(i)
            name = data1[1]
            if name not in summer:
                summer[name] = data1[4]
            elif name in summer:
                summer[name] += data1[4]
    if con==7 or con==8 or con==9:
        for i in range(1, rows):
            data1 = st.row_values(i)
            name = data1[1]
            if name not in autumn:
                autumn[name] = data1[4]
            elif name in autumn:
                autumn[name] += data1[4]
    if con==10 or con==11 or con==0:
        for i in range(1, rows):
            data1 = st.row_values(i)
            name = data1[1]
            if name not in winter:
                winter[name] = data1[4]
            elif name in winter:
                winter[name] += data1[4]
print("-------------------------")
print("春季最畅销的衣服:",max(spring,key=spring.get))
print("夏季最畅销的衣服:",max(summer,key=summer.get))
print("秋季最畅销的衣服:",max(autumn,key=autumn.get))
print("冬季最畅销的衣服:",max(winter,key=winter.get))
print("-------------------------")

# #每件衣服的销售额占比
#
clothes_type = {}
clothes_Price = {}
total_price ={}
month_clothes = {}
money_type = 0
y = yearsum()
for con in range(wd_len):
    st = wd.sheet_by_index(con)
    rows = st.nrows#获取有多少行
    cols = st.ncols# 获取有多少列
    for i in range(1,rows):
        data = st.row_values(i)
        name = data[1]
        number = data[4]
        price = data[2]
        if name not in clothes_type:
            clothes_type[name] = number
            clothes_Price[name] = price
            total_price[name] = 0
        elif name in clothes_type:
            clothes_type[name] = clothes_type[name]+number


for total in total_price:
    money_type = (clothes_type[total]*clothes_Price[total])
    print(total,"销售额占比:",'%.5f'%(money_type / y))

print("-------------------------")
#最畅销的衣服
max = max(clothes_type.values())
min = min(clothes_type.values())
for clothes in total_price:
    if max == clothes_type[clothes]:
        print("最畅销的衣服是:",clothes,"|售出:",max)
    elif min == clothes_type[clothes]:
        print("销量最低的衣服是:",clothes,"|售出:",min)







