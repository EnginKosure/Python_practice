# Binary to Decimal and Back Converter -
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.


def convert_decimal_to_binary(num):
    i = 0
    hmi = num
    while hmi / 2 >= 1:
        hmi /= 2
        i += 1

    # print(i)
    binary = [0] * (i + 1)
    while i > 0:
        x = int(num / (2 ** i))
        binary[len(binary) - 1 - i] = x
        num -= x * (2 ** i)
        i -= 1
    binary[-1] = num % 2
    # print(binary)
    y = int(''.join(map(str, binary)))
    print(y)


convert_decimal_to_binary(8)
convert_decimal_to_binary(9)
convert_decimal_to_binary(100)


# convert decimal to binary, method 2
# sum(d * 10**i for i, d in enumerate(list[::-1]))

def decimal_to_binary_2(num):
    bin = []
    while num:
        digit = num % 2
        num = int(num / 2)
        # print(digit)
        bin.append(digit)
    bin.reverse()
    print(bin)
    print(int(''.join(map(str, bin))))


decimal_to_binary_2(100)  # 1100100

# converter: convert binary to decimal
'''
Example -: 1011
1). Take modulo of given binary number with 10. 
    (1011 % 10 = 1)
2). Multiply rem with 2 raised to the power
    it's position from right end. 
    (1 * 2^0)
    Note that we start counting position with 0. 
3). Add result with previously generated result.
    decimal = decimal + (1 * 2^0)
4). Update binary number by dividing it by 10.
    (1011 / 10 = 101)
5). Keep repeating upper steps till binary > 0.

Final Conversion -: (1 * 2^3) + (0 * 2^2) +
                 (1 * 2^1) + (1 * 2^0) = 11
# sum(d * 10**i for i, d in enumerate(list[::-1]))

'''


def binary_to_decimal(num):
    i = 0
    decimal = 0
    while num:
        digit = num % 10
        decimal += digit * 2 ** i
        i += 1
        num = num // 10
        print(decimal)


binary_to_decimal(1001)


# Calculator -
# A simple calculator to do basic operators. Make it a scientific calculator for added complexity.


def calc(a, b, op):
    if op == '+':
        print('result of addition', a + b)
    elif op == '-':
        print('result of subtraction', a - b)
    elif op == '*':
        print('result of multiplication', a * b)
    elif op == '/':
        print('result of division', a / b)
    else:
        print('wrong input')


def x():  # Wrapper function

    a = int(input('Please type the first number: '))
    b = int(input('Please type the second number: '))
    op = input(
        'What kind of operation would you like to do?\
        \nChoose between "+, -, *, /" : ')

    print(calc(a, b, op))


if __name__ == '__main__':
    x()
