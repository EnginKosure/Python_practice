'''
the words and patterns are all lowercase
the order of the returned words doesn't matter
'''

from random import choice, choices, randint, random, sample


class Dictionary:
    def __init__(self, words):
        self.words = words

    def get_matching_words(self, pattern):
        res = []
        for word in self.words:
            if len(word) == len(pattern) and all(x == y for x, y in zip(word, pattern) if y != '?'):
                res.append(word)
        return res


def example_tests():
    dictionary = Dictionary(['apple', 'cherry', 'strawberry', 'raspberry', 'orange',
                             'melon', 'pineapple', 'papaya', 'lemon', 'blackberry', 'lime', 'banana'])
    tests = {
        '?????berry': ['strawberry', 'blackberry'],
        '?e?on': ['melon', 'lemon'],
        '?a?a?a': ['banana', 'papaya'],
        '??????': ['cherry', 'orange', 'papaya', 'banana'],
        '?????????': ['raspberry', 'pineapple'],
        '???': [],
        'cherr??': [],
        '?pple': ['apple'],
        'appl?': ['apple'],
        '?apple?': [],
        '????apple': ['pineapple'],
        'potato': []
    }
    for pattern, expected in tests.items():
        actual = sorted(dictionary.get_matching_words(pattern))
        expected = sorted(expected)
        print(expected)


example_tests()
