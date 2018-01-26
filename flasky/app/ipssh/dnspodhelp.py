#从dnspod批量插入IP

import urllib
import json
import re
import time
def _request_(param):
    url ="https://dnsapi.cn/Info.Version -d 'login_token=9a2e50dabb92eda52d8d5828bfa2c1a3&format=json'"
    resp = urllib.request.urlopen(url)
    data = resp.read()
    print(data)
    print("接口调用完成")
    return data

# print(_request_)

#
# import urllib
#
#
# test_data = 'login_token=login_token=40101,9a2e50dabb92eda52d8d5828bfa2c1a3&format=json'
# test_data_urlencode = urllib.urlencode(test_data)
#
# requrl = "https://dnsapi.cn/Info.Version"
# data = parse.urlencode(data).encode('utf-8')
# req = request.Request(url, headers=headers, data=data)
# page = request.urlopen(req).read()
# page = page.decode('utf-8')
#
#
#
# req = urllib2.Request(url = requrl,data =test_data_urlencode)
# print req
#
# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print res
# -*- coding: cp936 -*-
#! /usr/bin/env python3

import urllib.parse

import urllib.request
class analysisdomain:
    @staticmethod
    def dnspodurl():
        # url = 'https://dnsapi.cn/Info.Version'
        # url= 'https://dnsapi.cn/Domain.List'
        url='https://dnsapi.cn/Domain.List'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'login_token': '40101,9a2e50dabb92eda52d8d5828bfa2c1a3',
              'format': 'json',}
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data)
        req.add_header('Referer', 'https://dnsapi.cn/Info.Version')
        response = urllib.request.urlopen(req)
        the_page = response.read()
        return the_page.decode("utf8")

    leboweb=25714250
    @staticmethod
    def RecordList():
        url = 'https://dnsapi.cn/ Record.List'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'login_token': '40101,9a2e50dabb92eda52d8d5828bfa2c1a3',
                  'format': 'json',
                  'domain_id': 25714250}
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data)
        req.add_header('Referer', 'https://dnsapi.cn/Info.Version')
        response = urllib.request.urlopen(req)
        the_page = response.read()
        return(the_page)

    @staticmethod
    def dnspodlog():
        url = 'https://dnsapi.cn/User.Log'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'login_token': '40101,9a2e50dabb92eda52d8d5828bfa2c1a3',
                  'format': 'json', }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data)
        req.add_header('Referer', 'https://dnsapi.cn/Info.Version')
        response = urllib.request.urlopen(req)
        the_page = response.read()
        print(type(the_page))
        a=json.loads(the_page)
        for b in a['log']:
            print(b)
        # print(the_page['log'])
        return the_page.decode("utf8")
        # print(the_page.decode("utf8"))
print(analysisdomain.dnspodlog())
# a=analysisdomain.dnspodurl()
# print(a)
# print(type(a))
# b=eval(a)s
# print(type(b))
# print(b)
import MySQLdb
import configparser
config=configparser.ConfigParser()
config.read("config.ini")


def conall(ip,name):
    conn = MySQLdb.connect(
        host=config.get("mysql", "dbhost"),
        port=int(config.get("mysql", "dbport")),
        user=config.get("mysql", "dbuser"),
        passwd=config.get("mysql", "dbpassword"),
        db=config.get("mysql", "dbname"),
        charset=config.get("mysql", "dbcharset"),
    )
    cur = conn.cursor()
    cur.execute('insert into host(ip,name) values(%s,%s)',(ip,name) )
    a = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return a
# conall('192.168.1.1','aab')
#插入一条数据
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.execute(sqli,('3','Huhu','2 year 1 class','7'))
#插入多条
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
#     ])
#
#
#检查的
# print(analysisdomain.RecordList().decode())
# bb= json.loads(analysisdomain.RecordList().decode())
# print(bb['records'][0])
# print(len(bb['records']))
# conn = MySQLdb.connect(
#     host=config.get("mysql", "dbhost"),
#     port=int(config.get("mysql", "dbport")),
#     user=config.get("mysql", "dbuser"),
#     passwd=config.get("mysql", "dbpassword"),
#     db=config.get("mysql", "dbname"),
#     charset=config.get("mysql", "dbcharset"),
# )
# cur = conn.cursor()
# for a in bb['records']:
#     # print(type(a))
#     r1=re.search('(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',a['value'])
#     if r1 is not None:
#         print(a['name'],a['value'])
#
#         try:
#             cur.execute('insert into host(ip,name) values(%s,%s)', (a['value'], a['name']))
#             a = cur.fetchall()
#         except Exception as e:
#             print(e)
#
# cur.close()
# conn.commit()
# conn.close()


# https://dnsapi.cn/Domain.List















