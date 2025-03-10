import ipaddress

for i in range(1, 100):
    try:
        net = ipaddress.ip_network(f'20.24.96.0/{i}', 1)
        if ipaddress.ip_address('20.24.110.42') in net:
            print(i)
            break
    except Exception:
        pass