control_string = 'aeiou'


def find_vocals(s):

    result = ''

    for character in s:
        if character in control_string:
            result += character
    # to avoid the repeatings
    return ''.join(set(result))


print(find_vocals('Clarusway'))  # au
