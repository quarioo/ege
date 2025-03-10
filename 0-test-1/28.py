import math


def find_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


for i in range(1, 10000):
    if len(find_divisors(i)) == 16:
        print(i)
        break
