
import sys
# Check The Memory Usage Of An Object.
x = 1
print(sys.getsizeof(x))

test = ['I', 'Like', 'Python', 'automation']

print(' '.join(test))


test1 = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test1), key=test1.count))
