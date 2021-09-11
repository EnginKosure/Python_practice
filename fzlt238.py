# Implement a function which convert the given boolean value
# into its string representation.
def boolean_to_string(b):
    return str(b)


print(boolean_to_string(True))


def high_and_low(s):
    # print(sorted(s.split(' ')))
    # print(sorted(int(i) for i in s.split(' ')))
    return f"{sorted(int(i) for i in s.split(' '))[-1]} {sorted(int(i) for i in s.split(' '))[0]}"


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))  # return "5 1"
# high_and_low("1 2 -3 4 5")  # return "5 -3"
# high_and_low("1 9 3 4 -5")  # return "9 -5"


def high_and_low1(numbers):  # z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))
