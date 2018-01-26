import os
import re

def search(path,name):
    b=[]
    for item in os.listdir(path):
        re1 = re.search(name,item )
        if re1 is not None:
            b.append(item)
    return b#将.conf结尾的文件加入b
#读取文件内容
def openfile(filename):
    f = open(filename, 'r')
    f_read = f.read()
    f.close()
    return f_read
#创建文件夹
def makefile(name):
    try:
        os.mkdir(name)
    except Exception as e:
        return

#指定行插入文件第一个参数为文件，第二个参数为诶行数，第三个参数为行数，第四个功能为是否换行换行加'\n'即可，不换行加''
def insertdata(name,int,param,fun):
    fp = open(name,'r')
    lines = []
    for line in fp:  # 内置的迭代器, 效率会很高哦
        lines.append(line)
    fp.close()
    lines.insert(int, param+fun)  # 在第n行的下一行插入，参数化，fun参数是功能参数，主要是维护尾部加入换行符
    s = ''.join(lines)
    fp = open(name, 'w')
    fp.write(s)
    fp.close()
#寻找文件对应匹配行,并插入所需的字符串
#该匹配规则为如果有deny则会再deny后插入，如果没有，将会再alllow下一行插入，如果文件为空，则会直接插入
# def search_insert(sparam,iparam):
#     iter1 = re.finditer(r'(\n(deny|allow) (([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]);)', sparam)
#     r1=re.search('include', sparam)
#     b=[]
#     double = re.finditer(r'(deny ' + iparam + ')', sparam)
#     c=[]
#
#     for a in double:
#
#         c.append(a.span)
#     if c!=[]:return iparam
#     # print(iter1)
#     for i in iter1:
#         b.append(i.span())
#     if b ==[]:
#         b = 'deny '+iparam + ';\n' + sparam
#         return b
#     print(b)
#     print(b[len(b)-1][1])
#     c=''
#     c=sparam[0:b[len(b)-1][1]]+'\ndeny '+iparam+';'+sparam[b[len(b)-1][1]:]
#     return c
#白名单匹配规则
#白名单匹配规则
# def wsearch_insert(sparam,iparam):
#     iter1 = re.finditer(r'(\nallow (([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]);)', sparam)
#     r1=re.search('include', sparam)
#     #去重
#     b=[]
#     double = re.finditer(r'(allow ' + iparam + ')', sparam)
#     #去重函数结束
#     c=[]
#     for a in double:
#         print(a)
#         c.append(a.span)
#     if c!=[]:return iparam#重复就返回
#     # print(iter1)
#     for i in iter1:
#         # print(i)
#         b.append(i.span())
#     if b ==[]:
#         b = 'allow '+iparam + ';\n' + sparam
#         return b#为空就返回
#     print(b)
#     print(b[len(b)-1][1])
#     c=''
#     c=sparam[0:b[len(b)-1][1]]+'\nallow '+iparam+';'+sparam[b[len(b)-1][1]:]
#     return c#正常返回
# 操作deny
def deny(sparam,iparam):
    t=sparam
    stat=[]
    iter1 = re.search(r'allow ' + iparam+'(;\n|;)', t)
    if iter1 is not None:
        t=t[:iter1.span()[0]]+'\n'+t[iter1.span()[1]+1:]
        stat.append('存在白名单'+iparam+'已删除该白名单')

    iter2 = re.search(r'include xjallow', t)
    if iter2 is not None:
        # print(iter2)
        # from .iphelp import iphelp
        from app.bwlist.iphelp import iphelp
        # from .iphelp import iphelp
        country = countycheckw(sparam)
        for coun in country:
            # print(coun)
            x = iphelp(coun).checkwip(iparam)
            # 如果国家文件中含有该字段，或者判定为允许
            # print(x)
            if x == True:
                iter3 = re.search(r'deny ' + iparam + '(;\n|;)', t)
                # print(iter3)
                if iter3 is not None:
                    if iter3.span()[0]>=iter2.span()[0]:
                        tmp=t[iter3.span()[0]:iter3.span()[1]]
                        t=t[:iter3.span()[0]]+t[iter3.span()[1]:]
                        t=t[:iter2.span()[0]]+tmp+t[iter2.span()[0]:]
                        stat.append('国家允许名单包含' + iparam + '目前已增调整拒绝策略到白名单前')
                        return t,stat
                if iter3 is None:
                    t=t[:iter2.span()[0]]+'deny '+iparam+';'+t[iter2.span()[0]:]
                    stat.append('国家允许名单包含' + iparam + '目前已增加该拒绝策略到白名单前')
                    return t, stat
    # iter3=re.search(r'(^|\n *)deny ' + iparam + ';', t)
    iter4 = re.search(r'include xjdeny',t)
    if iter4 is not None:
        # from .iphelp import iphelp
        # from .iphelp import iphelp
        from .iphelp import iphelp
        country = countycheckb(sparam)
        for coun in country:
            # print(coun)
            x = iphelp(coun).checkbip(iparam)
            if x ==True:
                stat.append("国家策略包含拒绝策略"+iparam)
                return t,stat
            # if x ==False:
        iter3 = re.search(r'deny all(;\n|;)', t)
        if iter3 is None:
            t='deny ' + iparam + ';\n' + t
            stat.append('国家黑名单不包含,且不存在deny all全局拒绝' + iparam + '已增再首行加该拒绝策略')
            return t, stat
    iter5 = re.search(r'deny all(;\n|;)', t)

    if iter5 is not None:
        stat.append('全局deny all存在' + iparam + '无需拒绝')
        return t,stat
    #不存在denyall且不存在deny ip ,而且再国家检查中未出现相关ip子网
    iter3 = re.search(r'deny ' + iparam + '(;\n|;)', t)
    if iter5 is None and iter3 is None:
        t = 'deny ' + iparam + ';\n' + t
        stat.append('不存在deny,' + iparam + '已进行添加')
        return t, stat


    if iter3 is not None:
        stat.append('存在deny,' + iparam + '无需添加')
    return t,stat


