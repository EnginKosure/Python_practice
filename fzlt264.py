
import this
import sys
# Check The Memory Usage Of An Object.
x = 1
print(sys.getsizeof(x))

test = ['I', 'Like', 'Python', 'automation']

print(' '.join(test))


test1 = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test1), key=test1.count))


def some_func():
    ...
    print(...)  # Ellipsis


some_func()


def add_one(x): return x+1


print(add_one(4))

numbers = [1, 2, 3, 4]
times_two = map(lambda x: x * 2, numbers)

print(list(times_two))  # [2, 4, 6, 8]


my_list = [[j for j in range(3)] for i in range(4)]
print(my_list)  # [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]


flatten = [value
           for sublist in my_list
           for value in sublist]

print(flatten)


if not sys.version_info > (2, 7):
    print('congrats for still using a 10 year old version')
elif not sys.version_info >= (3, 5):
    print('Please upgrade')
else:
    # sys.version_info(major=3, minor=8, micro=3, releaselevel='final', serial=0)
    print(sys.version_info)
    print(sys.version_info >= (3, 8, 2))  # True


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}

print(merged)


a = 12
b = 13
a, b = b, a
print(a, b)
