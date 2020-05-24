from random import random

# Unit Converter (temp) -
# Converts various units between one another. The user enters the type of unit being entered,
# the type of unit they want to convert to and then the value. The program will then make the conversion.


temps = {'cf': lambda c: c * (9 / 5) + 32,
         'fc': lambda f: (f - 32) * (5 / 9),
         'ck': lambda c: c + 273.15,
         'kc': lambda k: k - 273.15,
         'fk': lambda f: (f + 459.67) * 5 / 9,
         'kf': lambda k: k * (9 / 5) - 459.67
         }
input1 = input('From which unit to convert into what: Select among cf, fc, ck, kc, fk, kf : ')
input2 = int(input('Value to convert: '))

print(temps[input1](input2))


# Coin Flip Simulation - Write some code that simulates flipping a single coin however many times the user decides.
# The code should record the outcomes and count the number of tails and heads.


def flip():
    flip = random()
    if flip >= .5:
        return True
    else:
        return False


def main(num):
    heads = 0
    tails = 0
    result_string = ""

    for i in range(int(num)):
        if flip():
            heads += 1
            result_string += "H"
        else:
            tails += 1
            result_string += "T"

    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")
    print(result_string)


userInput = input("Please enter a number of flips: ")
main(userInput)
