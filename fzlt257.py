if __name__ == '__main__':
    print("Welcome to hangman!!")
    word = "EVAPORATE"
    guessed = "_" * len(word)
    word = list(word)
    guessed = list(guessed)
    lstGuessed = []
    letter = input("guess letter: ")
    while True:
        if letter.upper() in lstGuessed:
            letter = ''
            print("Already guessed!!")
        elif letter.upper() in word:
            index = word.index(letter.upper())
            print("index", index)
            guessed[index] = letter.upper()
            print("guessed index", guessed[index])
            print("before", word[index])
            # To enable catching of next index, in case multiple appearance
            word[index] = '_'
            print("after", word[index])
        else:
            print(''.join(guessed))
            if letter is not '':
                lstGuessed.append(letter.upper())
            letter = input("guess letter: ")

        if '_' not in guessed:
            print("You won!!")
            break
