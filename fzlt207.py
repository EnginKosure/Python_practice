# add_one=lambda x:x+1
def add_one(x): return x+1


added = add_one(3)
print(added)  # 4

numbers = [1, 2, 3, 4]
times_two = map(lambda x: x * 2, numbers)
lst = list(times_two)
print(lst)  # [2, 4, 6, 8]


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


dispatch_dict('add', 2, 8)
# 10
dispatch_dict('mul', 2, 8)
print(dispatch_dict('mul', 2, 8))  # 16
dispatch_dict('unknown', 2, 8)
print(dispatch_dict('unknown', 2, 8))  # None
