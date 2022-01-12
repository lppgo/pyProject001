#!/usr/bin/env python

import smtplib
import time
# smtplib 用于邮件的发信动作
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.header import Header
# 用于构建邮件头
import csv
# 引用csv模块，用于读取邮箱信息

# 发信方的信息：发信邮箱，QQ邮箱授权码
# 方便起见，也可以直接赋值
from email.mime.multipart import MIMEMultipart
from_addr = input('请输入登录邮箱：')
password = input('请输入邮箱授权码kzwakcxjjlnlcaji：')#授权码需要自己登陆邮箱，进入设置，隐私设置，开启指定的SMTP设置

# 发信服务器
smtp_server = 'smtp.qq.com'
user_name=''
user_pass=''
num = 0
# 读取收件人数据，并启动写信和发信流程
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        to_addrs=row[9]
        user_name=row[1]
        if len(to_addrs)>0:
            # 邮件内容
            text='''您好：<br>
            xxx平台<br>
            信息展示地址：xxx<br>
            用户名：{account}<br>
            密码：xxxx<br>
            <br>
            信息录入地址：xxxxx<br>
            用户名：{account}<br>
            密码：xxxx<br>
            <br>
            请查收，谢谢！
            '''.format(account=user_name)
            msg = MIMEMultipart()
            txt = MIMEText(text, 'html', 'utf-8')
            msg.attach(txt)
            msg['From'] = Header(from_addr)
            msg['To'] = Header(to_addrs)
            msg['Subject'] = Header('邮件头名称')
            server = smtplib.SMTP_SSL(host='smtp.qq.com')
            server.connect(smtp_server,465)
            server.login(from_addr, password)
            server.sendmail(from_addr, to_addrs, msg.as_string())
            print(row[3],msg['To'],text)
            num = num + 1
            time.sleep(10)
        else:
            print(row[3],'邮箱地址为空')
#关闭服务器
server.quit()
print('已发送',num,'封邮件！')

