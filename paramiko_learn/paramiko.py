import paramiko

hostname = <hidden>
username = <hidden>
password = <hidden>
cmd = 'yum update -y'
s = paramiko.SSHClient()
s.load_system_host_keys()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
s.connect(hostname, username=username,password=password,allow_agent=False,look_for_keys=False)
stdin,stdout,stderr=s.exec_command(cmd)
cmd_result = stdout.read(), stderr.read()
for line in cmd_result:
    print line,
s.close()
