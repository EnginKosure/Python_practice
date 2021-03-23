def pageCount(n, p):
    return min(p//2, max((n % 2 == 0)((n-p-1)//2 + 1), (n % 2 != 0)(n-p)//2))
