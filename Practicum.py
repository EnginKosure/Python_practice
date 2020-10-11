waarde = int(input())
volume = 0
control_variable = waarde

while waarde != 0:
    if waarde > 0:
        control_variable = waarde
        volume += waarde**2
        waarde = int(input())
        if waarde >= control_variable:
            volume = 0

        else:
            volume + (waarde**2)
    else:
        while waarde < 0:

            volume = 0
            waarde = int(input())
            control_variable = waarde

print(volume)
