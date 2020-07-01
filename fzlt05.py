def advanced_sort(lst):
    return [[i]*lst.count(i) for i in dict.fromkeys(lst)]


print(advanced_sort([7, 'a', 7, 'b', 10, 'a', 'b', 'c', '10']))

print(dict.fromkeys([7, 'a', 7, 'b', 10, 'a', 'b', 'c', '10']))
# {7: None, 'a': None, 'b': None, 10: None, 'c': None, '10': None}


# print(['a']*3)  # ['a', 'a', 'a]
# print([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, ].count(3))  # 6
