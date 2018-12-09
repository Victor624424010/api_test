import smtplib#连接smtp服务器发送邮件
from conf import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart #混合格式

def send_report():
    #组装邮件正文
    body = MIMEMultipart()
    msg = MIMEText(config.body,'plain','utf-8') #plain 纯文本  html 代码
    body.attach(msg)#将正文添加到body对象中
    #组装邮件头
    body['from'] = config.smtp_user
    body['To'] = config.receiver
    body['Subject'] = 'from python'
    #附件
    with open('../report/report.html','rb')as f:
        att_file = f.read()
    att = MIMEText(att_file,'base64','utf-8')
    att['Content-Type']='application/octet-stream'#声明附件内容格式MIMIE数据流格式
    att['Content-Disposition']="attachment;filename='report.html'"#f附件描述信息
    body.attach(att)
    #连接smtp服务器并发送
    smtp = smtplib.SMTP_SSL('smtp.qq.com')#建立连接
    smtp.login ('624424010@qq.com','Victor929115')#登录邮箱
    smtp.sendmail('624424010@qq.com','963570929@qq.com',body.as_string())#发送邮件


