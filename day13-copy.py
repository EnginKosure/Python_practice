# to find the max layers built with 2 decks of cards
# This time, the lowest level basement is empty


def res(total_cards):

    n = 0
    used_cards = 0
    roof = 0
    base = 0

    while total_cards - 3 * n + 1 > 0:
        n += 1
        used_cards += 3 * n - 1
        total_cards -= 3 * n - 1
        roof += 2*n
        base += n-1

    print('total used', used_cards)  # 84
    print('remainder', total_cards)  # 20
    print('total layers', n)         # 7
    print('roof', roof)  # 72
    print('base', base)  # 28


res(104)
total_card_num = int(input('Enter total card number: '))
res(total_card_num)
