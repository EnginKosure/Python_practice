def dayOfProgrammer(year):
    if year == 1918:
        return '26.09.1918'
    elif 1700 <= year <= 1917:
        return f'13.09.{year}'*((year % 4) != 0)+f'12.09.{year}'*(year % 4 == 0)
    elif 1918 < year <= 2700:
        if ((year % 400) == 0 or ((year % 4) == 0 and (year % 100) != 0)):
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'


print(dayOfProgrammer(2003))
print(dayOfProgrammer(2004))
