def convert_string(s):
    new_string = ''
    for i in s:
        if i.lower() != i:
            i = i.lower()
            new_string += ' ' + i
        else:
            new_string += i
    print(new_string)
    return new_string


convert_string('helloWorld')  # hello world
convert_string('iLoveMyTeapot')  # i love my teapot
convert_string('stayInStaySafe')  # stay in stay safe
convert_string('iLoveClarusway')  # i love clarusway
