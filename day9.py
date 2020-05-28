from random import randint


# Center a string in terminal


def center(st, w=60):
    if len(st) >= w:
        return st

    spaces = (w - len(st)) // 2
    result = " " * spaces + st

    return result


print(center('center this regards to a given total length, for here, 80', 80))
print(center('|', 80))

print(center('center according to default width 60'))
print(center('|'))

# Random password

shortest = 7
longest = 15
min_ascii = 33  # !
max_ascii = 126  # ~


def random_password():
    random_length = randint(shortest, longest)  #
    print('password length', random_length)
    result = ''
    for i in range(random_length):
        random_char = chr(randint(min_ascii, max_ascii))
        result += random_char
    return result


def some_wrapper_function():
    print('Random password is:', random_password())


if __name__ == '__main__':
    some_wrapper_function()
