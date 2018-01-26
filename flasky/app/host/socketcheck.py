import socket
import MySQLdb
import configparser
import json
import urllib.parse
import urllib.request
import re
# from ..bwlist.mysqldb import con
from app.bwlist.mysqldb import con
config=configparser.ConfigParser()
config.read("config.ini")


def conall(param):
    conn = MySQLdb.connect(
        host=config.get("mysql", "dbhost"),
        port=int(config.get("mysql", "dbport")),
        user=config.get("mysql", "dbuser"),
        passwd=config.get("mysql", "dbpassword"),
        db=config.get("mysql", "dbname"),
        charset=config.get("mysql", "dbcharset"),
    )
    cur = conn.cursor()
    cur.execute(param)
    a = cur.fetchall()
    cur.close()
    conn.commit()
    conn.close()
    return a
#向dnspod取对应的值

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
    # bb=json.loads(analysisdomain.RecordList())
    # @staticmethod
    # def relist(RecordList):
    #     b=[[]]
    #     for a in RecordList['records']:
    #         # print(type(a))
    #         r1 = re.search('(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])', a['value'])
    #         if r1 is not None:
    #             print(a['name'], a['value'])
    #             b.append(a['name'], a['value'])
    #     print(b)
        # print(the_page.decode("utf8"))
class check:
    @staticmethod
    def checkip(hostname,port):
        b=''
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(1)
        try:
            sk.connect((hostname, port))
            # print('服务器:'+hostname+'端口:'+str(port)+'正常')
            b=('端口:'+str(port)+'正常')
        except Exception as e:
            # print('服务器:'+hostname+'端口:'+str(port)+'不正常 原因:'+str(e))
            b=('Error:端口:'+str(port)+'不正常 原因:'+str(e))
        sk.close()
        return (b)


    #检测ip的类
    # def check(self,hostname, port):
    #     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     sk.settimeout(1)
    #     try:
    #         sk.connect((hostname, port))
    #
    #         # print('服务器:'+hostname+'端口:'+str(port)+'正常')
    #         check.b.append('服务器:' + hostname + '端口:' + str(port) + '正常')
    #
    #
    #     except Exception as e:
    #
    #         # print('服务器:'+hostname+'端口:'+str(port)+'不正常 原因:'+str(e))
    #         check.b.append('服务器:' + hostname + '端口:' + str(port) + '不正常 原因:' + str(e))
    #     sk.close()
   #所有代理机器检测
    leboweb=json.loads(analysisdomain.RecordList())
    @staticmethod
    def checkallp(port):
        out=[]
        a=conall("select ip from host where `group`='1'")
        for x in a:
            out.append(check.checkip(x[0],port))
        return out
    @staticmethod
    def checkurlall(port):
        out=[]
        bb=check.leboweb
        for a in bb['records']:
            b=[a['name'],a['value']+check.checkip(a['value'], port)]
            out.append(b)
        return out
    #判断A字符串是否包含B字符串的静态方法
    @staticmethod
    def remod(param, param2):
        r1 = re.search(param, param2)
        if r1 is not None:
            return param
        else:
            False

    @staticmethod
    def scan(port):

        a=con('select sname,lname,comid from blacklist')
        b=check.checkurlall(port)
        c=[]
        import copy
        e=copy.copy(b)
        # print(b)
        for j in a:
            for i in b:
                if check.remod(j[0],i[0])==j[0]:
                    #将元素拼接入c同时移除b中的值
                    d = [j[0], j[1], j[2], i[0],i[1]]
                    c.append(d)
                    # print(i)
                    try:e.remove(i)
                    except:continue
                # if i[0]==j[0]:
                #     d=[i[0],i[1],i[2],j[1]]
                #     c.append(d)
        # print(e)
        # newdata=
        i=0
        while i<len(e):
            e[i].insert(0,' ')
            e[i].insert(0, ' ')
            e[i].insert(0, ' ')
            i=i+1
        c.extend(e)
        return c
    #未完毕,按照公司二码检测
    @staticmethod
    def hostcheck(param):
        str='select sname,lname,comid from blacklist where comid='+"'"+param+"'"
        print(str)
        a = con(str)
        print(a)
        b = check.checkurlall(80)
        c = []
        import copy
        e = copy.copy(b)
        # print(b)
        for j in a:
            for i in b:
                if check.remod(j[0], i[0]) == j[0]:
                    # 将元素拼接入c同时移除b中的值
                    d = [j[0], j[1], j[2], i[0], i[1]]
                    c.append(d)
                    # print(i)
                    try:
                        e.remove(i)
                    except:
                        continue

                    # if i[0]==j[0]:
                    #     d=[i[0],i[1],i[2],j[1]]
                    #     c.append(d)
        # print(e)
        # newdata=
        i = 0
        while i < len(e):
            e[i].insert(0, ' ')
            e[i].insert(0, ' ')
            e[i].insert(0, ' ')
            i = i + 1
        c.extend(e)
        return c
    #主机检测
    @staticmethod
    def hostportcheck(host):
        a=host+check.checkip(host,80)
        b=host+check.checkip(host,443)
        return a,b

        # 主机检测
    @staticmethod
    def hostportcheckint(host,port):
        a = host + check.checkip(host, port)
        return a



print(analysisdomain.RecordList().decode())
# bb= json.loads(analysisdomain.RecordList())
# print(bb['records'][0])
# print(bb['records'][0]['name'],bb['records'][0][])
# print(len(bb['records']))
# # check.checkip('118.193.192.92', 80)
# # check.checkip('172.16.60.120', 443)
# print(check.checkallp(80))
# print(check.checkallp(443))
# print(check.checkurlall(80))
# print(check.scan(80))
# print(check.hostportcheck('www.baidu.com'))
# print(check.hostportcheckint('www.baidu.com',80))