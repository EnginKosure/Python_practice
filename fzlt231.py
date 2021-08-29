

x = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"


def stat(x):
    av = []
    ra = []
    me = []
    for t in range(3):
        r = sorted([int(k) for k in (j[t]
                                     for j in (i.split('|') for i in x.split(',')))])
        rng = max(r)-min(r)
        avg = round(sum(r)/len(r))
        med = r[len(r)//2] if len(r) % 2 else round((r[len(r)//2]+r[len(r)//2+1])/2)
        av.append(avg)
        ra.append(rng)
        me.append(med)
    print(ra, av, me)
    for i in range(3):
        print(av[i], ra[i], me[i])


stat(x)
