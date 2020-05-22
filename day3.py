import math


# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of
# width and height, using a cost entered by the user.

width = float(input("Width of floor: "))
length = float(input("Length of floor: "))
cost = float(input("Cost of Tile (per m2): "))

print(f'Cost to tile a {width} x {length} floor is: ${width * length * cost}')

# Change Return Program - The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of quarters, dimes, nickels,
# pennies needed for the change.


def money_exchange(d, amount):
    i = 0
    used = [0] * len(d)
    # used1 = enumerate(used)
    used3 = {}
    while (amount > 0) and i < len(d):  # go until all money gone
        # get num of that d to use, always round down
        num = math.floor(amount / d[i])
        used[i] = num  # say we've used it
        used3[d[i]] = num
        amount = amount - num * d[i]  # set new amount
        i += 1  # go to next d
    # print(list(used1))
    print(used3)
    print(used)
    return used


# print([0] * 5)

money_exchange([2, 1, .5, .2, .1, .05], 29.85)
