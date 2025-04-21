import re

f = open('24.txt').readline()

num = r'([1-7][0-7]*|0)'

reg = rf'{num}(\*{num})*(-{num})*'

print(max(len(i.group(1)) for i in re.finditer(rf'(?=({reg}))', f)))