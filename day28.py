# control_string = 'aeiou'


# def find_vocals(s):

#     result = ''

#     for character in s:
#         if character in control_string:
#             result += character
#     # to avoid the repeatings
#     return ''.join(set(result))


# print(find_vocals('Clarusway'))  # au

def vowels(s):
    vowel = 'aeiou'
    finded = ''
    for i in s:
        if i in vowel:
            if not i in finded:
                finded += i
            # else:
            #     continue
        # else:
        #     continue
    return finded


print(vowels('Merhaba arkadaslarim'))
