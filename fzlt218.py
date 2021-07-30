import re

# Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("YES! We have a match!")
else:
    print("No match")

y = re.findall("ai", txt)
print(y)  # ['ai', 'ai']

z = re.findall("Portugal", txt)
print(z)  # []


t = re.search("\s", txt)

print("The first white-space character is located in position:", t.start())
