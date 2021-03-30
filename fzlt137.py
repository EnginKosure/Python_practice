
# Sum Over Every Other Value Python One-Liner
sum(stock_prices[::2])

# Read File Python One-Liner
[line.strip() for line in open(filename)]

# Quicksort Python One-liner
lambda L: [] if L == [] else qsort(
    [x for x in L[1:] if x < L[0]]) + L[0:1] + qsort([x for x in L[1:] if x >= L[0]])
