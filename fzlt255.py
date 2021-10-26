def invert(d):
    return dict([(k, v) for (v, k) in d.items()])


print(invert({"z": "q", "w": "f"}))  # { "q": "z", "f": "w" }

print(invert({"a": 1, "b": 2, "c": 3}))  # { 1: "a", 2: "b", 3: "c" }

# { "koala": "zebra", "camel": "horse" }
print(invert({"zebra": "koala", "horse": "camel"}))
