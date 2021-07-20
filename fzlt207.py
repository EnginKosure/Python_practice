# add_one=lambda x:x+1
def add_one(x): return x+1


added = add_one(3)
print(added)  # 4

numbers = [1, 2, 3, 4]
times_two = map(lambda x: x * 2, numbers)
lst = list(times_two)
print(lst)  # [2, 4, 6, 8]
