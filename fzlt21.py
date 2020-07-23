data = ['G', 'B', 'R', 'R', 'B', 'R', 'G', 'B']
data = [*[i for i in data if i == "B"], *
        [i for i in data if i == "G"], *[i for i in data if i == "R"]]
print(data)

R, G, B = data.count('R'), data.count('G'), data.count('B')

lst = [*'B'*B, *'G'*G, *'R'*R]
print(lst)
