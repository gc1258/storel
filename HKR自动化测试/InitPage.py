'''
    使用excel表来进行参数化数据。
    将测试结果回写excel表中。

    使用邮件发送报告

    使用centos系统做定时执行脚本。
    crontab -e
        * 15 * * *  python   自动化开发框架.py

'''
import xlrd


def LoginData(a):
    wb = xlrd.open_workbook(filename="HKR.xls", encoding_override=True)
    st = wb.sheet_by_index(0)
    rows = st.nrows
    success = []
    error = []
    for i in range(1,rows):
        data = st.row_values(i)
        if i == 1:
            success.append([data[0],data[1],data[2],i])
        else:
            error.append([data[0],data[1],data[2],i])
    if a == 0:
        return success
    elif a == 1:
        return error

print(LoginData(1))









    # #登陆成功的用例数据
    # loginSuccessData = [
    #     {"username":"jason","password":"12345678","expect":"Student Login"},
    #     {"username": "admin1", "password": "root", "expect": "Student Login"},
    # ]
    #
    #
    # # 登陆失败的用例数据  id=msg_uname
    # loginErrorData = [
    #     {"username":"jason","password":"123456789","expect":"账户名错误或密码错误!别瞎弄!"},
    #     {"username": "admin1", "password": "rootw", "expect": "账户名错误或密码错误!别瞎弄!"},
    # ]






