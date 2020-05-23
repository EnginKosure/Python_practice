# Binary to Decimal and Back Converter -
# Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.


def convert_decimal_to_binary(num):
    i = 0
    hmi = num
    while hmi / 2 >= 1:
        hmi /= 2
        i += 1

    # print(i)
    binary = [0] * (i+1)
    while i > 0:
        x = int(num / (2 ** i))
        binary[len(binary)-1 - i] = x
        num -= x * (2 ** i)
        i -= 1
    binary[-1] = num % 2
    # print(binary)
    y = int(''.join(map(str, binary)))
    print(y)


convert_decimal_to_binary(8)
convert_decimal_to_binary(9)
convert_decimal_to_binary(100)

