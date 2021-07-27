# Iterating through a string
h_letters = [letter for letter in 'human']
h_letters
['h', 'u', 'm', 'a', 'n']

# if with List Comprehension
even_list = [x for x in range(20) if x % 2 == 0]
even_list
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# if...else With List Comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
obj
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
