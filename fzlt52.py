# We're given a hashmap associating each courseId key with a list of courseIds values,
# which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.
# Return null if there is no such ordering.
# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
# should return ['CSC100', 'CSC200', 'CSC300'].


def order_lesson(o):
    return [k for k, l in sorted(o.items()) if k != [] or k in sorted(o.items())[sorted(o.items()).index(k)+1]]


z = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
print(order_lesson(z))  # ['CSC100', 'CSC200', 'CSC300']
