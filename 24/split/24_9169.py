f = open('../data_kompege/24_9169.txt').readline().replace('BAD', '*').replace('FAT', '*').split('*')

print(len(min([''.join(f[i:i+2]) for i in range(len(f))], key=len)) + 9)