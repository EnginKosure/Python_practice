# Task : Estimating the risk of death from coronavirus.
# Set a logical algorithm using boolean logic operators (and/or)
# and the given variables in order to give us True (there is a risk of death)
# or False (there is not a risk of death) as a result.

# Take the inputs from user. While not answered correctly, ask again.
control_variable = True
while control_variable:

    age = input(
        "Are you a cigarette addict older than 75 years old? ('y' or 'n'): ")

    chronic = input("Do you have a severe chronic disease? ('y' or 'n'): ")

    immune = input("Is your immune system too weak? ('y' or 'n'): ")

    if age.lower()[0] != 'y' and age.lower()[0] != 'n' or chronic.lower()[0] != 'y' and chronic.lower()[0] != 'n' or immune.lower()[0] != 'y' and immune.lower()[0] != 'n':
        print('You have entered irrelevant information!')
        print('Please only answer with "y" or "n"')
    else:
        control_variable = False


def covid_risk(a, c, i):
    # all yes answers
    if a.lower()[0] == 'y' and c.lower()[0] == 'y' and i.lower()[0] == 'y':
        print('You have a high death risk in case covid-19, stay home!')
        return True
    # in case one or two yes answers
    elif a.lower()[0] == 'y' or c.lower()[0] == 'y' or i.lower()[0] == 'y':
        print('Moderate risk. Keep the distance!')
    # all no answers
    else:
        print('You are safe from covid-19. But still, think the others and be cautious.')
        return False


# Call the function with the input variables
covid_risk(age, chronic, immune)
