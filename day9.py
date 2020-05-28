# Center a string in terminal
WIDTH = 80


def center(st, w):
    if len(st) >= w:
        return st

    spaces = (w - len(st)) // 2
    result = " " * spaces + st

    return result


print(center('center this', WIDTH))
