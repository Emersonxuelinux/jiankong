#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from mysqldb import butian_last_update, butian_last, butian_insert
from handle import matching_keywords
from handle import https_get as get
import re


last_data = "QTVA-2016-474677"

url = 'https://butian.360.cn/vul/list/page/%d' % n
n_page = get(url)
# def get_qid():                        # 抓取每页的ID并与上次任务对比
#     li = []
#     for n in range(1, 20):
#         url = 'https://butian.360.cn/vul/list/page/%d' % n
#         n_page = get(url)
#         print(n_page)
#         exit()
#         soup = bs(n_page, "html.parser")
#         items = soup.find_all('p', class_='list-view')
#         for item in items:
#             t = str(item.find('a', class_=''))[23:39]
#             li.append(t)
#             butian_last_update(li[0])
#             if t == last_data:
#                 if last_data == str(items[0].find('a', class_=''))[23:39]:
#                     # sys.exit()
#                     return "false"
#                 return li
#     return li
#
#
# def get_url():                                  # 获取每个id对应链接
#     url_data = []
#     qid = get_qid()
#     if qid == "false":
#         return "false"
#     for n in get_qid():
#         url_data_ = 'https://butian.360.cn/vul/info/qid/%s' % n
#         url_data.append(url_data_)
#     return url_data
#
#
# def main():
#     print("butian")
#     g_url = get_url()
#     if g_url == "false":
#         return
#     for n in get_url():
#         m_keyword = matching_keywords()
#         n_page = get(n)
#         soup = bs(n_page, "html.parser")
#         text = soup.find_all(text=re.compile(m_keyword), limit=1)
#         if text:
#             keyword_back = re.search(m_keyword, text[0])
#             title = soup.find_all(
#                 style=re.compile('font-weight: bold'))[0].string
#             time = soup.find('dt', text=re.compile('^20')).string[0:10]
#             vul_name = title  # 漏洞名称
#             vul_id = n[35:51]  # 漏洞编号
#             vul_time = time   # 漏洞发布时间
#             vul_keyword = keyword_back.group(0)  # 关键字
#             butian_insert(vul_name, vul_id, vul_time, vul_keyword)
#
#
# if __name__ == '__main__':
#     main()
