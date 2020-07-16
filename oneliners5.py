# The Data
unsorted = [33, 2, 3, 45, 6, 54, 33]


# The One-Liner
def q(l): return q([x for x in l[1:] if x <= l[0]]) + \
    [l[0]] + q([x for x in l if x > l[0]]) if l else []
# q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []


# The Result
print(q(unsorted))  # [2, 3, 6, 33, 33, 45, 54]
