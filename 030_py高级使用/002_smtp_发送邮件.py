#!/usr/bin/env python
# coding: utf-8

""" """
"""
SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
"""

# coding:utf-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "golpp@qq.com"  # 用户名
# zmbleoejjnrnjdfh
# afdcujjzqokzbaca
# bogkqitesijmbabj
# satnxkpdoyvljgij
# pqhrmxvxdmjcjbja
# pewspqkduwzrjiha
mail_pass = "pewspqkduwzrjiha"  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格


sender = "golpp@qq.com"
receivers = ["3205577372@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText("a test for python", "plain", "utf-8")
message["From"] = Header("lpp", "utf-8")  # 发件人
message["To"] = Header("you", "utf-8")  # 收件人

subject = "my test"  # 邮件主题
message["Subject"] = Header(subject, "utf-8")

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as err:
    print("邮件发送失败 : {}".format(err))
