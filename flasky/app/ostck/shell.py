
#
def sconnet():
    import paramiko
    # t = paramiko.Transport(("172.16.20.120", "端口"))
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("172.16.60.120", 22, "root", "34shidai")
    stdin, stdout, stderr = ssh.exec_command("ls -alh")
    print(stdin)
    print(stderr.readlines())
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command("pwd")
    print(stdin)
    print(stderr.readlines())
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command("cd /;pwd;whereis pwd;cd ~;pwd")
    print(stdin)
    print(stderr.readlines())
    print(stdout.readlines())
    stdin, stdout, stderr = ssh.exec_command("pwd")
    print(stdin)
    print(stderr.readlines())
    print(stdout.readlines())

    ssh.close()

# neutron port-create PROD-TC --fixed-ip ip_address=10.200.56.97
#
#
# nova boot --image centos7-1705 --flavor large --nic port-id=977b6e48-1562-4baf-a8ab-6a6e1dcc9d6e --user-data passwd.txt --key-name paul tc-kaijiang02

# sconnet()

x='22222222&&&1'
b=x.split('&')
print(b)