arr = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 10]
arr[3:3] = 'string'
print(arr)

s = ['aaaa', 'bbbb', 'cccc', 'dddd']
s[2:2] = 'pppp'
# print(s)
# arr[2:2] = 55
# [1, 2, 2, 's', 't', 'r', 'i', 'n', 'g', 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 10]
print(arr[3])  # 's'
print(arr[3:4])  # ['s']
# What is written to put 'George' between 'Bill' and 'Ronald'?
presidents = ['Barrack', 'George', 'Bill',
              'Ronald', 'Jimmy', 'Gerald', 'Richard']
presidents[3:3] = ['George']
print(presidents)


old = {"Emma": 71, "Jack": 89, "Amy": 15, "Ben": 29}
print(max(old, key=old.get))
print(max(old, key=old.setdefault))
