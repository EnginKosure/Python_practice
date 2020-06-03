# list comprehension review
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# for i in stuff:
#     print(i)

# y = [print(i) for i in [[w.upper(), w.lower(), len(w)] for w in words]]
# print(y) would return [None, None, None, None, None, None, None, None, None]

x = [i for i in [[w.upper(), w.lower(), len(w)] for w in words]]


print(x)  # print([i for i in x]) would give the same output
# [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3],
# ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]


# Two dice simulation
