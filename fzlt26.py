def allAnagram(input):

    # empty dictionary which holds subsets
    # of all anagrams together
    my_dict = {}

    # traverse list of strings
    for strVal in input:

        # sorted(iterable) method accepts any
        # iterable and rerturns list of items
        # in ascending order
        key = ''.join(sorted(strVal))
        print(key)

        # now check if key exist in dictionary
        # or not. If yes then simply append the
        # strVal into the list of it's corresponding
        # key. If not then map empty list onto
        # key and then start appending values
        if key in my_dict.keys():
            my_dict[key].append(strVal)
        else:
            my_dict[key] = []
            my_dict[key].append(strVal)

     # traverse dictionary and concatenate values
     # of keys together
    output = []
    print(my_dict)
    for key, value in my_dict.items():
        output.append(value)

    return output


xx = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(allAnagram(xx))
