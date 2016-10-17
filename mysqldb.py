
# coding:utf-8
import pymysql.cursors


# 数据库链接
def connect():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',  # 数据库密码
                                 db='jiankong',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# 漏洞关键字{1:'安徽',2:'合肥'}


def getkeyWord():
    dict1 = {}
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select id,name from keyword"
        cursor.execute(sql)
        data = cursor.fetchall()
    finally:
        connection.close()
    for i in data:
        dict1[i['id']] = i['name']
    return dict1

# print(getkeyWord())

# cnvd最后一条漏洞链接


def cnvd_last():
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select link from cnvd_last where id = 0"
        cursor.execute(sql)
        data = cursor.fetchall()
    finally:
        connection.close()
    return data[0]['link']


# 补天最后一条漏洞链接
def butian_last():
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select link from butian_last where id = 0"
        cursor.execute(sql)
        data = cursor.fetchall()
    finally:
        connection.close()
    return data[0]['link']

# 漏洞盒子最后一条漏洞链接


def loudonghezi_last():
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select link from loudonghezi_last where id = 0"
        cursor.execute(sql)
        data = cursor.fetchall()
    finally:
        connection.close()
    return data[0]['link']


# cnvd更新最后一条漏洞链接
def cnvd_last_update(id):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "update cnvd_last set link = '%s' where id = 0" % id
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()


# 补天更新最后一条漏洞链接
def butian_last_update(id):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "update butian_last set link = '%s' where id = 0" % id
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()


# 漏洞盒子更新最后一条漏洞链接
def loudonghezi_last_update(id):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "update loudonghezi_last set link = '%s' where id = 0" % id
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()


# cnvd插入漏洞
def cnvd_insert(name, link, time):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `cnvd`(`name`,`link`,`time`) VALUES ('%s','%s','%s')" % (
            name, link, time)
        cursor.execute(sql)
        id = cursor.lastrowid
        connection.commit()
    finally:
        connection.close()
    return id


# 补天插入漏洞
def butian_insert(name, link, time):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `butian`(`name`,`link`,`time`) VALUES ('%s','%s','%s')" % (
            name, link, time)
        cursor.execute(sql)
        id = cursor.lastrowid
        connection.commit()
    finally:
        connection.close()
    return id


# 漏洞盒子插入漏洞
def loudonghezi_insert(name, link, time):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `loudonghezi`(`name`,`link`,`time`) VALUES ('%s','%s','%s')" % (
            name, link, time)
        cursor.execute(sql)
        id = cursor.lastrowid
        connection.commit()
    finally:
        connection.close()
    return id


# cnvd插入数据到cnvd_keyword
def cnvd_keyword_insert(cnvd_id, keyword_id, keyword_name):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `cnvd_keyword`(`cnvd_id`,`keyword_id`,`keyword`) VALUES ('%s','%s','%s')" % (
            cnvd_id, keyword_id, keyword_name)
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

# 补天插入数据到cnvd_keyword


def butian_keyword_insert(butian_id, keyword_id, keyword_name):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `butian_keyword`(`butian_id`,`keyword_id`,`keyword`) VALUES ('%s','%s','%s')" % (
            butian_id, keyword_id, keyword_name)
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

# 漏洞盒子插入数据到cnvd_keyword


def loudonghezi_keyword_insert(loudonghezi_id, keyword_id, keyword_name):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `loudonghezi_keyword`(`loudonghezi_id`,`keyword_id`,`keyword`) VALUES ('%s','%s','%s')" % (
            loudonghezi_id, keyword_id, keyword_name)
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

# 获取发件人邮箱,返回['smtp服务器','smtp端口','邮箱账户','邮箱密码']


def getMailSet():
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select * from mail where id = 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        mailset = []
        mailset.append(data[0]['smtpserver'])
        mailset.append(data[0]['smtpport'])
        mailset.append(data[0]['usermail'])
        mailset.append(data[0]['userpass'])
        return mailset
    finally:
        connection.close()

# 获取关注某个关键字的用户的邮箱,传入关键字id


def getFollowMail(keyword_id):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select * from keyword_follow where keyword_id = " + \
            str(keyword_id)
        cursor.execute(sql)
        data = cursor.fetchall()
        useMail = []
        for i in data:
            if int(i['mail_send']) == 1:
                useMail.append(getUserMail(i['uid']))
        return useMail
    finally:
        connection.close()


def getUserMail(uid):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select * from user where id = " + str(uid)
        cursor.execute(sql)
        data = cursor.fetchall()
        return data[0]['email']
    finally:
        connection.close()

# cnvd_last_update("cnvd-2016-0217469")
# butian_last_update("QTVA-2016-443103")
# loudonghezi_last_update("vulbox-2016-022093")
# cnvd_insert("xx漏洞","cnvd-2016-0217469","2016:1:1")
# butian_insert("xx漏洞fs分多少","QTVA-2016-443103","2016:1:1")
# print(loudonghezi_insert("xx漏洞发送到","vulbox-2016-022093","2016:1:1"))
# data1 = cnvd_last()
# print(data1)
# data2 = butian_last()
# print(data2)
# data3 = loudonghezi_last()
# print(data3)
# print(getkeyWord())
# loudonghezi_keyword_insert("2","67","合肥")
# print(getMailSet())
# print(getFollowMail(99))
