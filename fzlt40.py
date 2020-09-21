# This is an interview question asked by Palantir.
# Write an algorithm to justify text. Given a sequence of words and an integer line length k,
# return a list of strings which represents each line, fully justified.
# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word.
# Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
# If you can only fit one word on a line, then you should pad the right-hand side with spaces.
# Each word is guaranteed not to be longer than k.
# For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over",  # 2 extra spaces distributed evenly
# "the   lazy   dog"]  # 4 extra spaces distributed evenly
#  k = 8, you should return the following:
# ['the     ',
# 'quick   ',
# 'brown   ',
# 'fox     ',
# 'jumps   ',
# 'over the',
# 'lazy dog']


def justify(list_of_words, k):
    list_of_words_1 = []
    counter = 0
    content = 0
    for i in list_of_words:
        content += len(i)
        if k >= (content+counter):
            list_of_words_1.append(" "+i)
            counter += 1
        else:
            list_of_words_1.append("0")
            content = 0
            counter = 0
            list_of_words.insert(0, i)
    divided_list = ''.join(list_of_words_1)
    divided_list = [line.split('-') for line in divided_list.split('0')]
    divided_list = [i[0].lstrip() for i in divided_list]
    print(divided_list)


justify(["the", "quick", "brown", "fox", "jumps",
         "over", "the", "lazy", "dog"], 16)
