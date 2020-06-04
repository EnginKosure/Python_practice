# unique chars

s = input('Enter chars: ')

chars = {}
for i in s:
    chars[i] = True

print('this string contains', len(chars), 'unique chars.')
print(s)
print(chars.keys())
