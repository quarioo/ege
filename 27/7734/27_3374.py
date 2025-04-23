from math import *
from turtle import *
from statistics import *
from random import *

f = [list(map(float, i.split("\t"))) for i in open('27-59a.txt').readlines()]

def mc(sp):
    cl = [sp]
    for cp in cl:
        for p in f:
            if dist(cp, p) <= 1:
                cl.append(p)
                f.remove(p)

    return cl

cls = []
while f:
    cls.append(mc(f.pop()))


def draw():
    tracer(0)
    up()
    for cl in cls:
        c = random(), random(), random()
        for x, y in cl:
            goto(x * 20, y * 20)
            dot(3, c)
    update()
    exitonclick()

cls = [cl for cl in cls if len(cl) >= 30]

def ce(cl):
    r = ([10**7, 10**7], float('inf'))
    for p in cl:
        s = sum(dist(p, i) for i in cl)
        if r[1] > s:
            r = (p, s)

    return r[0]

ces = list(zip(*[ce(i) for i in cls]))
print(mean(ces[0]) * 100_000)
print(mean(ces[1]) * 100_000)
