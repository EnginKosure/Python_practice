x = ["a", "b", "c"]
y = ["b", "c", "d", "a", "a"]

result = dict()

for i in x:  # O(N)
    if i in result:  # O(1)
        result[i] += 1
    else:
        result[i] = 1

for i in y:  # O(N)
    if i in result:  # O(1)
        result[i] += 1

print(result)
