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


def all_continents1(lst):
    return len(set(x["continent"] for x in lst)) == 5


def quarter_of(n):
    return (n + 2) // 3


# quarter_of1 = lambda m: __import__('math').ceil(m / 3)
