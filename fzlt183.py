list1 = [
    {'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil',
        'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus',
        'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no'},
    {'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia',
        'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes'},
    {'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland',
        'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no'}
]


def find_admin(lst, lang):
    admins = []
    for i in lst:
        if i['language'] == lang and i['githubAdmin'] == 'yes':
            admins.append(i['firstName'])
    return admins


def find_admin1(lst, lang):
    return [i for i in lst if i['language'] == lang and i['githubAdmin'] == 'yes']


print(find_admin(list1, 'JavaScript'))
