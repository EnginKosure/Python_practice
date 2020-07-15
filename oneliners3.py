# Data
t = ['lambda functions are anonymous functions.',
     'anonymous functions do not have a name.',
     'functions are objects in Python.']
q = 'anonymous'  # query

# One-Liner
mark = map(lambda s: (1, s) if q in s else (0, s), t)

# Result
print(list(mark))
# [(1, 'lambda functions are anonymous functions.'),
# (1, 'anonymous functions do not have a name.'),
# (0, 'functions are objects in Python.')]
