# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values
# of the array so that all the Rs come first, the Gs come second,
# and the Bs come last. You can only swap elements of the array.
# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].


def segregate_values(arr):
    return sorted(arr, reverse=1)


x = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
print(segregate_values(x))
