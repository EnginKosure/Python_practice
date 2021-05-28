# Write function RemoveExclamationMarks which removes
# all exclamation marks from a given string.
def remove_exclamation_marks(s):
    new_s = ''
    for i in s:
        if i == "!":
            continue
        new_s += i
    return new_s


def remove_exclamation_marks1(s):
    return s.replace('!', '')


print(remove_exclamation_marks("Hello World!!!"))
