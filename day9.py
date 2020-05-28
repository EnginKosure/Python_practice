# Center a string in terminal


def center(st, w=60):
    if len(st) >= w:
        return st

    spaces = (w - len(st)) // 2
    result = " " * spaces + st

    return result


print(center('center this', 80))
print(center('center according to default width 60'))
