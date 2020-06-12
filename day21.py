# to read end of file which is provided as a command line argument,
# This exercise is an extension to the ex. in day20.py file

import sys

num_lines = 10

if len(sys.argv) != 2:
    print('provide filename from command line')
    quit()
try:
    inp1 = open(sys.argv[1], 'r')

    lines = []
    for line in inp1:
        lines.append(line)

        if len(lines) > num_lines:
            lines.pop(0)
    inp1.close()

except:
    print('an error occurred while processing the file')
    quit()

for line in lines:
    print(line)
