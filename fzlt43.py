# daily-python-challenge
# This is an interview question asked by Facebook.
# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.

import math


def find_biggest(lst):
    x = sorted(list(map(abs, lst)), reverse=1)
    total = 1
    print(x)
    for i in range(3):
        total *= x[i]
    print(total)
    return total


find_biggest([-10, -10, 5, 2])


# def multiplying(given_list):
#     temp_1 = -(math.inf)
#     for i in range(len(given_list)):
#         for j in range(len(given_list)):
#             for k in range(len(given_list)):
#                 if i != j and i != k and j != k:
#                     temp = given_list[i]*given_list[j]*given_list[k]
#                     if temp > temp_1:
#                         temp_1 = temp
#                     else:
#                         continue
#     return temp_1
