# Problem : If you had deposited a coin on the cryptocurrency exchange
# that brought 7% fixed profit daily for a week,
# how much would your $ 1000 reach at the end of the 7th day?

# x = 1000
# for i in range(7):
#     x *= 1.07
#     print(i, x)
# print("$ %.2f" % x)  # $ 1605.78


# Interest=p*r*t
p = 1000
r = 0.07
t = 7
interest = p*r*t
total_money = p+interest

print(total_money)


#A = P (1 + r) **(t)
A = p*(1+r)**t
print(A)
c = 1000*1.07**7
print(c)
