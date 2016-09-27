#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi

from handle import get
from mysqldb import wooyun_insert, wooyun_last, wooyun_last_update, getkeyWord, wooyun_keyword_insert
import re


def get_bug_ids():      # 获取所有漏洞标号
    base_url = "http://www.wooyun.org/bugs/page/"
    bug_id_list = []
    last_id = wooyun_last()
    for i in range(1, 11):
        url = base_url + str(i)
        bug_id_page = get(url)
        bug_ids = re.findall(
            r'<a href="/bugs/(wooyun-\d{4}-\d{7})">', bug_id_page)
        if bug_id_list == bug_ids[0]:
            return None
        for id in bug_ids:
            bug_id_list.append(id)
            if id == last_id:
                return bug_id_list
    if bug_id_list:
        return bug_id_list
    else:
        return None


def qualified_bug(id):  # 获取满足关键字条件的漏洞标号
    url = "http://www.wooyun.org/bugs/" + id
    page = get(url)
    print(url)
    re_key = re.compile(deal_keyword())
    flag = re.search(re_key, page)
    return flag, page


def insert_bug_info(page):  # 插入数据
    try:
        title = re.findall(
            r"<h3 class='wybug_title'>漏洞标题：\s+(.+)\s+</h3>", page)[0][:-3].strip()  # 获取漏洞名称
        bug_id = re.findall(
            r'<h3>缺陷编号：\s+<a href="/bugs/(wooyun-\d{4}-\d{7})">WooYun-\d{4}-\d{6}</a>', page)[0]  # 漏洞id
        time = re.findall(r'提交时间：\s*(2016-\d{2}-\d{2})', page)[0]  # 获取漏洞发布时间
        print('------', title, bug_id, time)
        row_id = wooyun_insert(title, bug_id, time)
        return row_id
    except:
        pass


def get_qualified_key(id, page):  # 获取满足条件的关键字字典的key
    keyword_dict = getkeyWord()
    key_list = []
    for key in keyword_dict.keys():
        x = re.search(keyword_dict[key], page)
        if x:
            key_list.append(key)
    return key_list


def deal_keyword(keyword=getkeyWord()):  # 处理关键字，用来快速匹配
    key_str = ''
    for key in keyword.values():
        key_str += key + "|"
    key_str = key_str[0:-1]
    return key_str


def main():  # 主体函数
    bug_id_list = get_bug_ids()
    keyword = getkeyWord()
    if not bug_id_list:
        return
    else:
        # wooyun_last_update(bug_id_list[0])
        for id in bug_id_list:
            flag, page = qualified_bug(id)
            if flag:
                keys = get_qualified_key(id, page)
                row_id = insert_bug_info(page)
                for key in keys:
                    wooyun_keyword_insert(row_id, key, keyword[key])
            else:
                continue


if __name__ == '__main__':
    main()
