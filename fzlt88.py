f = open('fzlt88.txt', 'r')

t = 0
e = 0
pos = 1
for i in f:
    pos += 3
    if pos > len(i):
        pos = 1
        print('t-e', t, e)
    if i[pos] == '#':
        t += 1
    else:
        e += 1
print(t, e)
