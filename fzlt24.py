def find_bob(names):
    for i in names:
        if i == 'Bob':
            return names.index(i)
    else:
        return -1


print(find_bob(["Jimmy", "Layla", "Mandy", 'Bob']))
print(find_bob(["Jimmy", "Layla", "Mandy"]))


def find_bob_2(names):
    try:
        return names.index('Bob')
    except:
        return -1
