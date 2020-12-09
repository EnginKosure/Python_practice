# Create a function that takes a list of any length.
# Modify each element(capitalize, reverse, hyphenate).
def edit_words(arr):
    x = [j[::-1] for j in [i.upper() for i in arr]]
    y = [i[:len(i)//2]+'-'+i[len(i)//2:] if len(i) %
         2 == 0 else i[:len(i)//2+1]+'-'+i[len(i)//2+1:] for i in x]

    print(y)


def edit_words1(lst):
    return [''.join(reversed(x.upper()[0:len(x)//2] + '-' + x.upper()[len(x)//2:])) for x in lst]


edit_words(["new york city"])  # ["YTIC KR-OY WEN"]

edit_words(["null", "undefined"])  # ["LL-UN", "DENIF-EDNU"]

edit_words(["hello", "", "world"])  # ["OLL-EH", "-", "DLR-OW"]
