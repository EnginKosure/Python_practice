import json
# import datetime
from collections import Counter

month = []
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Ada Byron Lovelace": "12/10/1815",
    "Benjamin Franklin": "01/17/1706"
}

for x in birthdays.values():
    month.append(x.split()[0].split('/')[0])

print(Counter(month))
