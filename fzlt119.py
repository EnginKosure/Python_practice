def pluralize(lst):
    return set(i + 's'*(lst.count(i) > 1) for i in lst)


pluralize(["cow", "pig", "cow", "cow"])  # { "cows", "pig" }

pluralize(["table", "table", "table"])  # { "tables" }

pluralize(["chair", "pencil", "arm"])  # { "chair", "pencil", "arm" }
