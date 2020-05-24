# Unit Converter (temp, currency, volume, mass and more) -
# Converts various units between one another. The user enters the type of unit being entered,
# the type of unit they want to convert to and then the value. The program will then make the conversion.


temps = {'cf': lambda c: c * (9 / 5) + 32,
         'fc': lambda f: (f - 32) * (5 / 9),
         'ck': lambda c: c + 273.15,
         'kc': lambda k: k - 273.15,
         'fk': lambda f: (f + 459.67) * 5 / 9,
         'kf': lambda k: k * (9 / 5) - 459.67
         }
input1 = input('From which unit to convert into what: Select among cf, fc, ck, kc, fk, kf')
input2 = int(input('Value to convert: '))

print(temps[input1](input2))