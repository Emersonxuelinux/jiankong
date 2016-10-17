#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-08 09:17:53
# @Author  : K3vi (k3vi@atksec.com)
# @Link    : http://k3vi.xyz
# @Version : cnvd spider


import re
import requests
from sendMail import sendMail
from handle import matching_keywords
from mysqldb import cnvd_insert, cnvd_last, cnvd_keyword_insert, cnvd_last_update, getkeyWord, getFollowMail


def httpGet(url):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
    accept = "text/html,application/xhtml+xml,application/xml;q=0.9,imag"
    accept_encoding = 'gzip, deflate, sdch'
    accept_Language = 'zh-CN,zh;q=0.8'
    cache_control = "max-age=0"
    connection = "keep-alive"
    cookie = "bdshare_firstime=1472713241524;"
    headers = {"User-Agent": user_agent,
               "Accept": accept,
               "Accept-Encoding": accept_encoding,
               "Accept-Language": accept_Language,
               "Cache-Control": cache_control,
               "Connection": connection,
               "Cookie": cookie}
    try:
        f = requests.get(url, headers=headers)
        f.encoding = 'utf-8'
        page = f.text
        return page
    except Exception as e:
        print(e)


def dealAllVul():
    url = "http://www.cnvd.org.cn/flaw/typeResult?typeId=29&max=800&offset=0"
    page = httpGet(url)

url = "http://www.cnvd.org.cn/flaw/typeResult?typeId=29&max=800&offset=0"
page = httpGet(url)
print(page)