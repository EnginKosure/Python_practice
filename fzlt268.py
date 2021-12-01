import time

# for i in range(10):
#     for i in range(4):
#         time.sleep(0.5)
#         print("\a")  # \a is reserved to warning notification sound in Windows
#     time.sleep(3)


lst = "10, 50, 100, 500, 1000, 5000"
for i in lst:
    if i == str(0):
        print(i, end="|")


ten_billion = 10_000_000_000

print(f'{ten_billion:,}')
# 10, 000, 000, 000
