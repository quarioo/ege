from ipaddress import ip_network

net = ip_network('218.194.82.148/255.255.255.192', 0)
for i in net.hosts():
    print(i)