# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of
# the squares of its digits, and repeat the process until
# the number equals 1 (where it will stay), or it loops endlessly in a cycle
# which does not include 1. Those numbers for which this process
# ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.

def happy(n):
    answer = []
    while n != 1:
        summ = 0
        for i in str(n):
            summ += int(i)**2
        if summ in answer:
            return False
        else:
            print('sum', summ)
            answer.append(summ)
        n = summ
    return True


print(happy(20))  # False
print(happy(19))  # True


def isHappy(self, n):
    checked = []
    nums = str(n)
    while nums != '1' and not (nums in checked):
        checked.append(nums)
        result = 0
        for num in nums:
            result += int(num) * int(num)
        nums = str(result)
    if (nums == '1'):
        print("True")
    else:
        print("False")
