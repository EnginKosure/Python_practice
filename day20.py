import sys
# Display the first 10 lines of a file whose name is provided as a command line parameter
num_lines = 10
# Verify that only one command line parameter (in addition to the .py file) was supplied.

if len(sys.argv) != 2:
    print('Please provide the file name as a command line parameter.')
    quit()  # When quit func. called, the program ends immediately.

try:
    # Open the file for reading.
    inf = open(sys.argv[1], 'r')
    # read the first line from the file
    line = inf.readline()

    # Keep looping until 10 or eof
    count = 0
    while count < num_lines and line != '':
        # Remove the trailing newline char and count the line
        line = line.rstrip()
        count += 1

        # display the line
        print(line)

        # read the next line
        line = inf.readline()
    # close the file
    inf.close()
except IOError:
    # Display a message if sth goes wrong while accessing the file
    print("IOError-could not access the file")

# From terminal, execute like below
# python day20.py trial.py
# this code will read inside of the file which is provided as a second argument.
