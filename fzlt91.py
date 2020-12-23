# Given a list of four points in the plane, determine if
# they are the vertices of a parallelogram.
from math import hypot


def is_parallelogram(arr):
    # a = (arr[0][0]-arr[1][0] == arr[2][0]-arr[3][0]) or (arr[0][0]-arr[3][0] == arr[1][0] -
    #                                                      arr[2][0]) and (arr[0][1]-arr[1][1] == arr[2][1] -
    #                                                                      arr[3][1]) or (arr[0][1]-arr[3][1] == arr[1][1]-arr[2][1])
    # print(a)
    # return a
    print(hypot(arr[0][0], arr[0][1]))
    print(hypot(arr[1][0], arr[1][1]))
    print(hypot(arr[2][0], arr[2][1]))
    print(hypot(arr[3][0], arr[3][1]))
    print('-------------')
    # print(hypot(arr[1]))
    # print(hypot(arr[2]))
    # print(hypot(arr[3]))

    # 𝑃𝑥−𝑄𝑥=𝑅𝑥−𝑆𝑥
    # arr[0][0]-arr[1][0]==arr[2][0]-arr[3][0]
    # 𝑃𝑥−𝑆𝑥=𝑄𝑥−𝑅𝑥
    # arr[0][0]-arr[3][0]==arr[1][0]-arr[2][0]
    # 𝑃𝑦−𝑄𝑦=𝑅𝑦−𝑆𝑦
    # arr[0][1]-arr[1][1]==arr[2][1]-arr[3][1]
    # 𝑃𝑦−𝑆𝑦=𝑄𝑦−𝑅𝑦
  # arr[0][1]-arr[3][1]==arr[1][1]-arr[2][1]
is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)])  # True

is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)])  # False

is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)])  # True

is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)])  # True

is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)])  # True
