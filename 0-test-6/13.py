from ipaddress import ip_network

net = ip_network('212.192.32.96/255.255.255.224', 0)

ans = 0
for ip in net:
    s = f'{ip:b}'[-8:]
    if '111' not in s and '000' not in s:
        ans += 1

print(ans)