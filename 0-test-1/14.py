x = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50

x = -x
a = []

while x > 0:
    a = [x%49] + a
    x //= 49

print(sum(a))
