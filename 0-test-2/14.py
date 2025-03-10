# использовал range вместо букв
import string

for x in string.printable[:25]:
    s = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if s % 24 == 0:
        print(s // 24)