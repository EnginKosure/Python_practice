N = int(input("N: "))

x = 1
# negative step makes reverse order
for i in range(N, 0, -1):  # starting number, ending number, step
    numberOfSpaces = i - 1
    numberOfStars = N - i + x
    print(" " * numberOfSpaces + "*" * numberOfStars)
    x = x + 1


print(list(range(5, 1, -1)))  # [5, 4, 3, 2]
