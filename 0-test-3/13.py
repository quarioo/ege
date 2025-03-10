from ipaddress import ip_network

net = ip_network('192.138.245.125/255.255.240.0', 0)
print(net.network_address)