#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-27 15:07:41
# @Author  : K3vi (k3vi@atksec.com)
# @Link    : http://k3vi.xyz
# @Version : $Id$

from mysqldb import getMailSet
from sendMail import sendMail


def sendMail(mailset, to_mail_addr):
    smtp_server = mailset[0]
    smtp_post = mailset[1]
    user_mail = mailset[2]
    user_passwd = mailset[3]
    sendMail(smtp_server, smtp_post, user_mail,
             user_passwd, to_mail_addr, "你有新的漏洞信息，请注意查看")


def main():
    mailset = getMailSet()
    to_mail_addr = "1737257007@qq.com"
    test(mailset, to_mail_addr)


if __name__ == '__main__':
    main()
