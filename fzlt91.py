# Given a list of four points in the plane, determine if
# they are the vertices of a parallelogram.

is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)])  # True

is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)])  # False

is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)])  # True

is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)])  # True

is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)])  # True
