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


def find_pass2(s):
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
    print(exp)
    print('exp1', exp[n1], exp[n2])
    if exp[n1] == w and exp[n2] == w:
        # print(0)
        return 0
    if exp[n1] == w or exp[n2] == w:

        counter += 1
    print(counter)
    return counter


find_pass2('1-3 a: abcde')

c = 0
for a in f:
    if find_pass2(a) > 0:
        c += 1
print("c", c)
