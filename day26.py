# Generate passwords by concatenating two words
# Each word must be at least 3 chars long
# Total length must be between 8-10

from random import randrange

word_file = '/Users/enginkosure/Documents/docs/deneme.txt'

words = []
inf = open(word_file, 'r')

for line in inf:
    line = line.rstrip()

    if 3 <= len(line) <= 7:
        words.append(line)
inf.close()

# Randomly select the first word.
first = words[randrange(0, len(words))]
first = first.capitalize()

password = first

while len(password) < 8 or len(password) > 10:
    second = words[randrange(0, len(words))].capitalize()
    password = first+second
print('The random password is', password)
