# Given a string s consists of upper/lower-case alphabets and
# empty space characters ' ', return the length of last word
# (last word means the last appearing word if we loop from left to right) in the string.
# If the last word does not exist, return 0.

def last_length(s):
    return len(s.split()[-1])


print(last_length("One two three"))
