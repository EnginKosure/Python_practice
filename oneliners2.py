# How to read a file in Python
filename = "oneliners1.py"  # this code


f = open(filename)
lines = []

for line in f:
    lines.append(line.strip())

print(lines)

# ONELINER
print([l.strip() for l in open("002e6.js")])
