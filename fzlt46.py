waarde = int(input("Geef een getal: "))
volume = 0
control_variable = waarde

while waarde != 0:
    if waarde > 0:
        control_variable = waarde
        volume += waarde**2
        waarde = int(input("Geef een getal: "))
        # Burada if kontrolu buyuk sayiyi yakalayamiyordu, control_variable diye bir degisken olusturup
        # bir onceki degeri uzerine yazarak sakladik. Bu haliyle tum testleri geciyor.
        if waarde >= control_variable:
            volume = 0

        else:
            volume + (waarde**2)
            print(volume)
    else:
        while waarde < 0:
            # Negatif sayi gelirse volume u sifirlamamiz gerekiyor
            volume = 0
            waarde = int(input("Geef een getal: "))
print("De volume van de piramide is", volume)
