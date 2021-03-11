# Create a function that takes a number num and returns each place value in the number.


def num_split(num):
    numb = -1*num if num < 0 else num
    lst = []
    for i in range(len(str(numb))):
        lst.append(int(str(numb)[i])*10**(len(str(numb))-1-i))
    return lst if num >= 0 else [-1*i for i in lst]


num_split(39)  # [30, 9]

num_split(-434)  # [-400, -30, -4]

num_split(100)  # [100, 0, 0]
