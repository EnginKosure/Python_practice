# A function to read the content of a text file and store it in a list
def readTextFile(filename):
    list = []
    file = open(filename, "r")
    for value in file:
        # strip out all tailing whitespace and carriage returns
        list.append(value.rstrip('\r\n'))
    file.close()
    return list


# Main Program Starts Here
pupils = readTextFile("rewards.txt")
print(pupils)
