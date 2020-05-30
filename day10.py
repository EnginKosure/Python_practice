# Display the entered user data in ascending order
data = []

num = int(input('Enter an integer (0 to quit): '))

while num != 0:
    data.append(num)
    num = int(input('Enter an integer (0 to quit): '))

data.sort()

# display values in ascending order
print('The values in ascending order are: ')
for num in data:
    print(num)

print('The values in descending order are: ')

for num in data[::-1]:
    print(num)


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# hashMap usage

def two_sum(l, target):
    d = {}
    # print(list(enumerate(l)))
    for k, v in enumerate(l):
        # print(k, v)
        d[v] = k
    # print(d)

    c = []

    for i in l:
        if target - i in d.keys() and target - i != i:
            c.append(d[i])
    print(c)


a = [2, 7, 11, 15]
two_sum(a, 18)
arr = [3, 2, 1, 1]
two_sum(arr, 6)
