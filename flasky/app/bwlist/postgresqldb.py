import psycopg2
# 数据库连接参数
#整张表
def conall(param):

    conn = psycopg2.connect(database="leboadmin", user="leboadmin", password="34gp@shidai***^^^", host="10.100.62.20", port="5432")
    cur = conn.cursor()

    cur.execute('select * from '+param)
    a = cur.fetchall()        # all rows in table
    cur.close()
    conn.commit()
    conn.close()
    return a
# 查询单条数据
def con(param):
    conn = psycopg2.connect(database="leboadmin", user="leboadmin", password="34gp@shidai***^^^", host="10.100.62.20", port="5432")
    cur = conn.cursor()
    cur.execute(param)
    a=cur.fetchone()
    cur.close()
    conn.commit()
    conn.close()
    return a
# print(conall('blacklist'))


