def all_equal(l):
    return len(list(set(l))) <= 1


def all_equal1(items):
    return all(item1 == item2 for item1 in items for item2 in items)
