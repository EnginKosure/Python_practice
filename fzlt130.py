a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def within_bounds(value, low=3, high=7):
    return low <= value < high


filter(within_bounds, a_list)
