# Create a function that takes the side n of the game screen and returns the number of times the snake can eat
# before it runs out of space in the game screen.
import wikipedia
import pywhatkit as kit
from math import floor, log2


def snakefill(n):
    return len(bin(n**2))-3


snakefill(3)  # 3

snakefill(6)  # 5

snakefill(24)  # 9


def snakefill2(n):
    return floor(log2(n*n))


# kit.sendwhatmsg('+3**********', 'test with python', 22, 48)

wiki_val1 = wikipedia.search("Barack Obama")
print(wiki_val1)
wiki_val2 = wikipedia.search("Ford", results=3)
print(wiki_val2)

wiki_val3 = wikipedia.languages()

print(wiki_val3['tr'])
