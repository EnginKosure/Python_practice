N = int(input("N: "))

x = 1
for i in range(N, 0, -1):  # starting number, ending number, step
    numberOfSpaces = i - 1
    numberOfStars = N - i + x
    print(" " * numberOfSpaces + "*" * numberOfStars)
    x = x + 1