def allow(sparam,iparam):
    t=sparam
    stat=[]
    iter1 = re.search(r'deny '+iparam+'(;\n|;)', t)
    if iter1 is not None:
        # print(iter1.span())
        # print(t)
        t = t[:iter1.span()[0]] + t[iter1.span()[1]:]
        # print(t)
        stat.append('存在黑名单' + iparam + '已删除该黑名单')
    iter2 = re.search(r'allow ' + iparam + ';', t)
    if iter2 is not None:
        stat.append('存在白名单' + iparam + '无需添加')
        return t,stat
    else:
        iter3 = re.search(r'include xjallow', t)
        if iter3 is not None:
            # from .iphelp import iphelp
            from app.bwlist.iphelp import iphelp
            country = countycheckw(t)
            for coun in country:
                x = iphelp(coun).checkwip(iparam)
                if x ==True:
                    stat.append('include allow包含'+iparam+'无需添加')
                    return t,stat
    iter4=re.search(r'deny all', t)
    if iter4 is not None:
        t = 'allow ' + iparam + ';\n' + t
        stat.append('存在deny all，已再首行增加' + iparam)
        return t,stat
    iter5 = re.search(r'include xjdeny', t)
    if iter5 is not None:
        # from .iphelp import iphelp
        from app.bwlist.iphelp import iphelp
        country = countycheckb(t)
        for coun in country:
            x = iphelp(coun).checkbip(iparam)
            if x == True:
                t = 'allow ' + iparam + ';\n' + t
                stat.append('incloud xjdeny包含该IP ，已再首行增加允许' + iparam)
                return t,stat
        if iter4 is None:
    #这段不应该加入Flase判断
            # if x==False:
            if iter4 is None:
                stat.append('incloud xjdeny不包含该IP，且不存在deny all ，默认为允许' + iparam)
                return t,stat
    if iter4 is None and iter5 is None:
        stat.append('不存在deny xjdeny,且不存在deny all，默认为允许' + iparam)
        return t,stat
    iter6 = re.search(r'allow ' + iparam + '(;\n|;)', t)
    if iter6 is not None:
        stat.append("存在allow"+iparam+"无需添加")
    # if iter6 is not None and
    return t,stat
