from time import time

start_time = time()

control_string = 'aeiou'


def find_vocals(s):

    result = ''

    for character in s:
        if character in control_string:
            result += character
    # to avoid the repeatings
    return ''.join(set(result))


print(find_vocals('Merhaba arkadaslarim'))
print(f"--- AAA {time() - start_time} seconds ---")

start_time = time()


def vowels(s):
    vowel = 'aeiou'
    finded = ''
    for i in s:
        if i in vowel:
            if not i in finded:
                finded += i
            # else:
            #     continue
        # else:
        #     continue
    return finded


print(vowels('Merhaba arkadaslarim'))
print(f'--- BBB {time() - start_time} seconds ---')

start_time = time()


def vowels1(s):
    vowels = 'aeiou'
    x = ''
    return ''.join(set([letter for letter in s if letter in vowels]))


print(vowels1('Merhaba arkadaslarim'))
print(f'---CCC {time() - start_time} seconds')


# 3 ve 5 arasında şu şekilde bir kurala uyan bir kontrol kodu yazın
# 5  toplarken kullanılacak,
# 3 çarparken
# Hedef sayıya yani n sayısına bu şekilde ulaşılıyor mu onu kontrol edeceksiniz
# Örnek
# n = 14 ➞ True
# 14 = 3*3 + 5
# n = 25 ➞ True
# 25 = 5+5+5+5+5
# n = 7 ➞ False
# There exists no path to the target number 7
# n = 378 -> True
# Burada şuna dikkat 3 ile herhangi bir çarpımından geriye kalan 5  ile toplanabilmesi lazım


def control(num):
    if num % 5 == 0:
        return True
    elif num % 3 == 0 or num % 3 == 5 or num % 3 == 10:
        return True
    else:
        return False


print(control(382))
