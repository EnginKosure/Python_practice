def strange_math(n, k):
    return sorted(range(n+1), key=str).index(k)


print(strange_math(11, 2))  # 4
strange_math(15, 5)  # 11
strange_math(15, 15)  # 7
