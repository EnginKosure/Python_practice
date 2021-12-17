import re


def find_double_letters(s):
    newStr = ''
    string = list(s)
    for i in range(len(string)):
        if string[i] == string[i-1]:
            newStr += string[i]
    return newStr


print(find_double_letters('hello'))
