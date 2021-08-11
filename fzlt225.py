def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


def name_shuffler1(s):
    return ' '.join(reversed(s.split()))


# name_shuffler2 = lambda s: ' '.join(reversed(s.split(' ')))


def all_continents(lst):
    cont = []
    for i in lst:
        cont.append(i['continent'])
    return True if sorted(set(cont)) == ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania'] else False
