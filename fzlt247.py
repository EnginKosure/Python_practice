def find_cons(s):
    return max([len(i) for i in s.split('1')])


print(find_cons('1001101000110'))


def consecutive_zeros(bin_str):
    result = 0
    streak = 0
    for letter in bin_str:
        if letter == "0":
            streak += 1
        else:
            streak = 0
        result = max(result, streak)
    return result
