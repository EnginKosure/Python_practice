# Each player rolls his dice three times.
# Each player takes the maximal value of his three results.
# The player with the larger number wins.

# INPUT: an integer number n>=0

# OUTPUT: two integers a and b,
# the numerator and denominator of the probability written as a/b
# (with the smallest possible b) that you will win the game with your three attempts
def magicdice(n):
    return ((2**n)**3-(2**n-1)**3, (2**n)**3)
    # return (0, 1)


print(magicdice(5))  # (2977, 32768)
