from textwrap import wrap


def encode(string):
    return ''.join(''.join(bit * 3 for bit in f'{ord(letter):08b}') for letter in string)


def decode(bits):
    triples = wrap(bits, 3)
    corrected_bits = ''.join('1' if triple.count(
        '1') > triple.count('0') else '0' for triple in triples)
    return ''.join(chr(x) for x in [int(x, 2) for x in wrap(corrected_bits, 8)])
