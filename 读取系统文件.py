import re
ip_count = 0
ip_data = {}
data = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")

table = data.readlines()
for i in table:
    data1 = re.split(' ',i)
    if data1[0] not in ip_data:
        ip_data[data1[0]] = 1
    elif data1[0] in ip_data:
        ip_data[data1[0]] = ip_data[data1[0]]+1


print(ip_data)



















