from math import factorial


def fact_of_fact(n):
    a = 1
    for i in range(1, n+1):
        a *= factorial(i)
    return a


print(fact_of_fact(5))  # 288
# 4! * 3! * 2! * 1! = 288

# fact_of_fact(5)  # 34560

# fact_of_fact(6)  # 24883200


def param_count(*args):
    return len(args)
