def farey(n):
    def obeb(i, j):
        obeb = 1
        for n in range(2, min(i, j)+1):
            obeb = max(obeb, (i % n == 0 and j % n == 0)*n)
        return obeb
    return ['0/1']+sorted(set([f"{int(i/obeb(i,j))}/{int(j/obeb(i,j))}" for i in range(n, 0, -1) for j in range(i, n+1)]), key=lambda x: eval(x))


print(farey(13))


def farey1(n):
    lst1 = ["0/1"]
    lst2 = [0]
    for i in range(1, n + 1):
        for j in range(1, i):
            if round(j / i, 10) in lst2:
                continue
            else:
                lst1.append(str(j) + "/" + str(i))
                lst2.append(round(j / i, 10))
    answer = [x for _, x in sorted(zip(lst2, lst1))]
    answer.append("1/1")
    return answer
