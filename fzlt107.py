# 0 to 32 days	Zero
# 33 to 40 days	SGD$325 per billable day
# 41 to 48 days	SGD$550 per billable day
# Greater than 48 days	SGD$600 per billable day

def bonus(x):
    if x < 32:
        return 0
    elif x < 40:
        return (x-32)*325
    elif x < 48:
        return (x-40)*550
    else:
        return (x-48)*600 + (x-40)*550


print(bonus(15))  # 0

print(bonus(37))  # 1625

print(bonus(50))  # 8200
