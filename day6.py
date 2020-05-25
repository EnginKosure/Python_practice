# Fast Exponentiation -
# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.


def exponent(a, b):
    print(a ** b)


if __name__ == '__main__':
    input1 = int(input('enter base: '))
    input2 = int(input('enter exponent: '))
    exponent(input1, input2)
