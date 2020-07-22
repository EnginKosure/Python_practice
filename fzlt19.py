
def shift_letters(s, n):
    new_s = ''
    bsl = 0
    for i in s:
        if i == ' ':
            new_s += " "+i
            bsl += 1
        else:
            new_s = s[-n:]+s[:-n]
    print(new_s)
    return s


shift_letters("Boom", 2)  # "omBo"

shift_letters("This is a test",  4)  # "test Th i sisa"

shift_letters("A B C D E F G H", 5)  # "D E F G H A B C"
