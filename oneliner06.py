# Companies
c = {'CoolCompany': {'Alice': 33,
                     'Bob': 28,
                     'Frank': 29},
     'CheapCompany': {'Ann': 4,
                      'Lee': 9,
                      'Chrisi': 7},
     'SosoCompany': {'Esther': 38,
                     'Cole': 8,
                     'Paris': 18}}

# One-Liner to find illegal companies
i = [x for x in c if any(y < 9 for y in
                         c[x].values())]

# Result
print(i)
# ['CheapCompany', 'SosoCompany']
