# Create a function that takes a list lst and a number N and
# returns a list of two integers from lst whose product equals N.
def two_product(l, n):
    x = [int(n/i) for i in l if i != 0]
    s_x = set(x)
    s_l = set(l)
    intersection = s_x.intersection(s_l)
    if len(intersection) >= 2:
        return(list(intersection))
    return None


def two_product1(l, n):
    for x in l:
        if n/x in l and l.index(x) > l.index(n/x):
            return[int(n/x), x]


print(two_product1([1, 2, -1, 4, 5], 20))  # [4, 5]

print(two_product1([1, 2, 3, 4, 5], 10))  # [2, 5]

print(two_product1([100, 12, 4, 1, 2], 15))  # None
