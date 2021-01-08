input = 'abrkaabcdefghijjxxx'
y = {}
for _ in input:
    counter = 0
    a = ""
    for i in range(len(input)):
        if input[counter] not in a:
            a = a + input[counter]
            counter += 1
    y[a] = len(a)
    input = input[len(a):]
b = max(y.keys(), key=lambda k: y[k])
print(b, len(b))
