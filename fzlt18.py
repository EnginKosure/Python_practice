# Count the number of each letter in a sentence.
# The department you work for undertook a project construction that makes word / text analysis.
# You are asked to calculate the number of letters or any chars in the sentences entered under this project.
# Write a Python program that;
# takes a sentence from the user,
# counts the number of each letter of the sentence,
# collects the letters/chars as a key and the counted numbers as a value in a dictionary.
s = input('Enter a sentence: ')


def char_counter(s):
    my_dict = {}
    for i in s:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    print(my_dict)
    return my_dict


# {'h': 1, 'i': 1, 'p': 2, 'o': 2, ' ': 3, 'r': 1, 'u': 2, 'n': 1, 's': 2, 't': 1, '!': 1}
char_counter('hippo runs to us!')
char_counter(s)
