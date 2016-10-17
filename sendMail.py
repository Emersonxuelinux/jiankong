#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-26 09:58:12
# @Author  : K3vi (k3vi@atksec.com)
# @Link    : http://k3vi.xyz
# @Version : $Id$

import smtplib
import email.mime.multipart
import email.mime.text
from mysqldb import getMailSet


def mailSet(server, port, from_mail_addr, passwd, to_mail_addr, subject, VulKeyword, VulUrl):
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
    content = '''你好，\n\t你关注的关键字发现了新的漏洞，关键字内容为%s。\n\t漏洞链接为%s''' % (
        VulKeyword, VulUrl)
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    try:
        smtp = smtplib
        smtp = smtplib.SMTP()
        smtp.connect(server, port)
        smtp.login(from_mail_addr, passwd)
        smtp.sendmail(from_mail_addr, to_mail_addr, str(msg))
        print("Send Email succeed")
        smtp.quit()
    except Exception as e:
        print(e)


def mail(mailset, to_mail_addr, VulKeyword, VulUrl):
    smtp_server = mailset[0]
    smtp_post = mailset[1]
    user_mail = mailset[2]
    user_passwd = mailset[3]
    mailSet(smtp_server, smtp_post, user_mail,
            user_passwd, to_mail_addr, "你有新的漏洞信息，请注意查看", VulKeyword, VulUrl)


def sendMail(to_mail_addr, VulKeyword, VulUrl):
    mailset = getMailSet()
    mail(mailset, to_mail_addr, VulKeyword, VulUrl)
