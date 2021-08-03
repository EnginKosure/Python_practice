def test_distinct(data):
    return True if len(data) == len(set(data)) else False


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))
