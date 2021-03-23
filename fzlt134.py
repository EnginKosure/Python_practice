def pageCount1(n, p):
    return min(p//2, max((n % 2 == 0)*((n-p-1)//2 + 1), (n % 2 != 0)*(n-p)//2))


def pageCount(n, p):
    if n % 2 == 0 and n-1 == p:
        return min(p//2, 1)
    else:
        return min(p//2, (n-p)//2)


print(pageCount(5, 4))
print(pageCount(20, 12))


print(pageCount1(5, 4))
print(pageCount1(20, 12))
