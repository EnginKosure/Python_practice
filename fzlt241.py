def contain_all_rots(strng, arr):
    if strng == '':
        return True
    return [sorted(i) for i in arr].count(sorted(strng)) >= len(strng)
