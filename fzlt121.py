def invert(d):
    return {v: k for k, v in d.items()}


invert({"z": "q", "w": "f"})
# { "q": "z", "f": "w" }

invert({"a": 1, "b": 2, "c": 3})
# { 1: "a", 2: "b", 3: "c" }

invert({"zebra": "koala", "horse": "camel"})
# { "koala": "zebra", "camel": "horse" }
