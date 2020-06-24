from time import time
start_time = time()
D = 'acc?7??sss?3rr1??????5'
A = '0' + D + '0'
B, k, C, E = [], 0, [], []
for i, n in enumerate(A):
    if n.isdigit():
        B.append((A[k:i+1], A[k:i+1].count('?'), int(A[k])+int(A[i])))
        k = i
for i in B:
    if i[2] == 10:
        C.append(i)
        if i[1] == 3:
            E.append(i)
print(len(C) != 0 and len(C) == len(E))
print(f'---Time: {time()-start_time} seconds')
