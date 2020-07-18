# Write a Python code to sort the list at below without using .sort() method of list.
# elements of list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
# Expected output:
# [2, 11, 12, 45, 77, 99, 333, 999, 8982]

mylist = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[i] > mylist[j]:
            # temp = mylist[i]
            # mylist[i] = mylist[j]
            # mylist[j] = temp
            mylist[i], mylist[j] = mylist[j], mylist[i]
print(mylist)
