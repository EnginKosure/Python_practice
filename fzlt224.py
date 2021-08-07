import math
import numpy as np


def get_average(marks):
    return int(np.mean(marks))


def epidemic(tm, n, s0, i0, b, a):
    dt = tm / n
    i_array = [i0 for _ in range(n)]
    s_array = [s0 for _ in range(n)]
    r_array = [0 for _ in range(n)]
    for i in range(n - 1):
        i_array[i + 1] = i_array[i] + dt * \
            (b * s_array[i] * i_array[i] - a * i_array[i])
        s_array[i + 1] = s_array[i] - dt * b * s_array[i] * i_array[i]
        r_array[i + 1] = r_array[i] + dt * i_array[i] * a

    return math.ceil(max(i_array))
