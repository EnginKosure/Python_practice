# Problem : If you had deposited a coin on the cryptocurrency exchange
# that brought 7% fixed profit daily for a week,
# how much would your $ 1000 reach at the end of the 7th day?

x = 1000
for i in range(7):
    x *= 1.07
print("$ %.2f" % x)  # $ 1605.78
