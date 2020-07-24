# Perrin sequence
# P(0) P(1) P(2) P(3) P(4) P(5) P(6) P(7) ... P(n)
# 3, 0, 2, 3, 2, 5, 5, 7, ...


def perrin(n):
    lst = [3, 0, 2]
    while len(lst) <= n:
        lst.append(lst[-3]+lst[-2])
    print(lst)
    return lst[n]


# perrin(20)

# def perrin(n):
#     lst = [3, 0, 2]
#     for i in range(3, n+1):
#         lst.append(lst[i-3] + lst[i-2])
#     print(lst[n])
#     return lst[n]


# perrin(20)

# def perrin(n):
#     A, i = [3, 0, 2], 3
#     while len(A) <= n:
#         A.append(A[i-3]+A[i-2])
#         i += 1
#     print(A[0]*(n == 0)+A[1]*(n == 1)+A[2]*(n == 2)+A[-1]*(n >= 3))
#     return A[0]*(n == 0)+A[1]*(n == 1)+A[2]*(n == 2)+A[-1]*(n >= 3)


# perrin(3)
