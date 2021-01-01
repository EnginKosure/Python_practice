# You are given a list which may contain sublists.
# Your task is to find the depth of the deepest sublist.

# [a] = 1 depth
# [[a]] = 2 depth
# [[[a]]] = 3 depth, etc

def deepest(a):
    x = str(a)
    print(x)
    y = x.count('[')
    print(y)


deepest([1, [2, 3], 4, [5, 6]])  # 2

deepest([[[[[[[[[[1]]]]]]]]]])  # 10

deepest([1, 4, [1, 4, [1, 4, [1, 4, [5]]]]])  # 5
