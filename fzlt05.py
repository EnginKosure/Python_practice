def advanced_sort(lst):
    return [[i]*lst.count(i) for i in dict.fromkeys(lst)]


print(advanced_sort([7, 'a', 7, 'b', 10, 'a', 'b', 'c', '10']))

print(dict.fromkeys([7, 'a', 7, 'b', 10, 'a', 'b', 'c', '10']))

print(['a']*2)
