# unique chars
# anagram check


def char_counts(s):
    chars = {}
    for i in s:
        # keys = chars.keys()
        # if i in keys:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    print('this string contains', len(chars), 'unique chars.')
    print(s)
    print(''.join(chars.keys()))
    return chars


def main():
    s1 = input('Enter chars: ')
    s2 = input('Enter chars: ')

    seq1 = char_counts(s1)
    seq2 = char_counts(s2)

    if seq1 == seq2:
        print('Those strings are anagrams')
    else:
        print('Not anagram')


if __name__ == '__main__':
    main()
print(len(['', '']))
