from ipaddress import *

net = ip_network('112.154.132.0/255.255.252.0')

ans = 0
for ip in net:
    ip = f'{ip:b}'
    s1 = ip[:16].count('1')
    s2 = ip[16:].count('1')
    if s2 % 2 == 1 and s1 <= s2:
        ans += 1

print(ans)