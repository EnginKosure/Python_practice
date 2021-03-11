# Create a function that takes a number num and returns each place value in the number.


def num_split(num):
    numb = -1*num if num < 0 else num
    lst = []
    for i in range(len(str(numb))):
        lst.append(int(str(numb)[i])*10**(len(str(numb))-1-i))
    return lst if num >= 0 else [-1*i for i in lst]
