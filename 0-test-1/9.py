with open('../../quarioo.test/test.txt') as f:
    n = [sorted(map(int, i.split('\t'))) for i in f.readlines()]

    print(n)
    ans = [i for i in n if sum(i) == 360 and i[0] == i[1] and i[2] == i[3]]
    print(len(ans))