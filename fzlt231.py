

x = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"


def stat(x):
    for t in range(3):
        print([int(k) for k in (j[t]
                                for j in (i.split('|') for i in x.split(',')))])


stat(x)
