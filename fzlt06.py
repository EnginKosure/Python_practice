def triangle(perimeter, area):
    new_list = []
    nums = list(range(1, perimeter//2))
    s = perimeter/2
    for a in nums:
        for b in nums:
            for c in nums:
                if area == round((s * (s - a) * (s - b) * (s - c))**0.5, 6) and a <= b <= c and a+b+c == s*2:
                    new_list.append([a, b, c])
    return new_list


print(triangle(3, 0.43))


def triangle1(p, a):
    r = []
    s = p/2
    for x in range(1, p//2+1):
        for y in range(int(s-x+1), p//2+1):
            z = p-x-y
            if round((s*(s-x)*(s-y)*(s-z))**.5, 5) == a:
                new = sorted((x, y, z))
                if new not in r:
                    r.append(new)
    return sorted(r)


print(triangle1(3,  0.43301))


def triangle2(p, area):
    def f(a, b, c): return (p*(p-2*a)*(p-2*b)*(p-2*c))**0.5/4
    result = []
    for a in range(p//3, p):
        for c in range(p//3, 0, -1):
            b = p-a-c
            if abs(f(a, b, c)-area) < 0.5 and sorted([a, b, c]) not in result:
                result.append(sorted([a, b, c]))
    return sorted(result)
