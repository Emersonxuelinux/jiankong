#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-27 15:51:37
# @Author  : K3vi (k3vi@atksec.com)
# @Link    : http://k3vi.xyz
# @Version : $Id$


import re
from sendMail import sendMail
from pyquery import PyQuery as pyq
from handle import https_get as httpGet
from handle import matching_keywords
from mysqldb import butian_insert, butian_last, butian_keyword_insert, butian_last_update, getkeyWord, getFollowMail


def getAllVulUrl():
    sear_key = []
    vul_ids = []
    mainUrl = "https://butian.360.cn/vul/list/page/"
    try:
        last_id = butian_last()
        for i in range(1, 11):
            page = httpGet(mainUrl + str(i))
            pq = pyq(page)
            a_link = pq('.ld-con-list')
            for a in a_link:
                pqa = pyq(a)
                flag1 = re.search(
                    '<a href="/vul/info/qid/QTVA-\d{4}-\d{6}">.+</a>', str(pqa))
                flag2 = re.search(
                    '<a href="/vul/search/c/.+">.+</a>', str(pqa))
                if flag1:
                    urla = re.findall(
                        '<a href="/vul/info/qid/(QTVA-\d{4}-\d{6})">.+</a>', str(pqa))
                    if urla == last_id:
                        returnDict = [vul_ids, sear_key]
                        return returnDict
                    vul_ids.append(urla[0])
                elif flag2:
                    urlb = re.findall(
                        '<a href="/vul/search/c/.+">(.+)</a>', str(pqa))
                    sear_key.append(urlb[0])
                    if urlb == last_id:
                        returnDict = [vul_ids, sear_key]
                        return returnDict
        returnDict = [vul_ids, sear_key]
        return returnDict  # 字典
    except Exception as e:
        print(e)


def dealSearchKey(searchVul):  # returnDict[sear_key]
    try:
        keyWord = matching_keywords()
        all_key = getkeyWord()
        for vul in searchVul:
            keyIdList = []
            flag = re.search(keyWord, vul)
            if flag:
                for i in all_key.keys():
                    flag1 = re.search(all_key[i], vul)
                    if flag1:
                        keyIdList.append(i)
            for vid in keyIdList:
                xid = butian_insert(all_key[vid], all_key[vid], 'null')
                butian_keyword_insert(xid, vid, all_key[vid])
                toMailAddr = getFollowMail(vid)
                sendMail(toMailAddr[0], all_key[
                    vid], 'https://butian.360.cn/vul/search/c/%s' % all_key[vid])
    except Exception as e:
        print(e)


def dealVulIds(vulIds):
    try:
        keyWord = matching_keywords()
        all_key = getkeyWord()
        for vulId in vulIds:
            keyIdList = []
            url = 'http://butian.360.cn/vul/info/qid/%s' % vulId
            page = httpGet(url)
            flag = re.search(keyWord, page)
            if flag:
                for i in all_key.keys():
                    flag1 = re.search(all_key[i], page)
                    if flag1:
                        keyIdList.append(vulId)
            for vid in keyIdList:
                vulName = re.findall(
                    r"<title>(.+)- 补天 - - 全球最大的漏洞响应平台，帮助企业建立SRC</title>", page)[0]
                vulTime = re.findall(
                    r'<dt>(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})</dt>', page)[0]
                xid = butian_insert(vulName, vulId, vulTime)
                butian_keyword_insert(xid, vid, all_key[vid])
                toMailAddr = getFollowMail(vid)
                sendMail(toMailAddr[0], all_key[vid],
                         'http://butian.360.cn/vul/info/qid/%s' % s)
    except Exception as e:
        print(e)


def main():
    print("start")
    vulDict = getAllVulUrl()
    vulIds, searKey = vulDict[0], vulDict[1]
    butian_last_update(vulIds[0])
    dealSearchKey(searKey)
    dealVulIds(vulIds)


if __name__ == '__main__':
    main()
