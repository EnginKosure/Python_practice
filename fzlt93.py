# A format for expressing an ordered list of integers is to use
# a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated
# from the end integer in the range by a dash, '-'. The range
# includes all integers in the interval including both endpoints.
# It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in
# increasing order and returns a correctly formatted string in the range format.


def solution(numberlist):
    prev_number = min(numberlist) if numberlist else None
    pagelist = list()

    for number in sorted(numberlist):
        if number != prev_number+1:
            pagelist.append([number])
        elif len(pagelist[-1]) > 1:
            pagelist[-1][-1] = number
        else:
            pagelist[-1].append(number)
        prev_number = number
    x = ','.join(['-'.join(map(str, page)) for page in pagelist])
    print(x)
    return x


solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8,
          9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
