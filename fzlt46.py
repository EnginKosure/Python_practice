waarde = int(input())
volume = 0
control_variable = waarde

while waarde != 0:
    if waarde > 0:
        control_variable = waarde
        volume += waarde**2
        waarde = int(input())
        # Burada if kontrolu buyuk sayiyi yakalayamiyordu, control_variable diye bir degisken olusturup
        # bir onceki degeri uzerine yazarak sakladik. Bu haliyle tum testleri geciyor.
        if waarde >= control_variable:
            volume = 0

        else:
            volume + (waarde**2)
    else:
        while waarde < 0:
            # Negatif sayi gelirse volume u sifirlamamiz gerekiyor
            volume = 0
            waarde = int(input())
            # BURADA GUNCELLEDIK!!!
            control_variable = waarde

print(volume)
