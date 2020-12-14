# Write a function that returns the length of the shortest contiguous
# sublist whose sum of all elements strictly exceeds n.


min_length([5, 8, 2, -1, 3, 4], 9)  # 2

min_length([3, -1, 4, -2, -7, 2], 4)  # 3
# Shortest sublist whose sum exceeds 4 is: [3, -1, 4]

min_length([1, 0, 0, 0, 1], 1)  # 5

min_length([0, 1, 1, 0], 2)  # -1
