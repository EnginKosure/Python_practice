import math


def is_prime(num):
    if num >= 2:
        i = 2
        while i <= math.sqrt(num):
            if num % i == 0:
                i += 1

                return False
            else:
                return True
    else:
        return False


def truncatable(num):
    right = sum([1 for i in range(1, len(str(num))+1)
                 if is_prime(int(str(num)[:i]))]) == len(str(num))
    left = sum([1 for i in range(len(str(num))) if is_prime(
        int(str(num)[i:]))]) == len(str(num))
    if "0" in str(num):
        return False
    else:
        return "both"*left*right or "right"*right or "left"*left or False


truncatable(62383)
