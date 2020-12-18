f = open('fzlt88.txt', 'r')

t = 0
e = 0
pos = 0
ln = 0
for i in f:
    ln += 1
    pos += 3
    if pos > len(i):
        pos = 0
        print('t-e', t, e)
    if ln != 1 and i[pos] == '#':
        t += 1
    else:
        e += 1
print(t, e, ln)
