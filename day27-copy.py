
age = input("Are you a cigarette addict older than 75 years old? ('y' or 'n'): ")
chronic = input("Do you have a severe chronic disease? ('y' or 'n'): ")
immune = input("Is your immune system too weak? ('y' or 'n'): ")

if age == 'y' and chronic == 'y' and immune == 'y':
    print('High risk')
else:
    print('No risk')
