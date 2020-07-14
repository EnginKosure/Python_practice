# Fibonacci Sequence -
# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.


def generate_fibonacci_sq(input):
    seq = []
    x = 1
    y = 1
    for i in range(input):
        seq.append(x)
        # z=x+y
        # x=y
        # y=z
        x, y = y, x + y

    print('nth term', seq)
    return seq


# input = int(input('enter a number till 100'))


def fibonacci_till_input(input):
    seq = [1]
    x = 0
    y = 1

    while x <= input:
        seq.append(y)
        # x, y = y, x + y
        x = y-x
        y = x+y

    print('till input', seq)  # till input [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


# generate_fibonacci_sq(input)
# fibonacci_till_input(input)
fibonacci_till_input(55)

# num = 1
# count = 0
# list_fibonacci = [1]
# i = 0
# while max(list_fibonacci) < 55:
#     count += list_fibonacci[i-1]
#     list_fibonacci.append(count)
#     i += 1

# print(list_fibonacci)


# n = int(input("enter a number to check if it is a prime or not:"))
# count = 0
# for i in range(1, n+1):
#     if not (n % i):
#         count += 1
# if (n == 0) or (n == 1) or (count >= 3):
#     print(n, "is not a prime number.")
# else:
#     print(n, "is a prime number")
