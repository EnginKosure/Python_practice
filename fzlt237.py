x = "a=1, b=2, c=3, d=4"
# { 'a': 1, 'b': 2, 'c': 3, 'd': 4}


def str_to_hash(x):
    print([i.replace('=', ':') for i in x.split(',')])


str_to_hash(x)


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))  # {'a': 1, 'b': 2, 'c': 3}
