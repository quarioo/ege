
for k in range(1, 100):
    for i in range(1, 100):
        for j in range(1, 100):
            s = ((j + j + k) / 2) + ((i + i + 2 * k) / 2)
            print(j, i, k, s)
            break