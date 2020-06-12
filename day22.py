import math

'''
from math import degrees
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
