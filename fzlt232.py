d = {0: 'np1', 1: 'np2', 2: 'np3', 3: 'np4', 4: 'np5'}

s = {'np1',  'np2',  'np3',  'np4', 'np5'}
for i in range(len(d)):
    print(d[i])


a = [1, 2, 3, 4, 5]
del a[1::2]
print(a)


def apple(x):
    return ("Help yourself to a honeycomb Yorkie for the glovebox.", "It's hotter than the sun!!")[int(x)**2 > 1000]
