def list_of_multiples(x, y):
    a = []
    b = x
    for i in range(y):
        a.append(b)
        b += x
    print(a)
    return a


def list_of_multiples1(num, length):
    return [i*num for i in range(1, length+1)]


def list_of_multiples2(num, length):
    return list(range(num, num*length+1, num))


list_of_multiples(7, 5)  # [7, 14, 21, 28, 35]

list_of_multiples(12, 10)  # [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

list_of_multiples(17, 6)  # [17, 34, 51, 68, 85, 102]
