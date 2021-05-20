# All integers can be uniquely expressed as a sum of powers of 3 using each power of 3 at most once.

# For example:

# 17 = (-1) +   0  + (-9) + 27 = (-1 * 3^0) + ( 0 * 3^1) + (-1 * 3^2) + (1 * 3^3)
# -8 =   1  +   0  + (-9)      = ( 1 * 3^0) + ( 0 * 3^1) + (-1 * 3^2)
# 25 =   1  + (-3) +   0  + 27 = ( 1 * 3^0) + (-1 * 3^1) + ( 0 * 3^2) + (1 * 3^3)

# We can use the string +-0+ to represent 25 as the sum of powers of 3:

# Symbols      :   "+"   "-"   "0"   "+"
# Powers of 3  :    1     3     9    27
# Values       :    1    -3     0    27
# Given an integer n (not necessarily strictly positive),
# we want to write a function that expresses n as a sum of powers of 3 using the symbols -0+:
def as_sum_of_powers_of_3(n):
    m = n
    s = ""
    p = 0
    while m >= 2:
        m //= 3
        p += 1
    print(p, m)


as_sum_of_powers_of_3(17)  # "-0-+"
# as_sum_of_powers_of_3(-8)  # "+0-"
