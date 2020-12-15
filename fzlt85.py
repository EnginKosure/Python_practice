# Create a function that returns a list containing the prime factors
# of whatever integer is passed to it.

def prime_factors(n: int) -> List[int]:
    a = []
    while n % 2 == 0:
        a.append(2)
        n /= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n /= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    # Only odd number is possible
    return a


print(prime_factors(20))  # [2, 2, 5]

prime_factors(100)  # [2, 2, 5, 5]

prime_factors(8912234)  # [2, 47, 94811]
