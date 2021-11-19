
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
