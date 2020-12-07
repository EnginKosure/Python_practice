# Write a function that takes coordinates of two points on a two-dimensional plane and
# returns the length of the line segment connecting those two points.
def line_length(a1, a2):
    return round(((a1[0]-a2[0])**2+(a1[1]-a2[1])**2)**.5, 2)


print(line_length([15, 7], [22, 11]))  # ➞ 8.06

print(line_length([0, 0], [0, 0]))  # ➞ 0

print(line_length([0, 0], [1, 1]))  # ➞ 1.41
