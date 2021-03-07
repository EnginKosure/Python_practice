def find_odd(s):
    return [i for i in s if i % 2]


print(find_odd([1, 2, 3, 4, 5, 6]))


def question_marks(s):
    for k, v in enumerate(s):
        print(k, v)


question_marks('acc?7??sss?3rr1??????5"')


def avg_t(**scores):
    sum_t = 0
    for v in scores.values():
        sum_t += v
    print(sum_t/len(scores.values()))


dd = {'Mary': 85, 'Susan': 75, 'Barry': 65, 'Alexis': 88,
      'Jane': 45, 'Tina': 100, 'Tom': 90, 'Tim': 60}

avg_t(**dd)


def domainGet(email):
    return email.split('@')[-1]


domainGet('user@domain.com')
