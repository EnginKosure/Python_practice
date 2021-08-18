from string import ascii_lowercase


def even_or_odd(s):
    odds = sum([int(n) for n in s if int(n) % 2])
    evens = sum([int(n) for n in s if not int(n) % 2])
    if odds > evens:
        return "Odd is greater than Even"
    elif odds < evens:
        return "Even is greater than Odd"
    return "Even and Odd are the same"


def decode(r):
    num = int("".join([c for c in r if c.isdigit()]))
    coded = r.strip(str(num))
    alfabet = ascii_lowercase
    decoded = ""
    for c in coded:
        index = ""
        for i in range(26):
            if i * num % 26 == alfabet.index(c):
                if index != "":
                    return "Impossible to decode"
                index = i
                decoded += alfabet[i]
    return decoded
