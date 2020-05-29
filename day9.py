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


def password_control(p):
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    for ch in p:
        if 'a' <= ch <= 'z':
            has_lower = True
        elif 'A' <= ch <= 'Z':
            has_upper = True
        elif '0' <= ch <= '9':
            has_number = True
        elif ord(ch) in [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 58, 59, 60, 61, 62, 63, 64, 91, 92,
                         93, 94, 95, 96, 123, 124, 125, 126]:
            has_special = True
    if len(p) >= 8 and has_special and has_upper and has_number and has_lower:
        return True
    return False


if __name__ == '__main__':
    some_wrapper_function()
    p = input('Enter a password to check if valid: ')
    if password_control(p):
        print('Valid password')
    else:
        print('Invalid password')
