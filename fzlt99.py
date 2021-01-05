def arithmetic_operation(equation):
    '''
    Returns the result of evaluating the string equation
    '''
    from operator import add, sub, floordiv, mul

    OPS = {'+': add, '-': sub, '*': mul, '//': floordiv}
    a, op, b = equation.split()

    try:
        return OPS[op](int(a), int(b))
    except ZeroDivisionError:
        return -1


arithmetic_operation("12 + 12")  # 24 // 12 + 12 = 24

arithmetic_operation("12 - 12")  # 24 // 12 - 12 = 0

arithmetic_operation("12 * 12")  # 144 // 12 * 12 = 144

arithmetic_operation("12 // 0")  # -1 // 12 / 0 = -1

# Second solution
OP = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__,
      '//': lambda a, b: a//b if b else -1}


def arithmetic_operation1(n):
    a, o, b = n.split()
    return OP[o](int(a), int(b))


def arithmetic_operation2(n):
    a, b, c = n.split()
    if b == "//":
        return -1 if c == '0' else int(a)//int(c)
    elif b == "+":
        return int(a) + int(c)
    elif b == "-":
        return int(a) - int(c)
    else:
        return int(a) * int(c)
