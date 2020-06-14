# Concatenate Multiple Files
import sys

if len(sys.argv) == 1:
    print("Provide at least one file name")
    quit()
for i in range(1, len(sys.argv)):
    f_name = sys.argv[i]
    try:
        inf = open(f_name, 'r')

        # Display the file
        for line in inf:
            print(line)
        # close the file
        inf.close()
    except:
        # Display a message but don't quit.
        print('Could not open', f_name)

# From terminal, execute like below
# python day23.py trial.py day22.py day19.py
# this code will read inside of the file which is provided as arguments.
