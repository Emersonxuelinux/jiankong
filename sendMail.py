#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-26 09:58:12
# @Author  : K3vi (k3vi@atksec.com)
# @Link    : http://k3vi.xyz
# @Version : $Id$

import smtplib
import email.mime.multipart
import email.mime.text


def sendMail(server, port, from_mail_addr, passwd, to_mail_addr, subject):
    """
    server:邮件服务器地址
    port：邮件服务器端口
    from_mail_addr:发件邮箱地址
    to_mail_addr:接件邮箱地址
    passwd：发件邮箱密码
    subject：发件主题
    """

    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = from_mail_addr
    msg['to'] = to_mail_addr
    msg['subject'] = subject
    content = '''你好，\n\t这是一封自动发送的邮件。\n\twww.ustchacker.com'''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib
    smtp = smtplib.SMTP()
    smtp.connect(server, port)
    smtp.login(from_mail_addr, passwd)
    smtp.sendmail(from_mail_addr, to_mail_addr, str(msg))
    smtp.quit()
