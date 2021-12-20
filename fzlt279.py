# cumulative sum
x = [3, 10, 4, 12, 55]
cs = [0]*5

for i in range(0, len(x)):
    cs[i] = sum(x[0:(i+1)])

print(cs)


x = [3, 10, 4, 12, 55]
cs = list()

for i in range(0, len(x)):
    cs.append(sum(x[0:(i+1)]))

print(cs)

# how long to 5 5's
x = [5, 3, 2, 5, 5, 1, 2, 5, 3, 5, 1, 5, 1]

count = 0
i = 0

while count < 5:
    if x[i] == 5:
        count += 1
    i += 1

print(i)
