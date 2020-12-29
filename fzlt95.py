# Starting with either 3 or 5 and given these operations:

# add 5
# multiply by 3
# You should say if it is possible to reach the target number n.

def only_5_and_3(n):
    return [True if n % 3 == 0 or n-5 == 0 else only_5_and_3(n-3)]


only_5_and_3(14)  # True
# 14 = 3*3 + 5

only_5_and_3(25)  # True
# 25 = 5+5+5+5+5

only_5_and_3(7)  # False
# There exists no path to the target number 7
