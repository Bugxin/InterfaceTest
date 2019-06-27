#!/usr/bin/env python
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from conf import settings


# 发邮件相关操作的封装
class SendMail(object):
    def __init__(self,
                 send_user=settings.MAIL_SENDER,
                 password=settings.MAIL_PWD,
                 email_host=settings.MAIL_HOST,
                 reciever_list=settings.MAIL_RECIEVERS):
        self.send_user = send_user
        self.password = password
        self.email_host = email_host
        self.reciever_list = reciever_list
        self.server = smtplib.SMTP()
        self.server.connect(email_host)
        self.server.login(self.send_user, self.password)

    # 组装内容 发送邮件
    def send_mail(self, sub, success_count, failure_count, html_file):
        message = MIMEMultipart('mixed')

        message['Subject'] = Header(sub, 'utf-8')
        message['From'] = self.send_user
        message['To'] = ";".join(self.reciever_list)

        # 构造正文
        text_info = "本次一共跑了%s个接口，成功%s个, 失败%s个" % \
                    (success_count+failure_count, success_count, failure_count)
        text_sub = MIMEText(text_info, 'plain', 'utf-8')
        message.attach(text_sub)

        # 构造附件
        with open(html_file, 'rb') as f:
            html_info = f.read()
        html = MIMEText(html_info, 'base64', 'utf-8')
        html["Content-Type"] = 'application/octet-stream'
        html.add_header('Content-Disposition', 'attachment', filename='result.html')
        message.attach(html)

        # 发邮件
        self.server.sendmail(self.send_user, self.reciever_list, message.as_string())

    def __del__(self):
        self.server.quit()


