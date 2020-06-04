# unique chars

s = input('Enter chars: ')

chars = {}
for i in s:
    #keys = chars.keys()
    if i in chars:
        chars[i] += 1
    else:
        chars[i] = 1
print(chars)
print('this string contains', len(chars), 'unique chars.')
print(s)
print(''.join(chars.keys()))
