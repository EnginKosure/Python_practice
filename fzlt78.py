# Create a function that takes a list of any length.
# Modify each element(capitalize, reverse, hyphenate).
def edit_words(arr):
    x = [j[::-1] for j in [i.upper() for i in arr]]
    y = [i[:len(i)//2]+'-'+i[len(i)//2:] for i in x]
    # s[:4] + '-' + s[4:]

    print(y)


edit_words(["new york city"])  # ["YTIC KR-OY WEN"]

edit_words(["null", "undefined"])  # ["LL-UN", "DENIF-EDNU"]

# edit_words(["hello", "", "world"])  # ["OLL-EH", "-", "DLR-OW"]
