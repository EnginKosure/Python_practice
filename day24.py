# Remove comments from a py file

# Read and open the input file. Ensure it is opened

try:
    input_file_name = input("Enter the name of the python file: ")
    in_f = open(input_file_name, 'r')
except:
    print('Could not open the input file.')
    quit()

# Read and open output file. Ensure it is successfull.
try:
    output_file_name = input("Enter the name of the output file: ")
    out_f = open(output_file_name, 'w')
except:
    print('Error opening the output file.')
    quit()

# Read all lines from input file, remove comments.
# Save the lines to a new file.
try:
    for line in in_f:

        # Find the position of the comment character.
        # -1 if there is not any.
        pos = line.find('#')

        # If there is a comment, then form a slice of the string that excludes it.
        # Overwrite the line.
        if pos > -1:
            line = line[0:pos]
            line = line+'\n'
        # Write the modified line to the file
        out_f.write(line)
        # Close the files
    in_f.close()
    out_f.close()
except:
    print('Error')
