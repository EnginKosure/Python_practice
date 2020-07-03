sentence = input('Enter a sentence: ')

spaces = 0
for i in sentence:
    if i == ' ':
        spaces += 1
print('Number of words:', spaces+1)
