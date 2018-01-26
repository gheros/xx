import os
import re
def search(path):
    b=[]
    for item in os.listdir(path):
        re1 = re.search('.conf$',item )
        re2 = re.search('^xj',item )
        if re1 is not None and re2 is not None:
            b.append(item[:])
    return b
b=search('/home/edward/svn/tw_xjproxy')
print(search('/home/edward/svn/tw_xjproxy'))
def openfile(filename):
    f = open(filename, 'r')
    f_read = f.read()
    f.close()
    return f_read
def find(param):
    for a in b:
        c=openfile('/home/edward/svn/tw_xjproxy/'+a)
        r1 = re.search(param,c)
        if r1 is not None:
            print (a)
        # print(c)
    #

find('37377z')