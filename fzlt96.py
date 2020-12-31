# revisit exec() method
'''
The exec() method executes the dynamically created program, 
which is either a string or a code object.

exec() takes three parameters:

object - Either a string or a code object
globals (optional) - a dictionary
locals (optional)- a mapping object. 
Dictionary is the standard and commonly used mapping type in Python.
'''
# exec() doesn't return any value, it returns None.

program = 'a = 5\nb=10\nprint("Sum =", a+b)'
exec(program)  # Sum = 15
