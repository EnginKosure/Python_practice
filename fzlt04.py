def can_see_stage(seats):
    count = 0
    for j in range(len(seats[0])):
        A = []
        for i in range(len(seats)):
            A.append(seats[i][j])
        print(A)
        if A == sorted(A) and len(A) == len(set(A)):
            count += 1
    return count == len(seats[0])


a = [[1, 2, 3, 2, 1, 1],
     [2, 4, 4, 3, 2, 2],
     [5, 5, 5, 5, 4, 4],
     [6, 6, 7, 6, 5, 5]]

can_see_stage(a)
print(can_see_stage(a))


def can_see_stage(s):
    for i in range(len(s[0])):
        for j in range(1, len(s)):
            if s[j][i] <= s[j-1][i]:
                return(False)
    return(True)
