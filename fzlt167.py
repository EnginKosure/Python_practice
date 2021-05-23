# You will be given an array and a limit value.
# You must check that all values in the array are
# below or equal to the limit value. If they are,
# return true. Else, return false.
def small_enough(array, limit):
    return all([x <= limit for x in array])


print(small_enough([101, 45, 75, 105, 99, 107], 107))
