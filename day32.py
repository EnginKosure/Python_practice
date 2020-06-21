# "Kullanıcıdan aldığınız *boy* ve *kilo* değerlerine göre kullanıcının beden kitle indeksini bulun.
# Vücut Kitle Endeksi Formülü= kilo/((boy(cm)/100)kare2)
height = float(input('How your height in cm: '))
weight = float(input('Enter your weight in kg: '))

bmi = weight/(height/100)**2
print('Your body mass index is {:.2f}'.format(bmi))

if bmi < 18.4:
    print('Zayif')
elif 18.5 < bmi < 24.9:
    print('Normal')
elif 25 < bmi < 29.9:
    print('Fazla kilolu')
elif 34 < bmi < 34.9:
    print('Obez')
elif 35 < bmi < 39.9:
    print('Morbid obez')
elif bmi >= 40:
    print('Super obez')
