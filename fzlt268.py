import logging
# import sh
from itertools import count
import heapq
import time

# for i in range(10):
#     for i in range(4):
#         time.sleep(0.5)
#         print("\a")  # \a is reserved to warning notification sound in Windows
#     time.sleep(3)


lst = "10, 50, 100, 500, 1000, 5000"
for i in lst:
    if i == str(0):
        print(i, end="|")


ten_billion = 10_000_000_000

print(f'{ten_billion:,}')
# 10,000,000,000


# from 13 cards
cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# extract ace, 2, 3 only
# if you won't use the variable in the future, you can assign to _underscore
ace, two, three, *_ = cards
print(ace, two, three)
# A 2 3


# extract ace, 2, 3 only
ace, two, three, *others = cards
print(ace, two, three)  # A 2 3
print(others)  # ['4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


# extract ace, [numbers], J, Q, K
ace, *numbers, J, Q, K = cards
print(ace, numbers, J, Q, K)
# A['2', '3', '4', '5', '6', '7', '8', '9', '10'] J Q K


# For ~ Else
grades = ['A', 'B', 'C', 'D', 'E', 'F']

my_grade = 'A+'

for grade in grades:
    if grade == my_grade:
        print('grade found')
        break
else:
    print('grade not found')

# grade not found


grades = [5, 78, 6, 30, 91, 1005.2, 741, 1.9, 112, 809.5]
print(heapq.nlargest(2, grades))


c = count()

for i in range(20):
    print(next(c), end="|")


# sh.google_chrome('http://google.com')


logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything
