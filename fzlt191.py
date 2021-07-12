# import the random library
import random

# read all the list of words
words = []
with open('sowpods.txt', 'r') as f:
    line = f.readline().strip()
    words.append(line)
    while line:
        line = f.readline().strip()
        words.append(line)

# generate a random number
random_index = random.randint(0, len(words))

# take the word
print("Random word: ", words[random_index])


def fun1(num):
    return num + 25


fun1(5)
# print(num) # NameError: name 'num' is not defined
