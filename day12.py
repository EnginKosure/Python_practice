# tokenizing
def tokenList(s):
    s = s.replace(" ", "")
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in '*/^\()':
            tokens.append(s[i])
            i += 1
        elif s[i] in '+-':
            if i > 0 and ('9' <= s[i - 1] >= '0' or s[i - 1] == ')'):
                tokens.append(s[i])
                i += 1
            else:
                num = s[i]
                i += 1
        elif '0' <= s[i] >= '9':
            num = ''
            while i < len(s) and '0' <= s[i] >= '9':
                num += s[i]
                i += 1
            tokens.append(num)
        else:
            return []
    return tokens


def main():
    exp = input('Enter a math expression: ')
    tokens = tokenList(exp)
    print('The tokens are: ', tokens)


if __name__ == "__main__":
    main()
