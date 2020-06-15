# Remove comments from a py file

# Read and open the input file. Ensure it is opened

try:
    input_file_name = input("Enter the name of the python file: ")
    inf = open(input_file_name, 'r')
except:
    print('Could not open the input file.')
    quit()

# Read and open output file. Ensure it is successfull.


# Read all lines from input file, remove comments.
# Save the lines to a new file.

# Find the position of the comment character.
# -1 if there is not any.

# If there is a comment, then form a slice of the string that excludes it.
# Overwrite the line.

# Write the modified line to the file

# Close the files
