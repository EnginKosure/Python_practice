def cut_the_ropes(arr):
    res = [len(arr)]
    arr = sorted(arr)
    while len(set(arr)) > 1:
        arr = list(filter(bool, map(lambda x: x - arr[0], arr)))
        res.append(len(arr))
    return res
