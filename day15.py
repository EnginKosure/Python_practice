# list comprehension review
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# for i in stuff:
#     print(i)

[print(i) for i in [[w.upper(), w.lower(), len(w)] for w in words]]

# Two dice simulation
