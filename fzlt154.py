def is_merge(s, part1, part2):
    return (s[0] == part1[0] and is_merge(s[1:], part1[1:], part2) or s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]) if (s and part1 and part2) else s == part1 + part2)


def is_merge2(ss, p1, p2):
    print(sorted(list(ss)))
    print(sorted(list(p1)+list(p2)))
    return sorted(list(ss)) == sorted(list(p1)+list(p2))


is_merge3 = m = lambda s, x, y: not(s+x+y) or f(s, x, y) or f(s, y, x)
def f(s, x, y): return s and x and s[0] == x[0] and m(s[1:], x[1:], y)


print(is_merge2('codewars', 'code', 'wars'))
