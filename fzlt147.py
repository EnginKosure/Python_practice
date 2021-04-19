def operations(x, y):
    return x+y, x*y, '3th param'


res1, res2, res3 = operations(4, 4)

print(res1, res2, res3[:3])
