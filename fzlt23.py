def missing_char(word, n):
    new_word = ''
    for i in range(len(word)):
        if i != n:
            new_word += word[i]
    print(new_word)
    return new_word


missing_char('fazilet', 1)
missing_char('serra', 2)
