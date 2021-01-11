def long_palin(txt):
    a = []
    for i in range(len(txt)):
        for j in range(len(txt)-i):
            t = txt[i:(len(txt)-j)]
            if t == t[::-1]:
                if not t in a:
                    a.append(t)
    return(sorted(a, key=len, reverse=True)[0])


print(long_palin("million"))
