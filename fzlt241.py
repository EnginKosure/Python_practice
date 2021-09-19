def contain_all_rots(strng, arr):
    if strng == '':
        return True
    return [sorted(i) for i in arr].count(sorted(strng)) >= len(strng)


def contain_all_rots1(s, l):
    return all(s[i:]+s[:i] in l for i in range(len(s)))


def even_numbers(arr, n):
    return list(filter(lambda x: not x % 2, arr))[-n:]
