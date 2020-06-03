from random import randint
# list comprehension review
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]
# It can be done also using mapping with lambda
#stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)

# for i in stuff:
#     print(i)

# y = [print(i) for i in [[w.upper(), w.lower(), len(w)] for w in words]]
# print(y) would return [None, None, None, None, None, None, None, None, None]

x = [i for i in [[w.upper(), w.lower(), len(w)] for w in words]]


print(x)  # print([i for i in x]) would give the same output
# [['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3],
# ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]


# Two dice simulation

dice_probabilities = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5 /
                      36, 7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}

counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}


def two_dice():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    return d1+d2


for i in range(1000):
    t = two_dice()
    counts[t] += 1
print(counts)

for i in sorted(counts.keys()):
    print(i, counts[i]/10, round(dice_probabilities[i]*100, 1))
