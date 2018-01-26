from ldap3 import Server, Connection, ALL, NTLM,Tls
import ssl
server = Server('172.16.80.201',use_ssl=True, get_info=ALL)
# conn = Connection(server, auto_bind=True)
# conn = Connection(server, user="Domain\\Edward", password="34@Shidai", authentication='NTLM')
tls_configuration = Tls(validate=ssl.CERT_REQUIRED, version=ssl.PROTOCOL_TLSv1)
server = Server('172.17.17.201',use_ssl=True, get_info=ALL,tls=tls_configuration)
conn = Connection(server)
conn.open

print(conn)
print(conn.extend.standard.who_am_i())
print(server)
print(server.info)