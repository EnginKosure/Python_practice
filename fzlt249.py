def all_equal(l):
    return len(list(set(l))) <= 1


def all_equal1(items):
    return all(item1 == item2 for item1 in items for item2 in items)


x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b % 2 != 0]

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[2][1])


tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)
