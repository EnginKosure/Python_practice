f = open('fzlt86.txt', 'r')


def find_pass(s):
    counter = 0
    x = s.split(':')
    print('x', x)
    w = x[0][-1]
    print(w)
    exp = x[1]
    y = x[0].split('-')
    print('y', y)
    n1 = int(y[0])
    z = y[1].split(" ")
    print('z', z)  # ['11', 't']
    n2 = int(z[0])
    if n2 >= exp.count(w) >= n1:
        counter += 1
    print(counter)
    return counter


c = 0
for a in f:
    if find_pass(a) > 0:
        c += 1
print("c", c)
