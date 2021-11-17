import HTMLTestRunner
import unittest
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr

tests = unittest.defaultTestLoader.discover(os.getcwd(),pattern="Test*.py")

runner = HTMLTestRunner.HTMLTestRunner(
    title = "HKR测试报告",
    description="hkr登录测试报告",
    verbosity=1,
    stream=open(file="hkr.html",mode="wb")
)


runner.run(tests)


# 邮件发送代码

smtpserver = 'smtp.163.com'
#发送人邮箱地址与授权码
user = "a1711570217@163.com"
password = "AWPYRYNASKYBWKKF"
#发送人邮箱(已有user，可要可不要，不要则替换下方msgRoot[]，smtp.sendmail的sender)
sender = "a1711570217@163.com"
#收件人
receive = ['1711570217@qq.com']

#邮件标题
subject = '测试报告'
#邮件内容
content = "/h1<html><h1 style='color:blue'>功能的测试报告,附件为测试结果<></html>"


#附件地址
send_file = open(r"HKR.xls","rb").read()



msgRoot = MIMEMultipart()
msgRoot.attach(MIMEText(content,'xls','utf-8'))
msgRoot['Subject'] = subject
msgRoot['From'] = formataddr((str(Header('吴鼎','utf-8')),sender))
msgRoot['To'] = ','.join(receive)
#附件
att = MIMEText(send_file,"base64",'utf-8')
att['Content-Type'] = 'application/octet-stream'
# att['Content-Disposition'] = 'attachment;filename="计算器.html"' % str.encode("utf-8")
att.add_header('Content-Disposition','attachment',filename='HKR.xls')
msgRoot.attach(att)


#开始发送
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receive,msgRoot.as_string())
smtp.quit()





























































