# We're given a hashmap associating each courseId key with a list of courseIds values,
# which represents that the prerequisites of courseId are courseIds.
# Return a sorted ordering of courses such that we can finish all courses.
# Return null if there is no such ordering.
# For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
# should return ['CSC100', 'CSC200', 'CSC300'].


def order_lesson(o):
    return [k if k != [] or k in sorted(o.items())[sorted(o.items()).index(k)+1] else None for k, l in sorted(o.items())]


course = {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}
w = {'CSC400': ['CSC100', 'CSC200'], 'CSC300': [],
     'CSC200': ['CSC100'], 'CSC100': []}
print(order_lesson(course))  # ['CSC100', 'CSC200', 'CSC300']
print(order_lesson(w))  # ['CSC100', 'CSC200', 'CSC300', 'CSC400']


answer = []
for i in range(len(course.keys())):
    for j in course.keys():
        answer.append(j) if ((course[j] == answer or len(
            course[j]) <= len(answer)) and j not in answer) else answer
print(answer)


def ordered_courses(courses):
    c = courses.copy()
    result = []
    while [] in c.values():
        noreq = [k for k, v in c.items() if v == []]
        for i in noreq:
            result.append(i)
            del c[i]
            c = {k1: [v2 for v2 in v1 if v2 != i] for k1, v1 in c.items()}
    return result if len(c) == 0 else None
