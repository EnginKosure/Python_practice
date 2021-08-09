import re


def test_distinct(data):
    return True if len(data) == len(set(data)) else False


print(test_distinct([1, 5, 7, 9]))
print(test_distinct([2, 4, 5, 5, 7, 9]))


def to_camel_case(text):
    words = re.split(r"[-_]", text)
    return "".join([words[0]] + [word.title() for word in words[1:]]) if words else ""
