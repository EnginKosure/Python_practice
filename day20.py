import sys
# Display the first 10 lines of a file whose name is provided as a command line parameter
num_lines = 10
# Verify that only one command line parameter (in addition to the .py file) was supplied.

if len(sys.argv) != 2:
    print('Please provide the file name as a command line parameter.')
    quit()
