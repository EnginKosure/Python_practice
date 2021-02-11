def pluralize(lst):
    return set(i + 's'*(lst.count(i) > 1) for i in lst)


pluralize(["cow", "pig", "cow", "cow"])  # { "cows", "pig" }

pluralize(["table", "table", "table"])  # { "tables" }

pluralize(["chair", "pencil", "arm"])  # { "chair", "pencil", "arm" }


def arithmetic_operation(s):


arithmetic_operation("12 + 12")  # 24 // 12 + 12 = 24

arithmetic_operation("12 - 12")  # 24 // 12 - 12 = 0

arithmetic_operation("12 * 12")  # 144 // 12 * 12 = 144

arithmetic_operation("12 // 0")  # -1 // 12 / 0 = -1
