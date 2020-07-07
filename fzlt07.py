number = input("Enter the number : ")
n = len(number)
print(n)
sum_nth_pow = 0

for i in number:
    sum_nth_pow += int(i)**n
if int(number) == sum_nth_pow:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
