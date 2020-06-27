def ascending(txt):
    splitted = [split_txt(txt, step) for step in range(1, len(txt)//2+1)]
    return any([is_iterate(txt) for txt in splitted])


def split_txt(txt, step):
    ch, s, splited = '', step, []
    for i in txt:
        ch += i
        s -= 1
        if not s:
            splited.append(ch)
            ch, s = '', step
    if ch != '':
        splited.append(ch)
    return splited


def is_iterate(txt):
    start, boolList = int(txt[0]), []
    for i in txt[1:]:
        if int(i) != start+1:
            return False
        else:
            start = int(i)
    return True


print(ascending("57585960616263"))  # True
print(ascending('123412351236'))  # True
print(ascending('444445'))  # True
print(ascending('2324256'))  # False
print(ascending('35236237238'))  # False
print(ascending('1235'))  # False
