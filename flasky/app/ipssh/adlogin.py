from flask_ldap3_login import LDAP3LoginManager
config = dict()

config['LDAP_HOST'] = '172.17.17.201'
config['LDAP_BASE_DN'] = 'dc=stack,dc=tw'
config['LDAP_USER_DN'] = 'CN=someUser,CN=Users,DC=stack,DC=tw'
# a=conn.search('OU=Lebo,dc=stack,dc=tw', '(objectclass=person)')
config['LDAP_GROUP_DN'] = 'ou=Lebo'
config['LDAP_USER_RDN_ATTR'] = 'cn'
config['LDAP_USER_LOGIN_ATTR'] = 'dn'
config['LDAP_BIND_USER_DN'] = None
config['LDAP_BIND_USER_PASSWORD'] = None


ldap_manager = LDAP3LoginManager()
ldap_manager.init_config(config)


response = ldap_manager.authenticate('mailsend', '2018@mail')
print (response.status)