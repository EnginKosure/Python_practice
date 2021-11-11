import numpy as np
w, h = 8, 5
Matrix = [[0 for x in range(w)] for y in range(h)]

print(Matrix)


Matrix[0][0] = 1
Matrix[0][1] = 9

print(Matrix)


np_arr = np.ones((4, 6))
print(np_arr)


n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m
