# Create a function that takes a list of numbers and returns
# the sum of all prime numbers in the list.

def sum_primes(arr):
    if len(arr) == 0:
        return None
    return sum([x for x in arr
                if all(x % y for y in range(2, x)) and x != 1])


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # 17

print(sum_primes([2, 3, 4, 11, 20, 50, 71]))  # 87

print(sum_primes([]))  # None
