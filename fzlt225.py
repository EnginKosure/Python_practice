def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


def name_shuffler1(s):
    return ' '.join(reversed(s.split()))


# name_shuffler2 = lambda s: ' '.join(reversed(s.split(' ')))
