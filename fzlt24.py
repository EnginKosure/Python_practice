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


def find_bob_3(names):
    if 'Bob' in names:
        return names.index('Bob')
    else:
        return -1


def find_bob_4(*args):
    for n in args:
        if n == "Bob":
            return args.index(n)
            break
    else:
        return -1


print(find_bob_4("B", "Jimmy", "Layla", "Bob"))
print(find_bob_4("B", "Jimmy", "Layla"))


def find_bob_5(names):
    return names.index("Bob") if "Bob" in names else -1
