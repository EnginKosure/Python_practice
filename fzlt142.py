def farey(n):
    def obeb(i, j):
        obeb = 1
        for n in range(2, min(i, j)+1):
            obeb = max(obeb, (i % n == 0 and j % n == 0)*n)
        return obeb
    return ['0/1']+sorted(set([f"{int(i/obeb(i,j))}/{int(j/obeb(i,j))}" for i in range(n, 0, -1) for j in range(i, n+1)]), key=lambda x: eval(x))


print(farey(13))
