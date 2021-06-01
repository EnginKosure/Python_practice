
def error_printer(str):
    return f"{len(list(filter(lambda c:c>0,[1 if ord(i)>109 else 0 for i in str  ])))}/{len(str)}"


s = "aaabbbbhaijjjm"
print(error_printer(s))  # => "0/14"

s = "aaaxbbbbyyhwawiwjjjwwm"
print(error_printer(s))  # => "8/22"

# print(ord('m'))
