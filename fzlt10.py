# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]


def two_sum(nums, target):
    d = {}
    for k, v in enumerate(nums):
        # 0, 2
        # 1,7
        # 2,11
        # 3,15
        r = target-v
        # 7=18-11
        if r in d:
            print([d[r], k])
            return [d[r], k]
        print(k)
        # print(d[v])
        d[v] = k
        # d[2]=0
        # d[7]=1
        print(d)
    return []


two_sum([2, 7, 11, 15], 18)
