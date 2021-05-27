def counter(s):
    return len(set([ch for ch in s if s.count(ch) % 2]))


def lowest(s):
    cnt = counter(s)
    if not s:
        return 0
    return int(len(s) / cnt) - (int((len(s) / cnt) % 2) == 0) if cnt else len(s)
