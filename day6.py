from math import sqrt


# Fast Exponentiation -
# Ask the user to enter 2 integers a and b and output a^b (i.e. pow(a,b)) in O(lg n) time complexity.


def exponent(a, b):
    print(a ** b)


# Collatz Conjecture -
# Start with a number n > 1. Find the number of steps it takes to reach one using the following process:
# If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def collatz(n):
    i = 0
    while n != 1:
        i += 1
        if n % 2:
            n = n * 3 + 1
        else:
            n /= 2
    print(i)


collatz(48)

# free fall calculation
gravity = 9.8
d = float(input('height in meters: '))
vf = sqrt(2 * gravity * d)
print(f'it will hit the ground with {vf}m/s')

if __name__ == '__main__':
    input1 = int(input('enter base: '))
    input2 = int(input('enter exponent: '))
    exponent(input1, input2)
