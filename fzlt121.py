def invert(d):
    return {v: k for k, v in d.items()}


invert({"z": "q", "w": "f"})
# { "q": "z", "f": "w" }

invert({"a": 1, "b": 2, "c": 3})
# { 1: "a", 2: "b", 3: "c" }

invert({"zebra": "koala", "horse": "camel"})
# { "koala": "zebra", "camel": "horse" }


def line_length(a1, a2):
    return ((a1[0]-a2[0])**2+(a1[1]-a2[1])**2)**.5


print(line_length([15, 7], [22, 11]))  # 8.06

print(line_length([0, 0], [0, 0]))  # 0

print(line_length([0, 0], [1, 1]))  # 1.41
