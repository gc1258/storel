'''
    1.加载所有的测试用例
    2.执行用例并生成测试报告
'''
import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from email.header import Header

# 1.加载所有用例
tests = unittest.defaultTestLoader.discover(r"C:\Users\Admin\Desktop\作业\day13\任务代码",pattern="Test*.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",
    description="这是加、减、乘、除的测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="wb+")
)

# 3.执行用例
runner.run(tests)




# 4.任务： 使用邮件发送附件，把报告发送给我
smtpserver = 'smtp.163.com'
#发送人邮箱地址与授权吗
user = "a1711570217@163.com"
password = "AWPYRYNASKYBWKKF"
#发送人邮箱(已有user，可要可不要，不要则替换下方msgRoot[]，smtp.sendmail的sender)
sender = "a1711570217@163.com"
#收件人
receive = ['1004515171@qq.com']

#邮件标题
subject = '计算机测试报告A'
#邮件内容
content = "<html><h1 style='color:blue'>吴鼎的计算器加、减、乘、除法的测试报告</h1></html>"


#附件地址
send_file = open(r"C:\Users\Admin\Desktop\作业\day13\任务代码\计算器.html","rb").read()



msgRoot = MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject'] = subject
msgRoot['From'] = sender
msgRoot['To'] = ','.join(receive)
#附件
att = MIMEText(send_file,"base64",'utf-8')
att['Content-Type'] = 'application/octet-stream'
# att['Content-Disposition'] = 'attachment;filename="计算器.html"' % str.encode("utf-8")
att.add_header('Content-Disposition','attachment',filename='计算器测试报告.html')
msgRoot.attach(att)


#开始发送
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receive,msgRoot.as_string())
smtp.quit()



