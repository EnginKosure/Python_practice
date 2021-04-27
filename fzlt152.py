from random import randint
heads = 0
for i in range(1, 1001):
    if randint(0, 1) == 1:
        heads += 1
print('Heads came up ' + str(heads) + ' times.')
