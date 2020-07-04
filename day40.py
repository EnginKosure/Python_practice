def sum_square(n):
    sum_sq = 0
    for i in range(n+1):
        sum_sq += i**2
    print(sum_sq)
    return sum_sq


sum_square(10)


def square_sum(n):
    sq_sum = 0
    for i in range(n+1):
        sq_sum += i
    print(sq_sum**2)
    return sq_sum**2


square_sum(10)
