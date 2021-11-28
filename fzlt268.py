import time

for i in range(10):
    for i in range(4):
        time.sleep(0.5)
        print("\a")  # \a is reserved to warning notification sound in Windows
    time.sleep(3)
