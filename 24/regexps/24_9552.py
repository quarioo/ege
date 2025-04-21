import re

f = open('../data_kompege/24_9552.txt').readline()

reg = rf'(PC|CSGO)*'
print(max([len(i.group(1)) for i in re.finditer(rf'(?=({reg}))', f)]))