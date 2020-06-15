
import sys

if len(sys.argv) == 1:
    print("Provide at least one file name")
    quit()
for i in range(1, len(sys.argv)):
    f_name = sys.argv[i]
    try:
        inf = open(f_name, 'r')

        
        for line in inf:
            print(line)
        
        inf.close()
    except:
        
        print('Could not open', f_name)




