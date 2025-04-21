f = open('../data_kompege/24_10105.txt').readline().split('T')

print(max(len(''.join(f[i:i + 102])) for i in range(len(f))) + 100)