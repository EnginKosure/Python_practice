def find_odd(s):
    return [i for i in s if i % 2]


print(find_odd([1, 2, 3, 4, 5, 6]))


def question_marks(s):
    for k, v in enumerate(s):
        print(k, v)


question_marks('acc?7??sss?3rr1??????5"')
