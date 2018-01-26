









from ldap3 import Server, Connection, ALL

# define the server
s = Server('ldap://172.17.17.201', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s, user='mailsend', password='2018@mail')
print(c.bind())
# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)





#_____________
#
import ldap3
ldapServer = 'ldap://172.17.17.201:389'
domain = 'd1'
userName = 'mailsend'
domainUserName = domain + '\\' + userName
password = '2018@mail'
conn=ldap3.__version__
print(conn)
conn = ldap3.Connection(ldapServer)
conn.open(domainUserName, password)

from ldap3 import Server, Connection, ALL

# define the server
s = Server('ldap://172.17.17.201', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s, user='mailsend', password='2018@mail')
print(c.bind())
# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)



# _________________________________________________
# ldap_config = {
#     'ldap_path': 'ldap://172.17.17.201:389',
#     'base_dn': 'ou=users,dc=ledo,dc=com',
#     'ldap_user': 'uid=reporttest,ou=users,dc=ledo,dc=com',
#     'ldap_pass': '111111.0',
#     'original_pass': '111111.0'
# }
#
# ldap_message = {
#     0: 0, #'ok'
#     1: 1, #'用户名或密码错误'
#     2: 2, #ldap验证异常'
# }
#
# import ldap
# import base64
# import hashlib
# # from config_message import ldap_config, ldap_message
#
#
# class LDAP_API(object):
#
#     _ldap_path = ldap_config['ldap_path']
#     _base_dn = ldap_config['base_dn']
#     _ldap_user = ldap_config['ldap_user']
#     _ldap_pass = ldap_config['ldap_pass']
#     _original_pass = ldap_config['original_pass']
#
#     # 连接ldap服务器
#     def __init__(self):
#
#         try:
#             self.ldapconn = ldap.initialize(self._ldap_path)
#             self.ldapconn.protocal_version = ldap.VERSION3
#             self.ldapconn.simple_bind(self._ldap_user, self._ldap_pass)
#         except ldap.LDAPError as e:
#             print (e)
#
#     # 验证用户登录
#     def ldap_check_login(self, username, password):
#
#         obj = self.ldapconn
#         searchScope = ldap.SCOPE_SUBTREE
#         # searchFilter = '(&(cn='+username+')(userPassword='+password+'))'
#         searchFilter = 'uid=' + username
#
#         try:
#             obj.search(self._base_dn, searchScope, searchFilter, None)  # id--2
#             # 将上一步计算的id在下面运算
#             result_type, result_data = obj.result(2, 0)
#             if result_type != ldap.RES_SEARCH_ENTRY:
#                 return {'status': ldap_message[1], 'data': ''}
#             dic = result_data[0][1]
#             l_realname = dic['sn'][0]
#             l_password = dic['userPassword'][0]
#             md_password = LDAP_API.hash_md5(password)
#             if l_password in (password, md_password):
#                 return {'status': ldap_message[0], 'data': l_realname}
#             else:
#                 return {'status': ldap_message[1], 'data': ''}
#         except ldap.LDAPError as e:
#             return {'status': ldap_message[2], 'data': ''}
#
#     @staticmethod
#     def hash_md5(data):
#         md = hashlib.md5()
#         md.update(str(data))
#         a = md.digest()
#         b = '{MD5}' + base64.b64encode(a)
#         return b
#
# a=LDAP_API
# a.ldap_check_login('edward','34@Shidai')

# _____________________________
# !/usr/bin/python
# -*- coding: utf-8 -*-
# filename: ldap_test.py

# import ldap
#
# '''
# 实现LDAP用户登录验证，首先获取用户的dn，然后再验证用户名和密码
# '''
#
#
# # 获得用户的dn
# def getLdapUserDN(user):
#     l = ldap.initialize(ldapPath)
#     # Set LDAP protocol version used
#     l.protocol_version = ldap.VERSION3
#     l.simple_bind_s(ldapUser, ldapPasswd)
#     # l.simple_bind_s(dn,ldapPasswd)
#
#     searchScope = ldap.SCOPE_SUBTREE
#     searchFiltername = "sAMAccountName"
#     retrieveAttributes = None
#     searchFilter = '(' + searchFiltername + "=" + user + ')'
#     ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
#     result_type, result_data = l.result(ldap_result_id, 1)
#     if (not len(result_data) == 0):
#         r_a, r_b = result_data[0]
#         print
#         r_b["distinguishedName"]
#         return 1, r_b["distinguishedName"][0]
#     else:
#         return 0, ''
#
#
# if __name__ == '__main__':
#     ldapPath = "ldap://172.17.17.201"
#     baseDN = "OU=demo,DC=AD,DC=xx,DC=com"
#     # ldapUser = "root"
#     ldapUser = "CN=admin,OU=demo,DC=AD,DC=xx,DC=com"
#     ldapPasswd = "demo"
#     passwd = "0"
#     dn = getLdapUserDN("test1")[1]
#     print
#     dn
#     my_ldap = ldap.initialize(ldapPath)
#     print
#     my_ldap.simple_bind_s(dn, passwd)