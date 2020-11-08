# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

def sum_up(arr,t):
    for i in arr:
        for j in [n for n in arr if n !=i]:
            if i+j==t:
                return sorted([arr.index(i),arr.index(j)])


nums = [2,7,11,15], target = 9

# print