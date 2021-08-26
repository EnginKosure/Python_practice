# Create a function that takes the number of wins, draws and losses
# and calculates the number of points a football team has obtained so far.

# wins get 3 points
# draws get 1 point
# losses get 0 points
def football_points(x, y, z):
    return x*3+y*2


# test
print(football_points(3, 4, 2))  # ➞ 17

print(football_points(5, 0, 2))  # ➞ 15

print(football_points(0, 0, 1))  # ➞ 0


def make_negative(number):
    return -abs(number)


def make_negative1(number):
    return -number if number > 0 else number


def hex_to_dec(s):
    return int(s, 16)


def count_squares(x):
    return 6 * x**2 + 2


def fun_func(s):
    return s[::-1]


print(fun_func('fast'))


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
