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

# wooyun最后一条漏洞链接


def wooyun_last():
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "select link from wooyun_last where id = 0"
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


# wooyun更新最后一条漏洞链接
def wooyun_last_update(id):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "update wooyun_last set link = '%s' where id = 0" % id
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


# wooyun插入漏洞
def wooyun_insert(name, link, time):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `wooyun`(`name`,`link`,`time`) VALUES ('%s','%s','%s')" % (
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


# wooyun关键字插入到wooyun_keyword
def wooyun_keyword_insert(wooyun_id, keyword_id, keyword_name):
    connection = connect()
    try:
        cursor = connection.cursor()
        sql = "insert into `wooyun_keyword`(`wooyun_id`,`keyword_id`,`keyword`) VALUES ('%s','%s','%s')" % (
            wooyun_id, keyword_id, keyword_name)
        cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()


# 补天关键字插入wooyun_keyword
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


# 漏洞盒子关键字插入到wooyun_keyword
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


# wooyun_last_update("wooyun-2016-0217469")
# butian_last_update("QTVA-2016-443103")
# loudonghezi_last_update("vulbox-2016-022093")
# wooyun_insert("xx漏洞","wooyun-2016-0217469","2016:1:1")
# butian_insert("xx漏洞fs分多少","QTVA-2016-443103","2016:1:1")
# loudonghezi_insert("xx漏洞发送到","vulbox-2016-022093","2016:1:1")
# data1 = wooyun_last()
# print(data1)
# data2 = butian_last()
# print(data2)
# data3 = loudonghezi_last()
# print(data3)
# print(getkeyWord())
# loudonghezi_keyword_insert("2","67","合肥")
