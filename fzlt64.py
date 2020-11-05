import wikipedia
result = wikipedia.page('nikola tesla')
print(result.summary)


# Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
# For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137,
# since we would take elements 42, 14, -5, and 86.
# Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
def f_maxsub(nums):
    result = float("-inf")
    if len(nums) < 2:
        try:
            result = max(0, nums[0])
        except:
            result = 0
        else:
            return result
    for i in range(len(nums)):
        for j in range(i+1, len(nums)+1):
            result = max(result, sum(nums[i:j]))
    return max(0, result)
