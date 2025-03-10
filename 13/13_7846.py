# работает только на python 3.9.txt+
from ipaddress import *

for mask in range(32, -1, -1):
    net = ip_network(f'193.18.135.201/{mask}', 0)
    if len([ip for ip in net if f'{ip:b}'.count('1') == 19]) == 105:
        print(f'{net.netmask:b}'.count('0'))
