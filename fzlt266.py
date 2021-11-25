from collections import Counter
import jmespath
persons = {
    "persons": [
        {"name": "erik", "age": 38},
        {"name": "john", "age": 45},
        {"name": "rob", "age": 14}
    ]
}
print(jmespath.search('persons[*].age', persons))
print(jmespath.search('persons[*].name', persons))
# [38, 45, 14]


mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
c = Counter(mylist)
print(c)
