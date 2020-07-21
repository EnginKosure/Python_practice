# Data
cols = ['name', 'salary', 'job']
db = [('Alice', 180000, 'scientist'),
      ('Bob', 99000, 'manager'),
      ('Frank', 87000, 'CEO')]

# One-Liner
db = [dict(zip(cols, row)) for row in db]

# Result
print(db)
