# # "Fortune favours the bold." ➞ True
# "You can lead a horse to water, but you can't make him drink." ➞ True
# "Look before you leap." ➞ False
# # Duplicate letters in "Look" and "before".
# "An apple a day keeps the doctor away." ➞ False
# # Duplicate letters in "apple", "keeps", "doctor", and "away".
# print(duplicate_checker("Fortune favours the bold."))
# print(duplicate_checker("ou can lead a horse to water, but you can't make him drink."))
# print(duplicate_checker("Look before you leap."))
from time import time
s_t = time()


def duplicate_checker(s):
    s_arr = s.split()
    for i in s_arr:
        if len(set(i)) != len(i):
            return False
    return True


print(duplicate_checker("An apple a day keeps the doctor away."))
print(f'---AAA {time()-s_t}  seconds')
s_t = time()


def no_duplicate_letters(phrase):
    return not [1 for i in phrase.split() for x in i if i.count(x) > 1]


print(no_duplicate_letters("An apple a day keeps the doctor away."))
print(f'---BBB {time()-s_t}  seconds')
s_t = time()


def no_duplicate_letters2(phrase):
    return not any([len(set(i)) != len(i) for i in phrase.split()])


print(no_duplicate_letters2("An apple a day keeps the doctor away."))
print(f'---CCC {time()-s_t}  seconds')
