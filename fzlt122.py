# Given n pairs of parentheses, write a code to generate all combinations of
# well-formed (valid for Python) parentheses.
# For example, given n = 3,
# a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


import array as arr
n = 3
r = ["()"]
for _ in range(n-1):
    r = [i[0:j+1]+"()"+i[j+1:] for i in r for j in range(len(i))]
    r = list(dict.fromkeys(r))
print(r)

print((1, 2) + (3, 4))
print(2**2**2**2)
a = 1
b = ++a
print(b is a)

My_Array = arr.array('i', [1, 2, 3, 4])
My_list = [1, 'abc', 1.20]
print(My_Array)
print(My_list)
# Write a python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125


def exp_table(n):
    for i in range(n):
        print(f'{i+1} {(i+1)**0} {(i+1)**1} {(i+1)**2} {(i+1)**3}')


exp_table(5)


def stupid_addition(a, b):
    return None if type(a) != type(b) else str(a) + str(b) if type(a) == int else int(a) + int(b)


stupid_addition(1, 2)  # "12"

stupid_addition("1", "2")  # 3

stupid_addition("1", 2)  # None


def find_vertex(a, b, c):
    return [-b/2/a, c - b**2/4/a]


find_vertex(1, 0, 25)  # [0, 25]
# The vertex of y=x²+25 is at (0, 25).

find_vertex(-1, 0, 25)  # [0, 25]
# The vertex of y=-x²+25 is at (0, 25).

find_vertex(1, 10, 4)  # [-5, -21]
# The vertex of y=x²+10x+4 is at (-5, -21).


def find_vertex1(a, b, c):
    return [round((-1*b)/(2*a), 2), round((4*a*c - b*b)/(4*a), 2)]
