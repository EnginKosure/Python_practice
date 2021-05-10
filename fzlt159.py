s = ((1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31),
     (2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31),
     (4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31),
     (8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31),
     (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))


def guess_number(answers):
    return sum([x[0] for index, x in enumerate(s) if (answers[index] == 1)])


def answers_sequence(n):
    return [1 if n in x else 0 for index, x in enumerate(s)]


def guess_number1(answers):
    return int(''.join(map(str, reversed(answers))), 2)


def answers_sequence1(n):
    return list(map(int, reversed(f"{n:05b}")))
