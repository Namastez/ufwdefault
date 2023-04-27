import subprocess

# enable HTTP, HTTPS and SSH traffic
subprocess.run(['ufw', 'allow', 'http'])
subprocess.run(['ufw', 'allow', 'https'])
subprocess.run(['ufw', 'allow', 'ssh'])


# disable all other incoming traffic
subprocess.run(['ufw', 'default', 'deny', 'incoming'])

# allow all outgoing traffic
subprocess.run(['ufw', 'default', 'allow', 'outgoing'])

# enable established connections
subprocess.run(['ufw', 'insert', '1', 'allow', 'in', 'on', 'eth0', 'proto', 'tcp', 'from', 'any', 'to', 'any', 'state', 'RELATED,ESTABLISHED'])

# disable insecure outgoing traffic
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '25', 'proto', 'tcp'])
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '143', 'proto', 'tcp'])
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '110', 'proto', 'tcp'])
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '137:139', 'proto', 'tcp'])
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '137:139', 'proto', 'udp'])
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '445', 'proto', 'tcp'])
subprocess.run(['ufw', 'deny', 'out', 'to', 'any', 'port', '445', 'proto', 'udp'])

#ENABLE UFW
subprocess.run(['ufw', 'enable'])