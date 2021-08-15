def longest_repetition(chars):
    if chars == '':
        return '', 0

    # split the string in to individual characters
    lst = list(chars)

    # create a new string that will hold the groups of characters
    # separated by spaces
    txt = ' '

    for e in lst:
        # grouping the characters
        txt = txt + e if txt[-1] is e else txt + " " + e

    # creating a list with the groups
    txt_list = txt.split()

    # creating base values for the character and repetition
    chr, rep = '', 0

    for e in txt_list:
        # if the current lenght of the group is bigger then previous groups
        if rep < len(e):
            # set new character as the one from the current checked group
            chr = e[0]
            # set the repetition number to the current length of the group
            rep = len(e)

    return chr, rep
