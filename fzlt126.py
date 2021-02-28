def lcm_of_list(nums):
    b = max(nums)
    while True:
        if all([b % i == 0 for i in nums]):
            break
        else:
            b += max(nums)
    return b


print(lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


def find_lcm():
    m = 1
    k = max(A)
    for carp in range(2, k+1):
        for index1 in range(len(A)):
            if A[index1] == 1:
                continue
            while A[index1] % carp == 0:
                n = A[index1]
                A = list(map(lambda x: x//carp if x % carp == 0 else x, A))
                n = n//carp
                m = m*carp
    return m
