import ldap3
from ldap3 import Connection, Server, ANONYMOUS, SIMPLE, SYNC, ASYNC,ObjectDef,Reader
# server = Server('172.17.17.201', port=389, use_ssl=False, allowed_referral_hosts=[('server2', True), ('server3', False)])
# s=
# connection = Connection('172.17.17.201', user='cn=mailsend,o=test', password='2018@mail')
# print(connection)
# connection.start_tls()
# connection.bind()
# person = ObjectDef('mailsend', connection)  # read the object class hierarchy schema from the server
# person += ['memberOf', 'entryUUID', 'pwdChangedTime'] # this creates the missing AttrDef in the ObjectDef
# r = Reader(connection, person, 'my_base')
# r.serch()
#!/usr/bin/python3.5
from ldap3 import Server, Connection, NTLM, ALL
print(Server.schema)

# import class and constants
from ldap3 import Server, Connection, ALL

# define the server
s = Server('ldap://172.17.17.201', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s, user='mailsend', password='2018@mail')
c.bind()
# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)
# print(c)

c.unbind()

# import class and constants
from ldap3 import Server, Connection, ALL

# define the server
s = Server('ldap://172.17.17.201', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema

# define the connection
c = Connection(s)  # define an ANONYMOUS connection
c.bind()
# perform the Bind operation
if not c.bind():
    print('error in bind', c.result)




# server = Server('ldap://172.17.17.201', use_ssl=True,get_info=ALL)
#
# conn = Connection(server, user="local\\mailsend", password="2018@mail", authentication=NTLM, auto_bind=True)
# # print(conn)
# # dn = "CN=dctest,CN=Users,DC=home,DC=local"
# a=conn.search('OU=Lebo,dc=stack,dc=tw', '(objectclass=person)')
#
# # print(a)
# # print(conn.entries)
# print(conn.usage)
#
# print('______________')
# s = Server('ldap://172.17.17.201', port = 636, use_ssl = True)
# print(s)
#
# print('________________________')
# server = Server(host = 'ldap://172.17.17.201', port = 636)
# connection = Connection(server, auto_bind = True, version = 3, client_strategy = test_strategy, authentication = SASL,
#                         sasl_mechanism = 'DIGEST-MD5', sasl_credentials = (None, 'username', 'password', None))


# for entry in conn.entries:
#     print(entry)
#
# >>> conn = Connection(server, 'uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', 'Secret123', auto_bind=True)
# >>> conn.search('dc=demo1,dc=freeipa,dc=org', '(objectclass=person)')
# True
# >>> conn.entries


# from ldap3 import Server, Connection
#
# server = Server('ldaps://<AD server address>', use_ssl=True)
# conn = Connection(server, user="<domain>\\<username>", password="<current password>", auto_bind=True)
#
# dn = 'CN=<username>,OU=Users,DC=<dominaname>'
#
# res = conn.extend.microsoft.modify_password(dn, old_password='<current password>', new_password='<new password>')
# print(res)