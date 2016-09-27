#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from handle import matching_keywords
from handle import https_get as get
from mysqldb import loudonghezi_last_update, loudonghezi_last, loudonghezi_insert
import re
import sys


last_data = loudonghezi_last()


def get_qid(last_data):                        # 抓取每页的ID并与上次任务对比
    li = []
    for n in range(1, 10):
        url = 'https://www.vulbox.com/board/internet/page/%d' % n
        n_page = get(url)
        soup = bs(n_page, "html.parser")
        items = soup.find_all(
            href=re.compile('^/bugs/'), class_='btn btn-default btn-check')
        for item in items:
            t = str(item)[49:67]
            li.append(t)
            loudonghezi_last_update(li[0])
            if t == last_data:
                if last_data == str(items[0].find('a', class_=''))[23:39]:
                    sys.exit()
                return li
    return li


def get_url():                                  # 获取每个id对应链接
    url_data = []
    for n in get_qid(last_data):
        url_data_ = 'https://www.vulbox.com/bugs/%s' % n
        url_data.append(url_data_)
    return url_data


def main():
    print("loudonghezi")
    m_keyword = matching_keywords()
    for n in get_url():
        n_page = get(n)
        soup = bs(n_page, "html.parser")
        text = soup.find_all(text=re.compile(m_keyword), limit=1)
        if text:
            keyword_back = re.search(m_keyword, text[0])
            title = soup.h3.string
            time = soup.find('span', class_='time').string[0:10]
            vul_name = title  # 漏洞名称
            vul_id = n[28:46]  # 漏洞编号
            vul_time = time  # 漏洞发布时间
            vul_keyword = keyword_back.group(0)  # 关键字
            loudonghezi_insert(vul_name, vul_id, vul_time, vul_keyword)


if __name__ == '__main__':
    main()
