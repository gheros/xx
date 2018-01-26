import paramiko
import re
#远程命令以及监控


class info:
    pkey = '/home/edward/.ssh/id_rsa'
    key = paramiko.RSAKey.from_private_key_file(pkey, password='34@Shidai')  # 有解密密码时,

    def __init__(self, host,):
        self.host =host
        self.ssh = paramiko.SSHClient()
        self.ssh.load_system_host_keys()
    def con(self):
        self.ssh.connect(self.host,33899,"edward",pkey=info.key)#需要try
    def netsave(self):
        stdin, stdout, stderr = self.ssh.exec_command("cat /proc/net/dev")
        out=stdout.readlines()
        # print(stdin)
        # print(stderr.readlines())
        # print(out)
        for a in out:
            print(a)
            r1=re.search('eth0',a)
            if r1 is not None:
                print(a)
    def ping(self):
        stdin, stdout, stderr = self.ssh.exec_command("cat /proc/net/dev")
        out = stdout.readlines()
        print(out)
    def close(self):
        self.ssh.close()


    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #
    # print(stdin)
    # print(stderr.readlines())
    # print (stdout.readlines())
    # stdin, stdout, stderr = ssh.exec_command("cat /proc/meminfo")
    # print(stdin)
    # print(stderr.readlines())
    # print(stdout.readlines())

# # /proc/meminfo 内存
a=info('10.100.62.20')
# b=info('118.193.192.92')
a.con()
a.ping()
a.close()
# a.netsave()
#
# b.con()
# a.close()
# b.netsave()
# b.close()


# "118.193.192.92"