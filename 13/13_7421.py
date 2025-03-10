from ipaddress import *

for mask in range(32, -1, -1):
    net1 = ip_network(f'123.20.103.136/{mask}', 0)
    net2 = ip_network(f'123.20.103.151/{mask}', 0)
    if net1 != net2:
        print(int(f'{int(net1.netmask):032b}'[-8:], 2))