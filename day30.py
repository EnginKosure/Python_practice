# Task-1:

# Write a short Python program that asks the user to enter Celsius temperature
# (it can be a decimal number), converts the entered temperature into
# Fahrenheit degree and prints the result.


def convert_to_fahrenheit(c):
    fahrenheit = c*1.8+32
    # print('% .2f %s % .2f %s' %
    #       (c, 'celcius equals to', fahrenheit, 'fahrenheit'))
    print('{} {} {:.2f} {}'.format(
        c, 'celcius equals to', fahrenheit, 'fahrenheit'))
    return fahrenheit


celcius = float(input("Enter temperature in Celcius: "))
convert_to_fahrenheit(celcius)

# Task-2:
# Write a short Python program that asks the user to enter a distance
# (it can be a decimal number) in kilometers,
# converts the entered distance into miles and prints the result.
