# seconds to time

seconds_in_a_day = 60 * 60 * 24
seconds_per_hour = 60 * 60
seconds_per_minute = 60

if __name__ == '__main__':
    seconds = int(input('enter number of seconds: '))

    print(
        f'{(seconds / seconds_in_a_day)} days or {(seconds / seconds_per_hour)} hours or \
{(seconds / seconds_per_minute)} minutes')
