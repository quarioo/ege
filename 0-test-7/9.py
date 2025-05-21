import statistics

ans = []
for l in open('9_11658.txt'):
    l = list(map(int, l.split('\t')))
    c = [l.count(i) for i in l]
    if c.count(3) == 3 and c.count(1) == 4 and \
        statistics.mean(i for i in l if l.count(i) == 3) > statistics.mean(l):
        ans.append(l)

f = [list(map(int, i.split('\t'))) for i in open('9_11658.txt').readlines()]
print(f.index([61, 60, 61, 61, 31, 49, 26]))
