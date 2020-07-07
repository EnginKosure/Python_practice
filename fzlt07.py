control_var = True

while control_var:
    number = input("Enter the number : ")

    if '.' in number:
        number = input("Please enter an integer number : ")
        continue
    elif number.isdigit() and int(number) < 0:
        number = input("Please enter a positive number : ")
        continue
    elif not number.isdigit():
        number = input("Please enter only numbers : ")
        continue

    else:
        control_var = False

n = len(number)
print(n)
sum_nth_pow = 0

for i in number:
    sum_nth_pow += int(i)**n
if int(number) == sum_nth_pow:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
