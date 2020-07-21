# Data
cols = ['name', 'salary', 'job']
db = [('Alice', 180000, 'scientist'),
      ('Bob', 99000, 'manager'),
      ('Frank', 87000, 'CEO')]

# One-Liner
db = [dict(zip(cols, row)) for row in db]

# Result
print(db)
# [{'name': 'Alice', 'salary': 180000, 'job': 'scientist'},
# {'name': 'Bob', 'salary': 99000, 'job': 'manager'},
# {'name': 'Frank', 'salary': 87000, 'job': 'CEO'}]