# def allowall(sparam,string):
#
#
#     iparam=1
#     allow(sparam, iparam)

    # iter3 = re.search(r'(^|\n *)include xjdeny', sparam)
    # iter4 = re.search(r'(^|\n *)include', sparam)
    # iter5 = re.search(r'(^|\n *)deny all', sparam)
    # from app.bwlist.iphelp import iphelp
    # b=countycheckb(sparam)
    #
    #
    #
    #
    # #allow是否存在
    # if iter1 is not None:
    #     #是，已经存在
    #     return sparam
    # #否
    # else:
    #     #判断deny中是否存在ip
    #     if iter2 is not None:
    #         t=t[:iter2.span()[0]]+t[iter2.span()[1]+1:]
    #         return t
    #     else:
    #         if iter5 is not None:
    #             if iter3 is not None:
    #                 t=sparam[:iter4.span()[0]]+'allow '+iparam+';\n'+sparam[iter4.span()[0]:]
    #                 return t
    #             else:
    #                 t = 'allow ' + iparam + ';\n' + sparam
    #                 return t
    #         else:
    #             if iter3 is not None:
    #                 for i in b:
    #                     if iphelp(i).checkip(iparam)==True:
    #                         t = 'allow ' + iparam + ';\n' + sparam
    #                         return t
    #             else:
    #                 return t
#denycountry黑名单国家检查
def countycheckb(sparam):
    r=re.findall(r'^include xjdeny/(.*).conf', sparam)
    r1=re.findall(r'include xjdeny/(.*).conf', sparam)
    if r !=[]:r1.append(r[0])
    return r1
def countycheckw(sparam):
    r=re.findall(r'^include xjallow/(.*).conf', sparam)
    r1=re.findall(r'include xjallow/(.*).conf', sparam)
    if r !=[]:r1.append(r[0])
    return r1

# print(deny(openfile('/home/edward/svn1/xjdeny/test.conf'),'103.255.172.0'))
print(allow(openfile('/home/edward/svn1/xjdeny/amxj.conf'),'222.167.1.1'))
print(deny(openfile('/home/edward/svn1/xjdeny/amxj.conf'),'205.209.129.1'))
# print(allow(openfile('/home/edward/svn1/xjdeny/amxj.conf'),'1.1.1.1'))
# print(countycheckb(openfile('/home/edward/svn1/xjdeny/amxj.conf')))
# print(countycheckw(openfile('/home/edward/svn1/xjdeny/amxj.conf')))
#ip判断规则以及转换二进制
# print(bin(1))




#后边优化
# def deny1(sparam,iparam):
#     iter1 = re.match(r'deny ' + iparam, sparam)
#     iter2 = re.match(r'allow ' + iparam + ';', sparam)


    # if iter1 is not None:return ('已存在IP')
    # for a in iter2:
    #     print(a)
    # for a in iter3:
    #     print(a)

    # r1 = re.search('include', sparam)
    # print(r1)



# print()

# def writefile(file,param)
#
# # insertdata('data.txt',4,'11111111111111')
# fp = open('/home/edward/fileconf/xjdeny/pj.conf','r')
# f=fp.read()
# print(f)
# r1=re.search('deny',f)
# print(r1)

# print(openfile('/home/edward/fileconf/xjdeny/pj.conf')[392:411])
# print(openfile('/home/edward/fileconf/xjdeny/pj.conf')[411])
# wsearch_insert(openfile('/home/edward/fileconf/xjdeny/pj.conf'),'aaaaaaaabbbbbcc')
# print(search_insert(openfile('/home/edward/fileconf/xjdeny/ambjl.conf'),'192.168.1.1'))
# print(allow(openfile('/home/edward/fileconf/xjdeny/yldc.conf'),'202.58.99.82'))
# print(allowall(openfile('/home/edward/fileconf/xjdeny/yldc.conf'),'192.168.1.1 192.168.1.2 192.168.1.3'))

# print(wsearch_insert(openfile('/home/edward/fileconf/xjdeny/ambjl.conf'),'192.168.1.1'))