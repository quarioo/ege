from string import printable

ans = 0
for x in printable[:14]:
    for y in printable[:14]:
        n = int(f'14{y}5{x}2', 14) + int(f'31{x}2{y}3', 14)
        s = int(x, 14) + int(y, 14)
        if n % 9 == 0 and ans <= s:
            ans = s
            print(n // 9)