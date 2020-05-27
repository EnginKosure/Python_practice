# Caesar cipher

message = input('enter the message: ')
shift = int(input('enter the key'))

new_message = ''

for ch in message:
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        pos = (pos + shift) % 26
        new_char = chr(pos + ord('a'))
        new_message += new_char
    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        pos = (pos + shift) % 26
        new_char = chr(pos + ord('A'))
        new_message += new_char
    else:
        new_message += ch
print('The shifted message is', new_message)
