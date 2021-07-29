#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ----- 需要修改的参数 -----
# email相关
sender = 'fedbook@qq.com'
password = '******'
smtp_server = 'smtp.qq.com'
smtp_port = 465
receivers = ['recever1@163.com', 'recever2@qq.com']
# ------------------------


# Example 1: 发送纯文本邮件
def send_text_email(subject, detail):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    mail_msg = """
    时间：{now_time}
    详情：{detail}
    """.format(subject=subject, now_time=now_time, detail=detail)

    msg = MIMEText(mail_msg, 'plain', 'utf-8')
    msg['From'] = Header('fedbook汇报人 <%s>' % sender, 'utf-8')
    msg['To'] = Header('fedbook订阅者', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # smtp.set_debuglevel(1)    # 打印和SMTP服务器交互的所有信息
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('Error: 无法发送邮件')
        print(e)


# Example 2: 发送 HTML 格式的邮件
def send_html_email(subject, detail):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    mail_msg = """
    <h1 style='margin-top:10px;margin-bottom:10px;text-align:center'>{subject}</h1>
    <hr>
    <h2 style='margin-top:0;margin-bottom:10px'>时间</h2>
    <div style='margin-left: 40px'>{now_time}</div>
    <hr>
    <h2 style='margin-top:0;margin-bottom:10px'>详情</h2>
    <div style='margin-left: 40px'>{detail}</div>
    <hr>
    """.format(subject=subject, now_time=now_time, detail=detail)

    msg = MIMEText(mail_msg, 'html', 'utf-8')
    msg['From'] = Header('fedbook汇报人 <%s>' % sender, 'utf-8')
    msg['To'] = Header('fedbook订阅者', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # smtp.set_debuglevel(1)    # 打印和SMTP服务器交互的所有信息
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('Error: 无法发送邮件')
        print(e)


# Example 3: 发送带附件的邮件
def send_attach_email(subject, detail, attach_list):
    now_time = time.strftime('%Y-%m-%d %H:%M:%S')
    mail_msg = """
    时间：{now_time}
    详情：{detail}
    """.format(subject=subject, now_time=now_time, detail=detail)

    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # msg = MIMEText(mail_msg, 'plain', 'utf-8')
    msg['From'] = Header('fedbook汇报人 <%s>' % sender, 'utf-8')
    msg['To'] = Header('fedbook订阅者', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    msg.attach(MIMEText(mail_msg, 'plain', 'utf-8'))
    # 构造附件，传送指定目录下的文件
    for att_path in attach_list:
        att = MIMEText(open(att_path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att["Content-Disposition"] = 'attachment; filename={filename}'.format(filename=att_path)
        msg.attach(att)

    try:
        smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # smtp.set_debuglevel(1)    # 打印和SMTP服务器交互的所有信息
        smtp.login(sender, password)
        smtp.sendmail(sender, receivers, msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException as e:
        print('Error: 无法发送邮件')
        print(e)


def delay_func(delay_time):
    for i in range(delay_time):
        print('等待{0}s...'.format(delay_time-i))
        time.sleep(1)


if __name__ == "__main__":
    email_title = 'Python SMTP 纯文本邮件测试'
    detail = """
    Let's have a test.
    """
    send_text_email(email_title, detail)

    delay_func(5)

    email_title = 'Python SMTP HTML格式邮件测试'
    detail = """
    <div>代码仓库：<a href="https://github.com/wenyuan/practice-in-python" target="_blank">practice-in-python</a></div>
    <div style='margin-bottom:5px'>有问题可以在 Issues 留言。</div>
    """
    send_html_email(email_title, detail)

    delay_func(5)

    email_title = 'Python SMTP 带附件邮件测试'
    detail = """
    附件是案例源码，请查收。
    """
    attach_list = ['email_example.py', '../README.md']
    send_attach_email(email_title, detail, attach_list)
