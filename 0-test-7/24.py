import re

num = r'([1-9][0-9]*|0)'
reg = rf'AFD{num}([+*]{num})*'

print(max(len(i.group(1)) for i in re.finditer(f'(?=({reg}))', open('24_19967.txt').readline())))