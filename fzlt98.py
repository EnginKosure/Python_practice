lst, p = [1, 2, 3, 4], [[]]

for _ in lst:
    p = [[a] + b for a in lst for b in p if a not in b]
print(p)
