# Morse code
MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-'}

# Function to encrypt the string
# according to the morse code chart


def encrypt(message):
    # 'cipher' ->'stores the morse translated form of the english string'
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the correspponding morse code
            # along with a space to separate morse codes for different characters
            cipher += MORSE_CODE[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher

# Function to decrypt the string from morse to english


def decrypt(message):
    # extra space added at the end to access the last morse code
    # 'message' -> 'stores the string to be encoded or decoded'
    message += ' '
    # 'decipher' -> 'stores the english translated form of the morse string'
    decipher = ''
    # 'citext' -> 'stores morse code of a single character'
    citext = ''
    for morse_letter in message:
        # checks for space
        if (morse_letter != ' '):
            # counter to keep track of space
            # 'i' -> 'keeps count of the spaces between morse characters'
            i = 0

            # storing morse code of a single character
            citext += morse_letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:
                 # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values (reverse of encryption)
                # Special attention here!
                decipher += list(MORSE_CODE.keys()
                                 )[list(MORSE_CODE.values()).index(citext)]
                # empty the variable for the next loop
                citext = ''

    return decipher

# Hard-coded driver function to run the program


def main():
    message = "Make it happen"
    res = encrypt(message.upper())
    print(res)

    message = "-- .- -.- .  .. -  .... .- .--. .--. . -. "
    message1 = '... --- -- .  - . -..- - '
    n_message = 'SOME TEXT'
    result = decrypt(message)
    result1 = decrypt(message1)
    enc = encrypt(n_message)
    print(result)
    print(enc)
    print(result1)  # SOME TEXT


# Executes the main function
if __name__ == '__main__':
    main()

x = ['a', 'b', 'c']
print(x.index('a'))  # 0
print(x[0])  # a
print(x[x.index('a')])  # a

# Adding sth to test a git feature
