# to find the max layers built with 2 decks of cards

total_cards = 104
n = 0
used_cards = 0

while total_cards - 3 * n > 0:
    n += 1
    used_cards += 3 * n
    total_cards -= 3 * n

print('total used', used_cards)  # 84
print('remainder', total_cards)  # 20
print('total layers', n)         # 7
print('roof', used_cards * 2 / 3)  # 56
print('base', used_cards / 3)  # 28


def res(tot, m=0, used=0):
    if tot - 3 * m > 0:
        m += 1
        tot -= 3 * m
        used += 3 * m
        print(m, used, tot)
        return res(tot, m, used)
    else:
        print("layers", m)
        print('used', used)
        print("remained", tot)
        print('for roofs', used * 2 / 3)
        print('for bases', used / 3)

res(104)

