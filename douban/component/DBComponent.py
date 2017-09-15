# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors


def insertProxy(ip, speed):
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "insert into douban_proxy(ip,speed) \
             values('%s','%f');" % (
        ip, speed)
    try:
        cursor.execute(sql)
        conn.commit()
    except BaseException, e:
        print e
    finally:
        conn.close()


def getAllProxy():
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "select ip from douban_proxy"
    cursor.execute(sql)
    rows = cursor.fetchall()
    proxys = []
    for row in rows:
        proxys.append(row["ip"])
    conn.commit()
    conn.close()
    return proxys


def deleteProxy(ip):
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "delete from douban_proxy where ip='%s'" % ip
    try:
        cursor.execute(sql)
        conn.commit()
    except BaseException, e:
        print e
    finally:
        conn.close()


def insertGroup(name, url):
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "insert into douban_group(name,url) \
             values('%s','%s');" % (
        name, url)
    try:
        cursor.execute(sql)
        conn.commit()
    except BaseException, e:
        print e
    finally:
        conn.close()


def isExistGroup(url):
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "select * from douban_group where url ='%s'" % url
    cursor.execute(sql)
    rows = cursor.fetchall()
    flag = len(rows) > 0
    conn.commit()
    conn.close()
    return flag


def getAllGroup():
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "select * from douban_group"
    cursor.execute(sql)
    rows = cursor.fetchall()
    url_list = []
    for row in rows:
        url_list.append(row["url"])
    conn.commit()
    conn.close()
    return url_list


def addGroupMatch(url):
    conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="douban", charset="utf8",
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    sql = "update  douban_group set matchCount=matchCount+1 \
                where url='%s';" % url
    try:
        cursor.execute(sql)
        conn.commit()
    except BaseException, e:
        print e
    finally:
        conn.close()
