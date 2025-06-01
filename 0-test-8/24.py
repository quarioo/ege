import re

f = open('24.txt').readline()

reg = r'([BC][BC]A)*'

print(max(len(i.group(1)) for i in re.finditer(f'(?=({reg}))', f)))