def rotate(array, k):
    if array is None:
        return None
    length = len(array)
    k = k % length
    return array[length - k:] + array[:length - k]
