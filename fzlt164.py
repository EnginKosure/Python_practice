def strange_math(n, k):
    return sorted(range(n+1), key=str).index(k)
