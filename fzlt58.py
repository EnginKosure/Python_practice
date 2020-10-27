# Given an array of integers where every integer occurs three times
# except for one integer, which only occurs once, find and return the non-duplicated integer.
# For example, given[6, 1, 3, 3, 3, 6, 6], return 1. Given[13, 19, 13, 13], return 19.


def non_duplicated_int(lst):
    return [i for i in lst if lst.count(i) == 1][0]
