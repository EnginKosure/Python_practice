from time import time
for i in range(10):
    print(' '*(10-i)+str(i)*(2*i+1))
    print((2*i+1))


def is_prime(num):
    # num = int(input("enter a number : "))

    if num <= 1:
        print(f"{num} is NOT a prime number")

    elif num % 2 == 0 and num != 2:
        print(f"{num} is NOT a prime number")

    else:
        for i in range(3, int(num**0.5)+1, 2):
            if num % i == 0:
                print(f"{num} is NOT a prime number")
                break
        else:
            print(f"{num} is a prime number")


start = time()
for i in range(1000):
    is_prime(i)
print(f'TIME{time()-start}')
