# Given a positive integer, return its corresponding column title
# as appear in an Excel sheet.
# For example:
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


def convertToTitle(n):
    result = ""
    while n > 26:
        result = chr(65+(n-1) % 26) + result
        n = (n-1) // 26
    return chr(64+n) + result
