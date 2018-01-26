import datetime
import os
import re
import shutil
import time

# from .mysqldb import conall
# from .mysqldb import conall
from app.bwlist.mysqldb import conall

# from .readfile import search, openfile, makefile, search_insert, wsearch_insert,deny,allow
from app.bwlist.readfile import search, openfile, makefile,deny,allow
# from .svnhelp import down, up,writeup
from app.bwlist.svnhelp import down, up,writeup

import configparser
config=configparser.ConfigParser()
config.read("config.ini")

blackpath1=config.get('black','path')
# "/home/edward/svn1/xjdeny"
#文件备份路径
pathbak=config.get('black','pathbak')
# "/home/edward/fileconf/xjdeny"

filelock=0
class admin:
    def __init__(self, name):
        return

class user_client:
    def __init__(self, name):
        self.name = name
    #查看客户
    def scan(self):
        f1 = search(blackpath1, ".conf$")
        f2 = []
        for i in f1:
            f2.append(i[:-5])
        con1=list(conall('blacklist'))
        con=[]
        for i in con1:
            con.append(list(i))
        f3=[]
        for a in con:
            f3.append(a[1])
        return con
    #创建客户操作
    def insert(self):
        f1 = search(blackpath1, ".conf$")
        print(f1)
        for a in f1:
            if self.name+'.conf'==a:return "已存在该客户，无法增加"
        f1.append(self.name+'.conf')
        os.mknod(blackpath1+'/'+self.name+'.conf')

        return "增加客户成功"
    # 删除客户操作
    def delete(self):
        makefile(pathbak + '/.bak')
        shutil.move(blackpath1+'/'+self.name+'.conf',pathbak+'/.bak/' + self.name+'.conf'+str(datetime.datetime.now()))
        return "删除客户成功"
    def recover(self):
        return "recover"

class blacklist(user_client):
    def __init__(self,name,):
        self.name = name
    #查看黑名单操作
    def scan(self):
        down()
        f=open(blackpath1+'/'+self.name+'.conf','r')
        f2=''
        for line in f:
            r1=re.search('^deny (([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',line)
            r2=re.search('^include ',line)
            r3 = re.search('^deny all', line)
            if r1 is not None:
                # print(line)
                # print(type(line))
                f2=f2+line[5:]
            if r2 is not None:
                f2 = f2 + line
            if r3 is not None:
                f2 = f2 + line

        f2=f2.replace(' ','').replace('\n','')
        # print(f2)
        f2=f2
        f2=f2.split(';')
        if f2[len(f2)-1]=='':f2.pop(len(f2)-1)
        return f2

        return blackname+"删除成功"
    # 添加黑名单操作
    def insert(self,blackname):
        down()
        r1=re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',blackname)
        if r1 is None:return '不是IP地址'
        tmp=deny(openfile(blackpath1 + '/'+self.name+'.conf'), blackname)
        f2=tmp[0]
        print(f2)
        if f2 == openfile(blackpath1 + '/'+self.name+'.conf'): return tmp[1]
        f = open(blackpath1 + '/' + self.name + '.conf', 'w')
        f.write(f2)
        f.close()
        #开发版本注意注释，以免上传
        up(self.name, blackname)
        return tmp[1]
#以下是白名单操作
class whitelist(user_client):
    def __init__(self,name,):
        self.name = name
    #查看白名单操作
    def scan(self):
        down()
        f=open(blackpath1+'/'+self.name+'.conf','r')
        f2=''
        for line in f:
            r1=re.search('^allow (([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',line)
            # r2=re.search('^include xjallow',line)
            r2 = re.search('^include ', line)
            r3 = re.search('^deny all', line)

            if r1 is not None:
                # print(line)
                # print(type(line))
                f2=f2+line[5:]
            if r2 is not None:
                f2 = f2 + line
            if r3 is not None:
                f2 = f2 + line
            # if r2 is not None:
            #     f2 = f2 + line

        f2=f2.replace(' ','').replace('\n','')
        # print(f2)
        f2=f2
        f2=f2.split(';')
        if f2[len(f2)-1]=='':f2.pop(len(f2)-1)

        return f2
    #删除白名单操作
        # up()
        return blackname+"删除成功"
    # 添加白名单操作
    def insert(self,blackname):
        down()
        r1=re.search(r'(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5])',blackname)
        if r1 is None:return '不是IP地址'
        tmp=allow(openfile(blackpath1 + '/'+self.name+'.conf'), blackname)
        f2=tmp[0]
        if f2==openfile(blackpath1 + '/'+self.name+'.conf'):return tmp[1]
        f = open(blackpath1 + '/' + self.name + '.conf', 'w')
        f.write(f2)
        f.close()
        #开发版本不用上传,
        up(self.name,blackname)
        return tmp[1]
    # def
    #
    # f=search(blackpath1,".conf")
    # print(f)

#
# if __name__ == "__main__":
#     b = blacklist('ambc')
#     print(b.scan())
# a=user_client("ambc")
# print(a.scan())
# # # print(a.name)
# # # print(a.insert())
# # # # print(a.delete())
# b=blacklist('ambc')
# # xhjc.conf 包含incloud
# # print( b.scan())
# # # print(b.scan())
# # print(b.delete('192.168.1.1'))
# # print(b.insert('118.193.202.59'))
# print( b.scan())
#
# # # # # # TH
# # b=whitelist('xhjc')
# # print( b.scan())
# print(b.insert('192.168.1.1'))
# print( b.scan())