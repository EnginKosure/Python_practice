import math
import datetime

'''
from math import degrees
#degrees() method ->Converts angles from radians to degrees.
def to_degree(radians):
    return round(degrees(radians))
'''


def to_degree(radian):
    return round(180*radian/math.pi)


#to_degree2 = lambda r: round(r/math.pi*180)
# to_degree2 = lambda r: r/math.pi*180
def to_degree2(r): return round(r/math.pi*180)


print(to_degree(6.18))
print(to_degree2(3.142*2))


def time_for_milk_and_cookies(date):
    return date.month == 12 and date.day == 24
    # return  [date.month,date.day] == [11,24]


print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))  # True
