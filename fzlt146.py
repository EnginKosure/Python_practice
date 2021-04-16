
def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have second hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!


def isPhoneNumber1(text):
    arr_text = text.split('-')
    if len(text) != 12 and len(arr_text) != 3:
        return False  # not phone number-sized
    if len([False for i in arr_text for j in i if not j.isdecimal()]) > 0:
        return False
    # for i in arr_text:
    #     for j in i:
    #         if not j.isdecimal():
    #             return False
    return True  # "text" is a phone number!


print(isPhoneNumber1('415-555-4242'))
print(isPhoneNumber1('Mos-him-mosh'))

print(isPhoneNumber1('416-555-4242'))
a = {
    1: [{'n': 1}, {'n': 2}],
    2: [{'n': 3}, {'n': 4}],
    3: [{'n': 5}],
}
good = [1, 2]
[r['n'] for g in good for r in a[g]]
[1, 2, 3, 4]

print([r['n'] for g in good for r in a[g]])
