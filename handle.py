#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
# handle HTTP request
import urllib.request
import urllib.parse
import requests
from mysqldb import getkeyWord


def get(url):  # 发送get请求，返回网页内容
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
    headers = {"User-Agent": user_agent}
    try:
        req = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(req)
        page = response.read().decode("UTF8", errors='ignore')
        return page
    except Exception as e:
        print(e)


def post(url):  # 发送post请求，返回网页内容
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36"
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", user_agent)
        f = urllib.request.urlopen(req)
        page = f.read().encode('utf-8', errors='ignore')
        return page
    except Exception as e:
        print(e)


def matching_keywords(keyword=getkeyWord()):  # 处理关键字，用来快速匹配
    key_str = ''
    for key in keyword.values():
        key_str += key + "|"
    key_str = key_str[0:-1]
    return key_str


def https_get(url):  # 访问https
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36'
    headers = {"User-Agent": user_agent,}
                
    try:
        f = requests.get(url, headers=headers)
        f.encoding = 'utf-8'
        page = f.text
        return page
    except Exception as e:
        print(e)
