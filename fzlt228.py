def even_or_odd(s):
    odds = sum([int(n) for n in s if int(n) % 2])
    evens = sum([int(n) for n in s if not int(n) % 2])
    if odds > evens:
        return "Odd is greater than Even"
    elif odds < evens:
        return "Even is greater than Odd"
    return "Even and Odd are the same"
