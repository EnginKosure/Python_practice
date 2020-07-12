# Create employees dictionary of salaries
dic = {'Alice': 100000,
       'Bob': 99817,
       'Carol': 122908,
       'Frank': 88123,
       'Eve': 93121}

# What are the top earners earning over
# $100k per month?
res = [(k, v) for k, v in dic.items() if v > 99999]

# Print everything
print(res)
# [('Alice', 100000), ('Carol', 122908)]
