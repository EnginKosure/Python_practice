def sumOfTwo(a, b, v):
    lenA = len(a)
    lenB = len(b)
    for itemA in a:
        for i in range(lenB):
            currentNumberB = b[i]
            if v - itemA == currentNumberB:
                print("True")
                exit()
            else:
                if a.index(itemA) == lenA:
                    print("False")
                    exit()


sumOfTwo([1, 2, 3], [10, 20, 30], 23)
