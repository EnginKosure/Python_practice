def pair_13(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 13 and nums[i+1] == 13:
            return True

    return False


print(pair_13([26, 13, 13]))


def count_hi(p):
    # print(p.split('hi'))
    return len(p.split('hi'))-1


print(count_hi('abc hi ho'))  # 1
print(count_hi('ABChi hi'))  # 2
print(count_hi('hihi'))  # 2
