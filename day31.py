# "Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
# Ekrana yazdırma işlemini **format** metoduyla yapmaya çalışın."

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))

print(f'The multiplication of {num1}, {num2} and {num3} is {num1*num2*num3}')
print('The multiplication of {}, {} and {} is {}'.format(
    num1, num2, num3, num1*num2*num3))
print('%s %d %s %d %s %d %s %d' % ('The multiplication of',
                                   num1, ',', num2, 'and', num3, 'is', num1*num2*num3))

print('The multiplication of {1}, {2} and {3} is {4}'.format(
    {1=num1}, {2=num2}, {3=num3}, {4=num1*num2*num3}))
