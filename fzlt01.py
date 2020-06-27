# def ascending(txt):
#     for i in range(1, len(txt)):
#         numbers = int(txt[:i])
#         new_numbers = str(numbers)
#         if len(txt) % len(new_numbers):
#             continue
#         while len(new_numbers) < len(txt):
#             numbers += 1
#             new_numbers += str(numbers)
#             if new_numbers == txt:
#                 return True
#                 break
#     return False


# print(ascending("57585960616263"))  # True
# print(ascending('123412351236'))  # True
# print(ascending('444445'))  # True
# print(ascending('2324256'))  # False
# print(ascending('35236237238'))  # False
# print(ascending('1235'))  # False

# them.Test.assert_equals(ascending("232425"), True)
# Test.assert_equals(ascending("444445"), True)
# Test.assert_equals(ascending("1234567"), True)
# Test.assert_equals(ascending("123412351236"), True)
# Test.assert_equals(ascending("57585960616263"), True)
# Test.assert_equals(ascending("500001500002500003"), True)
# Test.assert_equals(ascending("919920921"), True)
# Test.assert_equals(ascending("2324256"), False)
# Test.assert_equals(ascending("1235"), False)
# Test.assert_equals(ascending("121316"), False)
# Test.assert_equals(ascending("12131213"), False)
# Test.assert_equals(ascending("54321"), False)
# Test.assert_equals(ascending("56555453"), False)
# Test.assert_equals(ascending("90090190290"), False)
# Test.assert_equals(ascending("35236237238"), False)

import time
b = time.time()
txt = "500001500002500003"
print(len(txt))  # 18
durum = False
for i in range(1, len(txt)):
    sayilar = int(txt[:i])
    print(sayilar)
    new_sayilar = str(sayilar)
    print(len(new_sayilar))
    print(len(txt) % len(new_sayilar))
    if len(txt) % len(new_sayilar):
        continue
    while len(new_sayilar) < len(txt):
        sayilar += 1
        new_sayilar += str(sayilar)
    print(new_sayilar)
    if new_sayilar == txt:
        durum = True
        break
print(f"döngü bitti {round(time.time() - b, 8)} saniyede  getirdik.")
