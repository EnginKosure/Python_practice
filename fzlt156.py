text = "http://www.imdb.com/title/tt0012349/"
sections = text.split('/')
print(sections[-2][2:])  # -1
# with regex
# 'http:\/\/www.imdb.com\/title\/(tt.*?)\/'


# Write a function that reverses the bits in an integer.

# For example, the number 417 is 110100001 in binary.
# Reversing the binary is 100001011 which is 267.


def to_binary(n):
    return int(format(n, '032b')[::-1], 2)


def reverse_bits(n):
    return int(("{0:b}".format(n))[::-1], 2)


def reverse_bits2(n):
    return int(bin(n)[2:][::-1], base=2)


print(reverse_bits(417))  # 267
