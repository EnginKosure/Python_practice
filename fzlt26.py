def group_anagrams(input):

    # start an empty dictionary to hold the values
    my_dict = {}

    # traverse list of strings
    for s in input:

        key = ''.join(sorted(s))
        # print(key)  #'aet'

        # check if key exist in dictionary or not.
        # If yes append the s into the list of corresponding key.
        # If not then start an empty list on the key and then append values
        if key in my_dict.keys():
            my_dict[key].append(s)
        else:
            my_dict[key] = []
            my_dict[key].append(s)

    output = []

    # print(my_dict)
    # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
    for key, value in my_dict.items():
        output.append(value)

    return output


xx = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(xx))  # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
