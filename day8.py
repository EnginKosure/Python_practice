# Caesar cipher

message = input('enter the message: ')
shift = int(input('enter the key: '))

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

# print(ord('a'), ord('z'), ord('A'), ord('Z'))  # 97 122 65 90

decrypted = ''
for i in new_message:
    if 'a' <= i <= 'z':
        pos = ord(i) - ord('a')
        pos = (pos - shift) % 26
        new_i = chr(pos + ord('a'))
        decrypted += new_i
    elif 'A' <= i <= 'Z':
        pos = ord(i) - ord('A')
        pos = (pos - shift) % 26
        new_i = chr(pos + ord('A'))
        decrypted += new_i
    else:
        decrypted += i
print('Decrypted version is:', decrypted)
