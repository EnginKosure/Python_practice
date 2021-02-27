def lcm_of_list(nums):
    b = max(nums)
    while True:
        if all([b % i == 0 for i in nums]):
            break
        else:
            b += max(nums)
    return b
# print(lcm_of_list([1, 2, 3,4,5,6,7,8,9,10]))
