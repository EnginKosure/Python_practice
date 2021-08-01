# An iterator is an object that can be iterated upon, meaning that you can
# traverse through all the values.
# To create an object/class as an iterator you have to implement the methods
#  __iter__() and __next__() to your object.
# Example:
class MySequenceGenerator:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


my_generator = MySequenceGenerator()
my_iter = iter(my_generator)

next(my_iter)
next(my_iter)
next(my_iter)
# Note: The __iter__() method acts similar to __init__() where you can do operations
# (initializing etc.), but must always return the iterator object itself.
# Note: The __next__() method also allows you to do operations,
# and must return the next item in the sequence.
