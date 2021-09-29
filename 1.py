
 #coding=utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
msg_from='3152007735@qq.com'
passwd='galipqbobahedgdg'
msg_to='57820048@qq.com'
subject="2019144126 桂雨梦"
content="我叫桂雨梦，我的学号是2019144126，我查询到手机流量私网IP地址：10.64.67.211，手机流量公网IP地址：172.68.143.152，校园网私网IP地址：10.128.65.91，校园网公网IP地址：220.164.161.128"
msg=MIMEText(content)
msg['Subject']=subject
msg['From']=msg_from
msg['To']=msg_to
try:
	s=smtplib.SMTP_SSL("smtp.qq.com",465)
	s.login(msg_from,passwd)
	s.sendmail(msg_from,msg_to,msg.as_string())
	print("发送成功")
except Exception as e:
	print("发送失败")
finally:
	s.quit()

	
