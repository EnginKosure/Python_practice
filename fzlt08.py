
s = 'ABCDBCA'

print(s.translate({ord('A'): ord('a'), ord('B'): ord('b'), ord('C'): None}))
print(s.translate({ord('a'): '0', ord('e'): '1',
                   ord('i'): '2', ord('o'): '2', ord('u'): '3'}))


def encrypt(word):
    word_r = word[::-1]
    word_t = word_r.translate({ord('a'): '0', ord('e'): '1',
                               ord('i'): '2', ord('o'): '2', ord('u'): '3'})
    word_t += 'aca'
    print(word_t)
    return word_t


encrypt('apple')
encrypt("banana")  # "0n0n0baca"

encrypt("karaca")  # "0c0r0kaca"

encrypt("burak")  # "k0r3baca"

encrypt("alpaca")  # "0c0pl0aca"


def encrypt1(word):
    return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'


coll = [2, 5, 9, 5, 4, 7, 0, 27, 35, 44, 66]
print([i for i in coll if i % 2])
print([i for i in coll if i % 2 == 0])
print(len([i for i in coll if i % 2]))
print(len([i for i in coll if i % 2 == 0]))
