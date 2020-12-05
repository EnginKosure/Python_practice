# parallel or not
def are_parallel_lines(l1, l2):
    if(l1[1] != 0 and l2[1] != 0):
        if(l1[0]/l1[1] == l2[0]/l2[1]):
            return True
        else:
            return False
    else:
        if(l1[0] == l2[0] and l1[1] == l2[1]):
            return True
        else:
            return False
