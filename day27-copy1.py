# Task : Estimating the risk of death from coronavirus.
# Set a logical algorithm using boolean logic operators (and/or)
# and the given variables in order to give us True (there is a risk of death)
# or False (there is not a risk of death) as a result.

# Take the inputs from user. While not answered correctly, ask again.
# case one
age, chronic, immune = True, True, True

print(age and chronic and immune)  # True

# case two

age, chronic, immune = False, True, False

print(age and chronic and immune)  # False

# case three

age, chronic, immune = False, True, True

print(age and chronic and immune)  # False
