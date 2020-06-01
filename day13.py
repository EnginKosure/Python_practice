# to find the max layers built with 2 decks of cards

total_cards = 104
n = 0
used_cards = 0

while total_cards - 3 * n > 0:
    n += 1
    used_cards += 3 * n
    total_cards -= 3 * n

print('total used', used_cards)
print('remainder', total_cards)
print('total layers', n)
print('roof', used_cards * 2 / 3)
print('base', used_cards / 3)
