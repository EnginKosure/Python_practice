# Classes and Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# Create a Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


# Create Object
p1 = Person("Jef", 1500)

p1.myfunc()
# Hello my name is Thor
# Note 1: The __init__() function is called automatically every time the class is being
# used to create a new object, also known as constructor in other OO languages.
# Note 2: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
