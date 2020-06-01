# tokenizing
def token_list(s):
    # remove all of the spaces
    s = s.replace(" ", "")
    # loop through all of the characters in the string
    # identify the tokens and add to list
    tokens = []
    i = 0
    while i < len(s):
        # These characters below must always be handled as a single character
        if s[i] in ["*", "/", "^", "\\", "(", ")"]:
            tokens.append(s[i])
            i += 1

        # Handle + and -
        elif s[i] in ["+", "-"]:
            # if there is a previous character and it is a number or close bracket
            # then the + or - is a token on its own
            if i > 0 and ('0' <= s[i - 1] <= '9' or s[i - 1] == ')'):
                tokens.append(s[i])
                i += 1
            else:
                # The + or - is part of a number
                num = s[i]
                i += 1

                # Keep on adding chars to the token as long as they are digits
                while i < len(s) and '0' <= s[i] <= '9':
                    num += s[i]
                    i += 1
                tokens.append(num)

        # Handle a number without a leading + or -
        elif '0' <= s[i] <= '9':
            num = ''

            # Keep on adding chars to the token as long as they are digits
            while i < len(s) and '0' <= s[i] <= '9':
                num += s[i]
                i += 1
            tokens.append(num)

        # Any other chars means the exp. is invalid.
        # Return an empty list to indicate that an error occurred.
        else:
            return []
    return tokens


def main():
    exp = input('Enter a math expression: ')
    tokens = token_list(exp)
    print('The tokens are: ', tokens)


if __name__ == "__main__":
    main()
