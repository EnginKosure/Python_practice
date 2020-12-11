# Create a function that takes a list lst and a number N and
# returns a list of two integers from lst whose product is that of the number N.

# Try doing this with 0(N) time complexity.
# No duplicates.
# In the list there can be multiple solutions so return
# the first full match that you have found.
# If any doubts please refer to the comments section.

def two_product(arr, n):
    return [int(n/i) for i in arr if n/i in arr]


print(two_product([1, 2, -1, 4, 5], 20))  # [4, 5]

print(two_product([1, 2, 3, 4, 5], 10))  # [2, 5]

print(two_product([100, 12, 4, 1, 2], 15))  # []
