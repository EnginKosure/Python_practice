def execute(s):
    d = {}
    for i in s:
        d[i[0]] = i[1]
    v = d.values()
    second = sorted(list(set(v)))[1]

    lowest2 = [key for key, value in d.items() if value == second]
    lowest2.sort()

    return [print(n) for n in lowest2]


students = [['Betty', 34], ['Berry', 45.5], [
    'Tina', 33], ['Akriti', 56], ['Harsh', 45.5], ['Fazi', 34]]

execute(students)  # Betty Fazi
