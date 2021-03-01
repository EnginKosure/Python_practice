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


def takeSecond(elem):
        return elem[1]
    P = sorted(D, key=takeSecond)
    K = sorted(list(set([i[1] for i in P])))
    M = sorted([i[0] for i in P if i[1] == K[1]])
    for j in M:
        print(j)


if __name__ == '__main__':
    students =[]
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = [i[1] for i in students]
    scores = list(sorted(set(scores)))
    res=sorted([i[0] for i in students if i[1]==scores[1]])
    print(*res,sep="\n")
