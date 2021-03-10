def rotate(array, k):
    if array is None:
        return None
    length = len(array)
    k = k % length
    return array[length - k:] + array[:length - k]


a = [1, 2, 3, 4, 5, 6, 7]
print(rotate(a, 3))  # [5, 6, 7, 1, 2, 3, 4]
