# You will be given a string with sets of characters, (i.e. words),
# seperated by between one and three spaces (inclusive).

# Looking at the first letter of each word (case insensitive-"A" and
# "a" should be treated the same), you need to determine whether it falls into
# the positive/first half of the alphabet ("a"-"m") or the negative/second half ("n"-"z").

# Return True if there are more (or equal) positive words than negative words, False otherwise.

# "A big brown fox caught a bad rabbit" => True
# "Xylophones can obtain Xenon." => False

def connotation(s):
    l = s.lower()
    arr = l.split()
    return True if sum(1 if ord(i[0]) < 110 else -1 for i in arr) >= 0 else False


print(connotation("A big brown fox caught a bad rabbit"))
print(connotation("Xylophones can obtain Xenon."))


def connotation1(s):
    lst = s.upper().split()
    return sum('A' <= w[0] <= 'M' for w in lst) >= len(lst)/2


print(sum([True, True, False, True, 1]))  # 4
