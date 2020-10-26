# The power set of a set is the set of all its subsets.
# Write a function that, given a set, generates its power set.
# For example, given the set {1, 2, 3}, it should return
# {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.


def f_subsets(s):
    result = []
    for i in s:
        result += [j.union({i}) for j in result]
        result.append({i})
    return [{}] + sorted(result, key=len)


def findPowerSet(S):

        # N stores total number of subsets
    N = int(pow(2, len(S)))
    s = set()

    # generate each subset one by one
    for i in range(N):
        # check every bit of i
        for j in range(len(S)):
            # if j'th bit of i is set, print S[j]
            if i & (1 << j):
                s.add(S[j])

        print(list(s))
        s.clear()


if __name__ == '__main__':

    S = [1, 2, 3]
    findPowerSet(S)
