
def error_printer(str):
    return f"{sum(i>'m' for i in str)}/{len(str)}"


def printer_error(s):
    return '{}/{}'.format(sum(color > 'm' for color in s), len(s))


s = "aaabbbbhaijjjm"
print(error_printer(s))  # => "0/14"

s = "aaaxbbbbyyhwawiwjjjwwm"
print(error_printer(s))  # => "8/22"

# print(ord('m'))
