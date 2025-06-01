import math
import statistics
from itertools import *
from turtle import *
from random import *

cls = [[], [], []]


def mc_a():
    f = list(list(map(float, i.split('\t'))) for i in open('27A.txt').readlines())
    for x, y in f:
        if y >= 3 * x - 10:
            cls[0].append((x, y))
        elif y > 5:
            cls[1].append((x, y))
        else:
            cls[2].append((x, y))


mc_a()


def draw():
    k = 5
    tracer(0)
    for cl in cls:
        c = random(), random(), random()
        pu()
        for x, y in cl:
            goto(x * k, y * k)
            dot(3, c)

    exitonclick()


def cen(cl):
    res = [[0, 0], 0]
    for cp in cl:
        s = sum(math.dist(p, cp) for p in cl)
        if res[1] < s:
            res = [cp, s]
    return res[0]


cens = [cen(cls[0]), cen(cls[1]), cen((cls[2]))]
cens = list(zip(*cens))
print(statistics.mean(cens[0]) * 10_000, statistics.mean(cens[1]) * 10_000)


cls = [[], [], [], [], []]
def mc_b():
    f = list(list(map(float, i.split())) for i in open('27B.txt').readlines())
    for x, y in f:
        if x < 10 and y > x:
            cls[0].append((x, y))
        elif x < 10:
            cls[1].append((x, y))
        elif x > 10 and y > x:
            cls[2].append((x, y))
        elif y > 10:
            cls[3].append((x, y))
        else:
            cls[4].append((x, y))

mc_b()
cens = [cen(cls[0]), cen(cls[1]), cen((cls[2])), cen(cls[3]), cen(cls[4])]
cens = list(zip(*cens))
print(statistics.mean(cens[0]) * 10_000, statistics.mean(cens[1]) * 10_000)
