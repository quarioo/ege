from statistics import *
from random import *
from turtle import *


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


def mc_a():
    for i in open('27-25a.txt'):
        x, y = map(float, i.split())
        if y > 5:
            cls[0].append((x, y))
        else:
            cls[1].append((x, y))


def ce(cl):
    ans = [[0, 0], 10000000]
    for p in cl:
        s = sum(max(abs(p[0] - cp[0]), abs(p[1] - cp[1])) for cp in cl)
        if ans[1] > s:
            ans = [p, s]

    return ans[0]


cls = [[], []]
mc_a()
ces = list(zip(*[ce(cls[0]), ce(cls[1])]))

print(int(mean(ces[0]) * 10_000), int(mean(ces[1]) * 10_000))

def mc_b():
    for i in open('27-25b.txt'):
        x, y = map(float, i.split())
        if y < -2.5:
            cls[0].append((x, y))
        elif x < 3:
            cls[1].append((x, y))
        else:
            cls[2].append((x, y))


cls = [[], [], []]
mc_b()
# draw()
ces = list(zip(*[ce(cls[0]), ce(cls[1]), ce(cls[2])]))
print(int(mean(ces[0]) * 10_000), int(mean(ces[1]) * 10_000))