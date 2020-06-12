import math


def to_degree(radian):
    return round(180*radian/math.pi)

# to_degree = lambda r: r/math.pi*180


print(to_degree(6.18))
