# Write a method, that will get an integer array as parameter and
# will process every number from this array.
# Return a new array with processing every number of the input-array like this:

# If the number has an integer square root, take this, otherwise square the number.
def sqr_or_not(a):
    return [int(i**.5) if (i**.5).is_integer() == True else int(i**2) for i in a]


print(sqr_or_not([4, 3, 9, 7, 2, 1]))  # [2,9,3,49,4,1]
