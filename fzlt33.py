# This is an interview question asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input[3, 4, -1, 1] should give 2. The input[1, 2, 0] should give 3.
# You can modify the input array in-place.


def find_missing(array):
    array = sorted(array)
    array_pos = [i for i in array if i >= 0]
    control = list(range(array_pos[0], array_pos[-1]+1))
    return array_pos[-1] + 1 if control == array_pos else list(set(control).difference(array_pos))[0]


def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i


def check(my_array):
    for i in range(max(my_array)+2):
        if i > 0 and not i in my_array:
            return i


print(find_missing([1, 2, 0]))
print(find_missing([3, 4, -1, 1]))

print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([3, 2, -2, -2, -3, -3, -4, -4, 4, -1, 1]))

print(check([3, 2, -2, -2, -3, -3, -4, -4, 4, -1, 1, 6, 4, 3]))
