# -*- coding: utf-8 -*-

from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)


app.config['DEBUG'] = True
app.config['MAIL_PORT'] = 25               # 邮件服务器端口
# app.config['MAIL_USE_SSL'] = True
# app.config['MAIL_USE_TLS'] = True        #
app.config['MAIL_USERNAME'] = 'gheros@qq.com'
app.config['MAIL_PASSWORD'] = 'ytjlmnq_888666'
print(app.config)
mail = Mail(app)
# if app.config['MAIL_USE_SSl']:print('1')
@app.route('/')
def index():
    msg = Message('Hi', sender='edward@stack.kw', recipients=['gheros@qq.com'])
    msg.html = '<b>Hello Web</b>'
    # msg.body = 'The first email!'
    mail.send(msg)
    return '<h1>OK!</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)


from flask import Flask
from flask_mail import Mail, Message
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.stack.kw'  # 邮件服务器地址
app.config['MAIL_PORT'] = 465               # 邮件服务器端口
# app.config['MAIL_USE_TLS'] = True          # 启用 TLS
app.config['MAIL_USE_SSL'] = True          # 启用 TLS
app.config['MAIL_USERNAME'] = 'edward@stack.tw'
app.config['MAIL_PASSWORD'] = '34@Shidai'

mail = Mail(app)

@app.route('/')
def index():
    msg = Message('Hi', sender='edward@stack.kw', recipients=['edward@stack.tw'])
    msg.html = '<b>Hello Web</b>'
    # msg.body = 'The first email!'
    mail.send(msg)
    return '<h1>OK!</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)

# !/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@runoob.com'
receivers = ['gheros@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")

