# shuffling a deck of cards

from random import randrange


def create_deck():
    cards = []

    for suit in ['s', 'h', 'd', 'c']:
        for value in ['2', '3', '4', '5', '6', '7', '8', '9',
                      'T', 'J', 'Q', 'K', 'A']:
            cards.append(value + suit)
    return cards


def shuffle(cards):
    for i in range(0, len(cards)):
        ran_pos = randrange(0, len(cards))

        temp, cards[i] = cards[i], cards[ran_pos]


def main():
    cards = create_deck()
    print('The original deck: ')
    print(cards)

    shuffle(cards)
    print('The shuffled deck: ')
    print(cards)


if __name__ == '__main__':
    main()
