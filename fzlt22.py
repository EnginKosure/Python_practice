# Perrin sequence
# P(0) P(1) P(2) P(3) P(4) P(5) P(6) P(7) ... P(n)
# 3, 0, 2, 3, 2, 5, 5, 7, ...


def perrin(n):
    lst = [3, 0, 2]
    while len(lst) <= n:
        lst.append(lst[-3]+lst[-2])
    print(lst)
    return lst[n]


perrin(20)

# def perrin(n):
#     lst = [3, 0, 2]
#     for i in range(3, n+1):
#         lst.append(lst[i-3] + lst[i-2])
#     print(lst[n])
#     return lst[n]


# perrin(20)
