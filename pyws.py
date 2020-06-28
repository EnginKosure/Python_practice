B = 131
A = str(B)
left, right, contrl = [], [], ''


def prime(num):
    K = sum([1 for j in range(2, int(num**(1/2))+1) if num % j == 0])
    if K == 0:
        return True
    else:
        return False


if '0' in A:
    print('False')
else:
    for i in range(len(str(A))):
        if prime(int(A[0:i+1])) == False or int(A[0:i+1]) == 1:
            break
    else:
        contrl += 'right'
    for i in range(1, len(str(A))+1):
        if prime(int(A[-i:])) == False or int(A[-i:]) == 1:
            break
    else:
        contrl += 'left'
    print('both' * (len(contrl) > 5) or 'False' * (len(contrl) == 0) or 'left' * (len(contrl) == 4) or 'right' * (len(contrl)
                                                                                                                  == 5))
