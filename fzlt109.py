a = [3, 5, 12, 5, 13]
b = {True for i in a for j in a if i**2 + j**2 in [k**2 for k in a]}
print(b)
