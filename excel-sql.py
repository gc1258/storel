import pymysql
import xlrd




def up_SQL(sql,param):
    con = pymysql.connect(host="localhost",user="root",password="",database="Clothing_sales")
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def month_if(month_name):
    con = pymysql.connect(host="localhost",user="root",password="",database="Clothing_sales")
    cursor = con.cursor()
    sql = "show tables"
    cursor.execute(sql)
    table = cursor.fetchall()
    con.commit()
    cursor.close()
    con.close()
    if month_name in table:
        return 1
    else:
        return 0

wb = xlrd.open_workbook(filename=r"C:\Users\Admin\Desktop\作业\day7\任务\2020年每个月的销售情况.xlsx",encoding_override=True)

# 选项卡数量
wb_len = len(wb.sheets())

for i in range(wb_len):
    st = wb.sheet_by_index(i)
    rows = st.nrows
    month_name = str(i+1)+"月份"
    mi = month_if(month_name)
    if mi == 0:
        sql1 = "CREATE TABLE `%s月份` (日期 varchar(20),服装名称 varchar(20),价格 decimal(10,2),库存 decimal(10,2),销售量 decimal(10,2))"
        month = i+1
        up_SQL(sql1,month)
    for j in range(1,rows):
        data = st.row_values(j)
        sql = "INSERT INTO `%s月份` VALUE(%s,%s,%s,%s,%s);"
        up_SQL(sql,(i+1,data[0],data[1],data[2],data[3],data[4]))
    print(i+1,"月ok")





