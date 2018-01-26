import os
import MySQLdb
import configparser
config=configparser.ConfigParser()
config.read("config.ini")

# [mysql]
# dbhost=172.16.60.120
# dbport=3306
# dbname=lebo
# dbuser=root
# dbpassword=34@shidai
# dbcharset=utf8
# host = config.get("mysql", "dbhost"),
# port = config.get("mysql", "dbport"),
# user = config.get("mysql", "dbuser"),
# passwd = config.get("mysql", "dbpassword"),
# db = config.get("mysql", "dbname"),
# charset = config.get("mysql", "dbcharset"),
#语句查询
def con(param):
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
        # a=cur.fetchone()
        a=cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return a
#整张表
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
        cur.execute('select * from '+param)
        a = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return a

# tmp=conall('blacklist')
# print(tmp)
# print(tmp)
# print(tmp[0][1])
#
# # print(con('select * from blacklist where sname="ambc"'))
# b=con('select * from blacklist where sname="ambjl"')
# for a in b:
#         print(a)




# class dbhelp():


#创建数据表
# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

# #插入一条数据
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")


#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")
#插入一条数据
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.execute(sqli,('3','Huhu','2 year 1 class','7'))

#一次插入多条记录
# sqli="insert into student values(%s,%s,%s,%s)"
# cur.executemany(sqli,[
#     ('3','Tom','1 year 1 class','6'),
#     ('3','Jack','2 year 1 class','7'),
#     ('3','Yaheng','2 year 2 class','7'),
#     ])


