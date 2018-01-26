import os
import re
import configparser
from .svnhelp import down,up,writeup
# from app.domain.svnhelp import down,up,writeup
config=configparser.ConfigParser()
config.read("config.ini")

#以下为两个测试函数,搜索方法
def search(path):
    b=[]
    for item in os.listdir(path):
        re1 = re.search('.conf$',item )
        re2 = re.search('^xj',item )
        if re1 is not None and re2 is not None:
            b.append(item[2:-5])
    return b#将.conf结尾的文件加入b
#读取文件内容
def openfile(filename):
    f = open(filename, 'r')
    f_read = f.read()
    f.close()
    return f_read

# def domain(sparam,doparam):
#     iter1 = re.search(r'allow ' + doparam + ';', sparam)
#     print()
#
#     return sparam


#域名类
class domain:
    #配置区
    path=config.get('domain','path')
    path1=config.get('domain','path1')
    #配置区结束，考虑以后是否修改为配置文件的区域
    #第一层读取文件，公共数据
    rparam1 = openfile(path1 + '.conf').encode()

    #静态方法，处理字符串,前台qcxj读取并筛选出需要字符串
    @staticmethod
    def xjqc(name):
        aa = re.findall(b'server *{\n *listen *80;\n *server_name *(.*);\n *error_log */data/logs/error/'+name.encode()+b'\..*',domain.rparam1)
        return aa
    #读取文件，并筛选出后台需要字符串,后台nginx配置
    @staticmethod
    def readpro(name):
        rparam = openfile(domain.path + 'xj' + name + '.conf').encode()
        aa = re.findall(b'.*server *{\n *listen *80;\n *server_name *(.*);\n *include *xjdeny.*', rparam)
        return aa
    #文件的写入方法,后台路径
    @staticmethod
    def write(name,prarm):
        f=open(domain.path+'xj'+name+'.conf','w')
        f.write(prarm.decode())
        f.close()
    #文件写入方法，前台路径
    @staticmethod
    def xjqcwrite(prarm):
        f = open(domain.path1 +'.conf', 'w')
        f.write(prarm.decode())
        f.close()
        #注意，文件写入完毕后，需要重新加载文件，避免数据不同步
        domain.rparam1=openfile(domain.path1 + '.conf').encode()
    #检查重复值
    @staticmethod
    def double(name,param):
        param=b' '+param
        r1 = re.search(b' '+name.encode(), param)
        return r1
    #判断输入是否为域名,检测函数参数
    @staticmethod
    def domainre(param):
        r1 = re.match(b'[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?', param.encode())
        if r1 is not None:
            return 1

    def __init__(self, name,):
        self.name =name
        # self.rparam=openfile(domain.path+name+'.conf','r').read().encode()
        #后台文件数据
        self.rparam=openfile(domain.path+'xj'+name+'.conf').encode()

    def readconf(self):
        #读取nginx数据
        aa = domain.readpro(self.name)
        # print(self.name)
        if aa!=[]:
            bb=aa[0].decode().split(' ')
            return bb
        return '不存在该配置或配置文件有误'
    def insert(self,param):
        down()
        param = param.lower()
        if domain.domainre(param) is None:
            return '不是域名，请检查输入'
        # 分割文件字符串
        # print(type(param))
        aa = domain.readpro(self.name)
        r1 = re.search(b' ' + param.encode() + b'( |;)', self.rparam)
        r2 = re.search(b' ' + param.encode() + b'( |;)', domain.rparam1)
        # bb=domain.double(param,aa[0])
        if r1 is not None and r2 is not None:return param+'该域名已存在'
        #后台文件存在，写入前台
        if r1 is not None and r2 is None:
            xjqc = domain.xjqc(self.name)
            # print(xjqc)
            xjqcb = re.finditer(xjqc[0], domain.rparam1)
            for i in xjqcb:
                a = i
            c = domain.rparam1[:a.span()[1]] + b' ' + param.encode() + domain.rparam1[a.span()[1]:]  # 为新拼接的字符串
            # print(c)
            domain.xjqcwrite(c)  # 文件写入操作
            up(self.name, param)

            return (param + '已添加至后台文件尾')
        #前台文件存在，写入后台
        if r1 is None and r2 is not None:
            bb = re.finditer(aa[0], self.rparam)
            # print(bb)
            for i in bb:
                a = i
            b = self.rparam[:a.span()[1]] + b' ' + param.encode() + self.rparam[a.span()[1]:]  # 为新拼接的字符串
            # print(b)
            domain.write(self.name, b)  # 文件写入操作
            # 前台文件操作完毕
            up(self.name,param)
            return (param + '已添加至前台文件尾')
        #以下是整段的文件操作，两个文件的写入操作
        if aa!=[]and len(aa)==1:
            #后台文件操作
            bb = re.finditer(aa[0], self.rparam)
            # print(bb)
            for i in bb:
                a=i
            b = self.rparam[:a.span()[1]] + b' ' + param.encode() + self.rparam[a.span()[1]:]#为新拼接的字符串
            # print (b)
            domain.write(self.name,b) #文件写入操作
            #前台文件操作
            xjqc=domain.xjqc(self.name)
            # print(xjqc)
            xjqcb = re.finditer(xjqc[0], domain.rparam1)
            for i in xjqcb:
                a=i
            c = domain.rparam1[:a.span()[1]] + b' ' + param.encode() + domain.rparam1[a.span()[1]:]#为新拼接的字符串
            # print(c)
            domain.xjqcwrite(c) #文件写入操作
            # 前台文件操作完毕
            up(self.name, param)
            return (param+'已添加至文件尾')
        return '添加失败，请联系管理人员检查'
        # for i in bb:
        #     b=i
        #     print(i.span())
        # print(type(b.span()[1]))
        # print(self.rparam[:b.span()[1]])
        # a=self.rparam[:b.span()[1]]+b' '+param.encode()+self.rparam[b.span()[1]:]
        # print(a)
        # return a

    @staticmethod
    def scan():
        from ..bwlist.mysqldb import con
        a=con('select sname,lname,comid from blacklist')
        #查看客户数据
        return a

    def delete(self, param):
        #转换为小写
        down()
        param = param.lower()
        if domain.domainre(param) is None:
            return '不是域名，请检查输入'

        # print(self.rparam)
        aa = re.search(b' '+param.encode()+b'( |;)', self.rparam)
        bb = re.search(b' ' + param.encode()+b'( |;)', domain.rparam1)
        # print(aa)
        # print(bb)
        print(aa)
        print(bb)
        if aa is not None and bb is not None:
            a1 = self.rparam[:aa.span()[0]] + self.rparam[aa.span()[1] - 1:]
            b1 = domain.rparam1[:bb.span()[0]] + domain.rparam1[bb.span()[1] - 1:]
            domain.write(self.name,a1)
            domain.xjqcwrite(b1)
            up(self.name, param)
            return (param+'删除成功')
        if aa is not None and bb is None:
            print('11111111111')
            return '11111111111'
        return ('不存在该域名或删除失败')

    def check(self,param):
        #全部转换为小写
        param=param.lower()
        if domain.domainre(param) is None:
            return '不是域名，请检查输入'
        aa = re.finditer(b' ' + param.encode() + b'( |;)', self.rparam)
        bb = re.finditer(b' ' + param.encode() + b'( |;)', domain.rparam1)
        for a in aa:
            for b in bb:
                if a is not None and b is not None:return (param+'均存在该域名')
                if a is not None:return (param+'仅后台文件存在该域名,可以进行添加')
                if b is not None: return (param + '仅前台文件存在该域名，可以进行')
                # if a is not None:return

        return '该域名不存在,可以进行添加'

    def docat(self):
        aa = domain.readpro(self.name)
        b=aa[0].decode().split(' ')
        return b




        # [0 - 9a - zA - Z]([-.\w]*[0 - 9a - zA - Z])*(: (0 - 9) *)*(\ / ?)(
        # [a - zA - Z0 - 9\-\.\?\, \'\/\\\+&amp;%\$#_]*)?
        # if aa is not None and bb is not None




        # for a in aa:
        #     print(a)
        #






#测试方法
# test=search('/home/edward/svn/tw_xjproxy/')
#print(domain.rparam1)
#print(test)
#for a in test:
#    domain(a).readconf()
#    print(domain.xjqc(a))




# print(domain('mgyx').rparam1)
# print(domain('mgyx').readconf())
# print(domain('mgyx').check('bb.bb'))
# print(domain('mgyx').delete('bb.bb'))
# print(domain('mgyx').insert('bb.bb'))

# print(domain.scan())

# print(domain.xjqc('mgyx'))
# domain.rparam1
# domain('amblh').insert('www')

# print(domain(openfile('/home/edward/fileconf/tw_xjproxy/test.conf'),'www.baidu.com'))
