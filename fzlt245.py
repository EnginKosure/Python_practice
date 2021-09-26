array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, -1, 10]


def isValidSubsequence(array, sequence):
    # Write your code here.
    return all(i in array for i in sequence)


print(isValidSubsequence(array, sequence))
