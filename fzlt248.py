# Define a function named convert that takes a list of numbers as its only parameter and
# returns a list of each number converted to a string.

# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

def convert(a):
    return [str(i) for i in a]


print(convert([1, 2, 3]))
