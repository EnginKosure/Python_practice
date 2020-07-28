import string


def print_rangoli(size):
    x = string.ascii_lowercase[:size]
    print('x', x)
    width = size+(size-1)
    width += width-1
    for ii in range(1, size):
        print("-".join(x[-1:-ii:-1]+x[-ii:]).center(width, "-"))
    for i in range(size):
        print("-".join(x[size-1:i:-1]+x[i:]).center(width, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
