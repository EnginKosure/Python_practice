a = [1, 2, 3, 4, 5]
del a[::2]
print(a)


b = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
transpose = [list(i) for i in zip(*b)]
print(transpose)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
