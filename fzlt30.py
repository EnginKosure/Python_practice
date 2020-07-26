# def permute(xs, low=0):
#     if low + 1 >= len(xs):
#         yield xs
#     else:
#         for p in permute(xs, low + 1):
#             yield p
#         for i in range(low + 1, len(xs)):
#             xs[low], xs[i] = xs[i], xs[low]
#             for p in permute(xs, low + 1):
#                 yield p
#             xs[low], xs[i] = xs[i], xs[low]


# for p in permute([1, 2, 3, 4]):
#     print(p)

def permute(numbers):
    result = [[]]
    for n in numbers:
        my_perms = []
        for p in result:
            for i in range(len(p)+1):
                my_perms.append(p[:i] + [n] + p[i:])
                result = my_perms
    return result


xx = [1, 2, 3]

print(permute(xx))


lst = [1, 2, 3]
p = [[]]

for i in range(len(lst)):
    p = [[a] + b for a in lst for b in p if a not in b]
print(p)
