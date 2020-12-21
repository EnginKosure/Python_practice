def actual_memory_size(s):
    x = int(s[:-2])*0.93
    if s[-2:] == 'MB':
        return str(int(x))+'MB'
    elif x < 1:
        return str(int(float(x)*1000))+'MB'
    else:
        return str(x)+'GB'


print(actual_memory_size('32GB'))  # 29.76GB
print(actual_memory_size('1GB'))  # 1.86GB
print(actual_memory_size('2GB'))  # 1.86GB
print(actual_memory_size('512MB'))  # 476MB
