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
