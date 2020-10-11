from subprocess import Popen, PIPE

######################################################################################################################
# TODO:                                                                                                              #
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                    #
# 2) CHANGE THE NAME 'MY_FILE_NAME.py' BELOW THIS BOX TO THE NAME OF YOUR PYTHON FILE                                #
# 3) RUN THIS FILE                                                                                                   #
######################################################################################################################

YOUR_SOLUTION_FILE_NAME = "Practicum.py"

######################################################################################################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE                                                                             #
######################################################################################################################


# parse the given output string
def parse_output(full_output_string):
    splitted = full_output_string.split(b'\n')
    uitvoer_string = str(splitted[0]).replace('\\r', '')
    try:
        uitvoer = int(uitvoer_string[2:-1])
    except:
        uitvoer = -1
    return uitvoer


# Run one test case with given input and output, return True when test succeeds, False when test fails
def run_one_test_case(inp, verwachte_uitvoer):
    process = Popen(["python", YOUR_SOLUTION_FILE_NAME],
                    stdin=PIPE, stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate(inp)
    if len(str(err)) > 3:
        print('Your program threw an ERROR')
        return False
    exit_code = process.wait()
    uitvoer = parse_output(output)
    if uitvoer == -1:
        print('Check your output format: print exactly one numeric value (no text)')
        return False
    return uitvoer == verwachte_uitvoer


# Retrieve a list containing all test_cases
def get_test_cases():
    all_test_cases = []
    # IN: 8 6 4 2 0 OUT: 120
    all_test_cases.append((b'8\n6\n4\n2\n0\n', 120))
    # IN: 6 4 -1 10 8 4 2 0 OUT: 184
    all_test_cases.append((b'6\n4\n-1\n10\n8\n4\n2\n0\n', 184))
    # IN: 4 3 2 1 0 OUT: 30
    all_test_cases.append((b'4\n3\n2\n1\n0\n', 30))
    # IN: 12 10 8 9 7 4 2 1 0 OUT: 151
    all_test_cases.append((b'12\n10\n8\n9\n7\n4\n2\n1\n0\n', 151))
    # IN: 12 15 -1 0 OUT: 0
    all_test_cases.append((b'12\n15\n-1\n0\n', 0))
    return all_test_cases


# Run all given test_cases
def run_test_cases(all_tests):
    for test_nb in range(len(all_tests)):
        (inp, outp) = all_tests[test_nb]
        test_result = run_one_test_case(inp, outp)
        if test_result:
            print('Test ' + str(test_nb + 1) + ': Succeeded')
        else:
            print('Test ' + str(test_nb + 1) + ': Failed')


# load all test cases and test them on given solution
all_tests = get_test_cases()
run_test_cases(all_tests)
