import smtplib
from email.mime.text import MIMEText
msg = MIMEText("This is an email", 'plain', 'utf-8')

from_addr = "gaoaolei@km.com"
to_addr = ["853573584@qq.com"]

server = smtplib.SMTP()
server.connect('smtp.km.com', 25)
server.ehlo()
server.starttls()
server.login(from_addr, '4209841413Pl')
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
print('ok')