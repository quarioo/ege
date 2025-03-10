from ipaddress import *

net = ip_network('83.152.68.115/255.255.224.0', 0)
print([*net.hosts()][-1])