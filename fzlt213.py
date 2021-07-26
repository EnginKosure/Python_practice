sample_data = [
    {"id": 1, "name": "Amol", "project": False},
    {"id": 2, "name": "Kiku", "project": False},
    {"id": 3, "name": None, "project": False},
    {"id": 4, "name": "Lini", "project": True},
    {"id": 4, "name": None, "project": True},
]

# With Python 3.8 Walrus Operator
for entry in sample_data:
    if name := entry.get("name"):
        print("Found Person:", name)

# Found Person: Amol
# Found Person: Kiku
# Found Person: Lini

# Without Walrus Operator
for entry in sample_data:
    name = entry.get("name")
    if name:
        print('Found Person:', name)

# Found Person: Amol
# Found Person: Kiku
# Found Person: Lini
