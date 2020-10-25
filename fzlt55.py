# Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
# For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
# As another example, given the string "google", you should return "elgoogle".


def f_min_insert(s):
    if s == s[::-1]:
        return s
    if s[0] == s[-1]:
        return s[0] + f_min_insert(s[1:-1]) + s[-1]
    else:
        sl = s[0] + f_min_insert(s[1:]) + s[0]
        sr = s[-1] + f_min_insert(s[:-1]) + s[-1]
        if len(sl) > len(sr):
            return sr
        elif len(sl) < len(sr):
            return sl
        return sl if sl < sr else sr
