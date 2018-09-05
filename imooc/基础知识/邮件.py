# import smtplib
# from email.mime.text import MIMEText
# msg = MIMEText("This is an email", 'plain', 'utf-8')
#
# from_addr = "853573584@qq.com"
# to_addr = ["853573584@qq.com"]
#
# server = smtplib.SMTP()
# server.connect('smtp.qq.com', 25)
# # server.ehlo()
# # server.starttls()
# server.login(from_addr, 'jxridcxixgjtbbic')
# server.sendmail(from_addr, to_addr, msg.as_string())
# server.quit()
# print('ok')

# !/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "853573584@qq.com"  # 用户名
mail_pass = "jxridcxixgjtbbic"  # 口令

sender = '853573584@qq.com'
receivers = ['864981619@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText("""    见信如唔，别月余，思念之甚，之切，之烈如肝肠寸断，然迫时事，不得效命远方，归期无期；适逢堂兄大婚，得以此
机归家探望，然票不得，奈何奈何，君毋望，好生在家上奉父母，下抚小儿，吾甚慰。""", 'plain', 'utf-8')
message['From'] = Header("你亲爱的老公", 'utf-8')
message['To'] = Header("戴巧珍", 'utf-8')

subject = '来自远方的爱'
message['Subject'] = Header(subject, 'utf-8')

try:
    # smtpObj = smtplib.SMTP()
    # smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    # smtpObj.ehlo()
    # smtpObj.starttls()
    # smtpObj.login(mail_user, mail_pass)
    # smtpObj.sendmail(sender, receivers, message.as_string())
    # print("邮件发送成功")
    # 方法二
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
    # smtpObj.ehlo()
    # smtpObj.starttls()
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e)
