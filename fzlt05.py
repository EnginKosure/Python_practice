def advanced_sort(lst):
    return [[i]*lst.count(i) for i in dict.fromkeys(lst)]
