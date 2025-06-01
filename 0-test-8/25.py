for i in range(0, 10**9, 999):
    s = str(i)
    if s.startswith('13') and s.endswith('9') and s[-4:-2] == '57':
        print(i, i // 999)