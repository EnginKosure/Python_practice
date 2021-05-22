def first_non_consecutive(arr):
    return [arr[i] for i in range(1, len(arr)) if abs(arr[i] - arr[i-1]) > 1][0]
    # for i in range(1, len(arr)):
    #     if abs(arr[i] - arr[i-1]) > 1:
    #         return arr[i]
    # return None


a = [1, 2, 3, 4, 6, 7, 8]
print(first_non_consecutive(a))
