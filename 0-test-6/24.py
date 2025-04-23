import re

f = open('24.txt').readline()
reg = r'(yandex|y4ndex|yand3x|y4nd3x)*(yande|yand|yan|ya|y|y4nde|y4nd|y4n|y4|yand3|y4nd3)'
print(len(max([i.group(1) for i in re.finditer(f'(?=({reg}))', f)], key=len)))