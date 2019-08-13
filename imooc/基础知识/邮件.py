# !/usr/bin/python3 只能发qq，用的是qq邮箱的授权码
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "smtp.qq.com"  # 设置服务器
from_address = "853573584@qq.com"  # 用户名
mail_pass = "hjdphfvzyjotbcif"  # 口令
to_address = 'gaoaolei@km.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText("""    见信如唔，别月余，思念之甚，之切，之烈如肝肠寸断，然迫时事，不得效命远方，归期无期；适逢堂兄大婚，得以此
机归家探望，然票不得，奈何奈何，君毋望，好生在家上奉父母，下抚小儿，吾甚慰。""", 'plain', 'utf-8')
message['From'] = Header(from_address, 'utf-8')
message['To'] = Header(to_address, 'utf-8')
message['Subject'] = Header('来自远方的爱', 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL()
    smtpObj.connect(mail_host, 465)
    smtpObj.login(from_address, mail_pass)
    smtpObj.sendmail(from_address, to_address, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(e)
