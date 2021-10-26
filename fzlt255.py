def invert(d):
    return dict([(k, v) for (v, k) in d.items()])


def invert1(d):
    return {v: k for k, v in d.items()}


def invert2(dct):
    return {dct[i]: i for i in dct}


def invert3(dct):
    return dict(zip(dct.values(), dct.keys()))


def invert4(dct):
    return dict(map(reversed, dct.items()))


print(invert({"z": "q", "w": "f"}))  # { "q": "z", "f": "w" }

print(invert({"a": 1, "b": 2, "c": 3}))  # { 1: "a", 2: "b", 3: "c" }

# { "koala": "zebra", "camel": "horse" }
print(invert({"zebra": "koala", "horse": "camel"}))
