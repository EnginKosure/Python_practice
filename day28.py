control_string = 'aeiou'


def find_vocals(s):

    result = ''

    for character in s:
        if character in control_string:
            result += character
    return result


print(find_vocals('Clarusway'))  # aua
