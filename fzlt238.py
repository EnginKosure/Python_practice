# Implement a function which convert the given boolean value
# into its string representation.
def boolean_to_string(b):
    return str(b)


print(boolean_to_string(True))


def high_and_low(s):
    # print(f"{sorted(s.split(' '))[-1]} {sorted(s.split(' '))[0]}")
    return f"{sorted(s.split(' '))[-1]} {sorted(s.split(' '))[0]}"


high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5")  # return "5 -3"
# high_and_low("1 9 3 4 -5")  # return "9 -5"
