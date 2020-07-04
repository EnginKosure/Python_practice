def sum_square(n):
    sum_sq = 0
    for i in range(n+1):
        sum_sq += i**2
    print(sum_sq)
    return sum_sq


sum_square(10)
