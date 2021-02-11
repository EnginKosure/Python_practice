def pluralize(lst):
    return set(i + 's'*(lst.count(i) > 1) for i in lst)


pluralize(["cow", "pig", "cow", "cow"])  # { "cows", "pig" }

pluralize(["table", "table", "table"])  # { "tables" }

pluralize(["chair", "pencil", "arm"])  # { "chair", "pencil", "arm" }


OP = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__,
      '//': lambda a, b: a//b if b else -1}


def arithmetic_operation(n):
    a, o, b = n.split()
    return OP[o](int(a), int(b))


arithmetic_operation("12 + 12")  # 24 // 12 + 12 = 24

arithmetic_operation("12 - 12")  # 24 // 12 - 12 = 0

arithmetic_operation("12 * 12")  # 144 // 12 * 12 = 144

arithmetic_operation("12 // 0")  # -1 // 12 / 0 = -1
