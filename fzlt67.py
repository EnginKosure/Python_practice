# QUESTION: Level of Interview Question = Medium
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
# like this: (you may want to display this pattern
#             in a fixed font for better legibility)


def convert3(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    table = [""]*numRows
    r, dir = 0, -1
    for i in s:
        if (r == numRows-1) or (r == 0):
            dir *= -1
        table[r] += i
        r += dir
    return "".join(table)
