from ipaddress import *

net = ip_network('172.16.128.0/255.255.192.0')
print(len([ip for ip in net if sum(map(int, f'{int(ip):032b}')) % 2 == 0]))