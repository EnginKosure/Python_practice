f = open('fzlt87.txt', 'r')


def find_num(n):
    return 2020-int(n)


c = 0
l = []
for a in f:
    l.append(int(a))

    x = find_num(a)
    if x in l:
        print(x)
        c = x*(2020-x)
print("c", c)
