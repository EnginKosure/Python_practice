def swap(a, b, c):
    d = tuple(set((a, b, c)))
    e = (a, b, c)
    print(d)
    print(e)
    # print(e ^ d)


swap(1, 0, 0)  # 1
# a = 1, b = 0, c = b
# return a

swap(1, 3, 1)  # 3
# a = 1, b = 3, c = a
# return b

swap(27, 31, 31)  # 27
# a = 27, b = 31, c = b
# return a
