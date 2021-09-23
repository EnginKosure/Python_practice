list1 = [
    {'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco',
        'continent': 'Europe', 'age': 49, 'language': 'PHP'},
    {'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia',
        'continent': 'Asia', 'age': 38, 'language': 'Python'},
    {'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania',
        'continent': 'Europe', 'age': 19, 'language': 'Python'},
    {'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan',
        'continent': 'Asia', 'age': 49, 'language': 'PHP'},
]

# sorted(orders.items(), key=lambda x: x[1], reverse=True)


def find_senior(lst):
    a = list(i.items() for i in lst)
    # return list(i.keys() for i in a)
    return a


print(find_senior(list1))
