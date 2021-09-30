def find_cons(s):
    return max([len(i) for i in s.split('1')])


print(find_cons('1001101000110'))
