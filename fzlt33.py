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


print(find_missing([1, 2, 0]))
print(find_missing([3, 4, -1, 1]))
