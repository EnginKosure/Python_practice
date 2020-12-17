from itertools import combinations
f = open('fzlt87.txt', 'r')


def test(val):
    return sum(val) == 2020


def find_num(n):
    return 2020-int(n)


def find_num2(n):
    x = 2020-int(n)
    return x


c = 0
l = []
for a in f:
    l.append(int(a))

res = list(filter(test, list(combinations(l, 3))))
print("res", res)
print(res[0][0]*res[0][1]*res[0][2])
