with open('17 (1).txt') as f:
    n = [int(i) for i in f.readlines()]

    ans = 0
    min_prod = 0

    for i in range(1, len(n)):
        pair = [n[i], n[i - 1]]

        if i < 3:
            neigb = [(n[i + 1], n[i + 2])]
        elif i > len(n) - 3:
            neigb = [(n[i - 3], n[i - 2])]
        else:
            neigb = [(n[i - 3], n[i - 2]), (n[i + 1], n[i + 2])]

        if all(sum(pair) > sum(j) for j in neigb) and all(sum(j) > 0 for j in neigb) and sum(pair) > 0:
            ans += 1
            min_prod = min(min_prod, pair[0] * pair[1])

print(ans, min_prod)