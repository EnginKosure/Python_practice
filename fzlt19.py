
def shift_letters(txt, n):
    letters = txt.replace(' ', '')
    print('letters', letters)
    n %= len(letters)
    print(n)
    shifted = iter((letters[-n:] + letters[:-n]))
    return ''.join(' ' if i.isspace() else next(shifted) for i in txt)


print(shift_letters("Boom", 2))  # "omBo"

print(shift_letters("This is a test",  4))  # "test Th i sisa"

shift_letters("A B C D E F G H", 5)  # "D E F G H A B C"
'str i n g '.count(' ')
