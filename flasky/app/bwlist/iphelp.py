import re
import os
from socket import inet_aton
from struct import unpack, pack

import configparser
config=configparser.ConfigParser()
config.read("config.ini")
def search(path, name):
    b = []
    for item in os.listdir(path):
        re1 = re.search(name, item)
        if re1 is not None:
            b.append(item)
    return b  # 将.conf结尾的文件加入b

def openfile(filename):
    f = open(filename, 'r')
    f_read = f.read()
    f.close()
    return f_read
class iphelp:
    #路径配置
    path=config.get("svn","svnlocal")
    #检索出该路径下所有的首字母为大写的文件，并返回所有文件名
    @staticmethod
    def checksuper():
        a=search(iphelp.path,'')
        b=[]
        for i in a:
            if i[:-5].isupper()==True:b.append(i)
        return(b)
    #子网掩码转换函数，输入值为通配符，转换值为子网掩码
    @staticmethod
    def exchange_maskint(mask_int):
      bin_arr = ['0' for i in range(32)]
      for i in range(mask_int):
        bin_arr[i] = '1'
      tmpmask = [''.join(bin_arr[i * 8:i * 8 + 8]) for i in range(4)]
      tmpmask = [str(int(tmpstr, 2)) for tmpstr in tmpmask]
      return '.'.join(tmpmask)
    #ip对比函数，输入值为需检测的ip，文件配置的IP，以及对应的通配符
    @staticmethod
    def isInSameNetwork(ip_add1, ip_add2, mask):
        ip1_num, = unpack("!I", inet_aton(ip_add1))
        ip2_num, = unpack("!I", inet_aton(ip_add2))
        mask_num, = unpack("!I", inet_aton(mask))
        if ip1_num & mask_num != ip2_num & mask_num:
            return False
        else:
            return True
    #遍历读取所有文件的值文件,并且返回IP地址以及通配符数组
    # a=checksuper()
    # for i in a
    #     openfile(i)
    @staticmethod
    def readfileall():
        b=[]
        c=[]
        a=iphelp.checksuper()
        for i in a:
            # print(i)
            b.append(openfile(iphelp.path+'/'+i))
            for i in b:
                r1=re.findall(r'(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)/[1-9][0-9]{0,1}',i)
                if r1 is not None:
                    for x in r1:
                        c.append(x)
        return(c)
    #检查素有文件的IP，并做判断是否存在
    @staticmethod
    def checkall(inip):

        a=iphelp.readfileall()
        for i in a:
            x=i.split('/')
            b=iphelp.isInSameNetwork(inip,x[0],iphelp.exchange_maskint(int(x[1])))
            if b==True:return b
            else:return False

    #传入文件读取的文件名检查文件字符串是否有国家，并返回国对应家名数组
    @staticmethod
    def countycheck(filename):
        sparam=openfile(iphelp.path+'/xjdeny/'+filename+'.conf')
        r = re.findall(r'^include xjdeny/(.*).conf', sparam)
        r1 = re.findall(r'include xjdeny/(.*).conf', sparam)
        if r != []: r1.append(r[0])
        return r1
    def __init__(self, country):
        self.country =country
        # self.rparam=openfile(domain.path+name+'.conf','r').read().encode()

        # self.wpath = openfile(iphelp.path + '/xjallow/' + country + '.conf')
    #检测国家文件对应的ip，是否为其子网，如果是，返回true，否则返回false
    def checkbip(self,ipaddr):
        cpath = openfile(iphelp.path + '/xjdeny/' + self.country + '.conf')
        c=[]
        r1 = re.findall(r'((?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?));', cpath)
        if ipaddr in r1: return True
        r2 = re.findall(r'(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)/[1-9][0-9]{0,1}', cpath)
        if r2 is not None:
            for x in r2:
                c.append(x)
        for i in c:
            x = i.split('/')
            b = iphelp.isInSameNetwork(ipaddr, x[0], iphelp.exchange_maskint(int(x[1])))
            if b == True:
                return True
        return False


    def checkwip(self,ipaddr):
        cpath = openfile(iphelp.path + '/xjallow/' + self.country + '.conf')
        c=[]
        r1=re.findall(r'((?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?));',cpath)
        if ipaddr in r1:return True
        r2=re.findall(r'(?:25[0-5]\.|2[0-4]\d\.|[01]?\d\d?\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)/[1-9][0-9]{0,1}', cpath)
        if r2 is not None:
            for x in r2:
                c.append(x)
        for i in c:
            x = i.split('/')
            b = iphelp.isInSameNetwork(ipaddr, x[0], iphelp.exchange_maskint(int(x[1])))
            if b == True:
                return True
        return False










    # def paramsplite(param):
    #     a=param.split('/')
    #     print(a)
    #     print(type(a[0]),a[1])
    #     b=a[0].split('.')
    #
    #     print(b)
    # def fomatip(ip):
    #     if ip.find("/") == -1:
    #         print (ip + "/255.255.255.255")
    #         return ip + "/255.255.255.255"
    #     else:
    #         ipcheck=ip.split('/')
    #         print(ipcheck)
#
# print(iphelp.readfileall())
# print(iphelp.checkall('118.238.192.0'))
# print(iphelp.checksuper())
print(iphelp("HK").checkbip("222.167.1.1"))
print(iphelp("HK").checkbip("1.1.1.1"))
# print(iphelp("OUR").checkwip("119.82.254.50"))

# paramsplite('118.240.0.0/15')
# fomatip('118.240.0.0/24')
# '118.240.0.0/15'
            # i=i.split('deny ')
            #
            # print(i[1])
    # print(b)
    # for i in b:
    #     print(i)

    # print(b)


# readfile()


# print(checksuper())
# a=checksuper()
# print(openfile('/home/edward/fileconf/xjdeny/KR.conf'))
