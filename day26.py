# Generate passwords by concatenating two words
# Each word must be at least 3 chars long
# Total length must be between 8-10

from random import randrange

word_file = 'day13-copy.py'

words = []
inf = open(word_file, 'r')

for line in inf:
    line = line.rstrip()

    if 3 <= line <= 7:
        words.append(line)
inf.close()

# Randomly select the first word.
