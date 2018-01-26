from ldap3 import Server, Connection, ALL

# define the server
def login(username,passwd):
    s = Server('ldap://172.17.17.201', get_info=ALL)  # define an unsecure LDAP server, requesting info on DSE and schema
# define the connection
    c = Connection(s, user=username, password=passwd)
# perform the Bind operation
    a=c.bind()

    c.unbind()
    return a



print(login('mailsend','2018@mail'))
