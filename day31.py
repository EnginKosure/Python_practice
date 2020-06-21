# "Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
# Ekrana yazdırma işlemini **format** metoduyla yapmaya çalışın."

num1 = int(input('Enter the first number: '))  # '5' -> 5
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
result = num1*num2*num3

# The multiplication of 2, 4 and 5 is 40
print(f'The multiplication of {num1}, {num2} and {num3} is {result}')
print('The multiplication of {}, {} and {} is {}'.format(
    num1, num2, num3, result))
print('%s %d %s %d %s %d %s %d' % ('The multiplication of',
                                   num1, ',', num2, 'and', num3, 'is', result))
