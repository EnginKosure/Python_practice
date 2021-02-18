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
