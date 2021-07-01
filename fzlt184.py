from math import sqrt
import re
from math import ceil
n = 6
print('\n'.join('* ' * i for i in range(1, n + 1)))


def new_avg(arr, newavg):
    next = ceil(newavg * (len(arr) + 1) - sum(arr))
    if next <= 0:
        raise ValueError
    return next


len(re.findall('python', 'python is a programming language. python is python.'))


def bonus(arr, s):
    bonus = s / sum(1 / x for x in arr)
    return [round(bonus / x) for x in arr]


def order_food(lst):
    keys = [x['meal'] for _, x in enumerate(lst)]
    return {key: keys.count(key) for key in keys}


def largest_pair_sum(numbers):
    return sum(sorted(numbers, reverse=True)[:2])


def find_outlier(integers):
    mods = [n % 2 for n in integers]
    return integers[mods.index(0)] if sum(mods[:3]) > 1 else integers[mods.index(1)]


def chess_knight(cell):
    x, y = ord(cell[0]) - ord('a') + 1, int(cell[1])
    moves = {(-2, -1), (-2, 1), (-1, 2), (1, 2),
             (2, 1), (2, -1), (1, -2), (-1, -2)}
    return sum(0 < x + i < 9 and 0 < y + j < 9 for i, j in moves)


def add_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Input arguments are not of equal length")
    return [array1[i] + array2[i] for i in range(len(array1))]


def decipher_this(string):
    words = string.split()
    res = []
    for word in words:
        word = chr(int(''.join([ch for ch in word if ch.isdigit()])))\
            + ''.join([ch for ch in word if ch.isalpha()])
        if len(word) == 3:
            word = word[:1] + word[2] + word[1]
        elif len(word) > 3:
            word = word[:1] + word[-1] + word[2:-1] + word[1]
        res.append(word)
    return ' '.join(w for w in res)


def presents(a):
    res = [0] * len(a)
    for x, i in enumerate(a, 1):
        res[i - 1] = x
    return res


def presents1(a):
    return [a.index(i)+1 for i in range(1, len(a)+1)]


def solve(a, b):
    rotated = {"0": "0",
               "1": "1",
               "6": "9",
               "8": "8",
               "9": "6"}
    count = 0
    for x in range(a, b):
        rot = [rotated[d] for d in str(x) if d in rotated][::-1]
        try:
            if int("".join(rot)) == x:
                count += 1
        except Exception:
            continue
    return count


def heron(*args):
    s = sum(args) / 2
    return round(sqrt(s * (s - args[0]) * (s - args[1]) * (s - args[2])), 2)


def t_area(t_str):
    return (t_str.count("\n") - 2) ** 2 / 2


def order(sentence):
    spl = sentence.split(" ")
    n = 1
    ns = ""
    for loop in range(len(spl)):
        for a in spl:
            if str(n) in a:
                ns = ns + (a)+" "
        n += 1
    return ns[:-1]
