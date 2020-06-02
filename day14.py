# Reverse lookup
def reverse_lookup(data, value):
    keys = []

    # check each key, adding it to keys if the values match
    for key in data:
        if data[key] == value:
            keys.append(key)

    return keys


def main():
    fr_en = {'le': 'the', 'la': 'the', 'livre': 'book', 'pomme': 'apple'}

    print('The French words for "the" are: ', reverse_lookup(fr_en, 'the'))


if __name__ == '__main__':
    main()
