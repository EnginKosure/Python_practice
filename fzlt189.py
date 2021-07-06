def close_compare(a, b, margin=0):
    if margin >= abs(a - b) or a == b:
        return 0
    elif a < b:
        return -1
    return 1
