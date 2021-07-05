def Ordered_binary_Search(olist, item):

    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist) // 2
        if olist[midpoint] == item:
            return True
        else:
            if item < olist[midpoint]:
                return binarySearch(olist[:midpoint], item)
            else:
                return binarySearch(olist[midpoint+1:], item)
