# Data
letters_amazon = '''
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
'''

# One-Liner


def find(txt, q): return txt[txt.find(q)-18:txt.find(q)+18]
#find = lambda txt, q: txt[txt.find(q)-18:txt.find(q)+18]


# Result
print(find(letters_amazon, 'SQL'))
# a fully-managed MySQL and PostgreSQL
