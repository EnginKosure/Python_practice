def actual_memory_size(s):
    x = int(s[:-2])*0.93
    if s[-2:] == 'MB':
        print(str(int(x))+'MB')
    else:
        print(str(x)+'GB')


actual_memory_size('32GB')  # 29.76GB

actual_memory_size('2GB')  # 1.86GB

actual_memory_size('512MB')  # 476MB
