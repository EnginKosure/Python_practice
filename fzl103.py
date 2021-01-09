# 80 >> 3 = floor(80/2^3) = floor(80/8) = 10
# -24 >> 2 = floor(-24/2^2) = floor(-24/4) = -6
# -5 >> 1 = floor(-5/2^1) = floor(-5/2) = -3

def shift_to_right(a, b):
    print(a//2**b)


shift_to_right(80, 3)  # 10

shift_to_right(-24, 2)  # -6

shift_to_right(-5, 1)  # -3

shift_to_right(4666, 6)  # 72

shift_to_right(3777, 6)  # 59

shift_to_right(-512, 10)  # -1
