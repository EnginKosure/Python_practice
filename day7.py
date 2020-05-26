# seconds to time

seconds_in_a_day = 60 * 60 * 24
seconds_per_hour = 60 * 60
seconds_per_minute = 60

if __name__ == '__main__':
    seconds = int(input('enter number of seconds: '))

    print(
        f'{(seconds / seconds_in_a_day)} days or {(seconds / seconds_per_hour)} hours or \
{(seconds / seconds_per_minute)} minutes')


# leap year
def is_leap_year(x):
    if x % 400 == 0:
        return True
    elif x % 100 == 0:
        return False
    elif x % 4 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    input1 = int(input('Enter year to check if it is a leap year: '))
    print(is_leap_year(input1))
