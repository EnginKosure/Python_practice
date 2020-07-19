# Data (daily stock prices ($))
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

# One-Liner
sample = [line[::2] for line in price]

# Result
print(sample)
# [[9.9, 9.8, 9.5],
#  [9.5, 9.4, 9.2],
#  [8.4, 7.9, 8.0],
#  [7.1, 4.8, 4.7]]


# Data
visitors = ['Firefox', 'corrupted',
            'Chrome', 'corrupted',
            'Safari', 'corrupted',
            'Safari', 'corrupted',
            'Chrome', 'corrupted',
            'Firefox', 'corrupted']

# One-Liner
visitors[1::2] = visitors[::2]

# Result
print(visitors)
# ['Firefox', 'Firefox',
#  'Chrome', 'Chrome',
#  'Safari', 'Safari',
#  'Safari', 'Safari',
#  'Chrome', 'Chrome',
#  'Firefox', 'Firefox']
