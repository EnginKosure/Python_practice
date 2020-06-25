# print(not 0 and "write me")


# tutar = float(input("Lutfen alışveriş tutarını girin"))
# verien_para = float(input("Lütfen verilen miktarı girin"))
# if verien_para < tutar:
#     print("Daha fazla para vermelisin")
# para_ustu = verien_para - tutar
# paralar = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
# adet, bol = 0, 0
# for i in paralar:
#     bol = para_ustu//i
#     if(bol != 0):
#         adet += bol
#         print(f"{i} euro dan  {bol} tane")
#     para_ustu = round(para_ustu % i, 2)
#     # print(para_ustu)
# print(f"Toplam {adet} tane para ve { verien_para - tutar} euro vermelisin")
from time import time
start_time = time()
money = float(input('Please enter your money: '))
payment = float(input('Please enter your payment: '))
repayment = money-payment
print(f'Your change is {repayment}')
A = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
i, B = 0, {}
while repayment > 0 and i != len(A):
    k = int(repayment//A[i])
    repayment = repayment-k*A[i]
    if k != 0:
        print(f'{k} adet {A[i]} Euro')
    i = i+1
print(f'---AAA {time()-start_time} seconds')
start_time = time()


def money_exchange(amount, d=[500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5,
                              0.2, 0.1, 0.05, 0.02, 0.01]):
    print(f'Total returned money: {amount}')
    i = 0
    used = {}  # start with an empty dictionary
    while (amount > 0) and i < len(d):  # go until all money gone
        num = amount // d[i]
        used[d[i]] = num
        amount -= num * d[i]
        i += 1
    for i in used:
        if used[i] > 0:
            print(f'{int(used[i])} times {i} banknotes')
    return used


money = float(input('Please enter your money: '))
payment = float(input('Please enter your payment: '))
change = money-payment
money_exchange(change)
print(f'---BBB {time()-start_time} seconds')
