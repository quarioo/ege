from ipaddress import *

net = ip_network('102.141.0.0/255.255.192.0')

ans = 0
for ip in net:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 7 == 0 and ip.endswith('1011'):
        ans += 1

print(ans)