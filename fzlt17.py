def sum_double(n):
    return lambda x: x + n if x != n else (x + n)*2


new = sum_double(4)
print(new(4))
print(new(8))
