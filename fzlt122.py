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
