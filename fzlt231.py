

x = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"


def stat(x):
    for t in range(3):
        r = sorted([int(k) for k in (j[t]
                                     for j in (i.split('|') for i in x.split(',')))])
        rng = max(r)-min(r)
        avg = sum(r)/len(r)
        med = r[len(r)//2] if len(r) % 2 else (r[len(r)//2]+r[len(r)//2+1])/2
        print(rng, avg, med)


stat(x)
