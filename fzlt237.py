x = "a=1, b=2, c=3, d=4"
# { 'a': 1, 'b': 2, 'c': 3, 'd': 4}


def str_to_hash(x):
    y = [j.split(':') for j in (i.replace('=', ':') for i in x.split(','))]
    z = [item for sublist in y for item in sublist]
    v = [int(i) if z.index(i) % 2 else i for i in z]
    # print([item for sublist in y for item in sublist])
    it = iter(v)
    res_dct = dict(zip(it, it))
    return res_dct


print(str_to_hash(x))
# flat_list = [item for sublist in t for item in sublist]

# def Convert(lst):
#     res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return res_dct


# # Driver code
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))  # {'a': 1, 'b': 2, 'c': 3}


# def Convert(a):
#     it = iter(a)
#     res_dct = dict(zip(it, it))
#     return res_dct

# # Driver code
# lst = ['a', 1, 'b', 2, 'c', 3]
# print(Convert(lst))
