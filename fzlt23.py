# def missing_char(word, n):
#     new_word = ''
#     for i in range(len(word)):
#         if i != n:
#             new_word += word[i]
#     print(new_word)
#     return new_word


# missing_char('fazilet', 1)
# missing_char('serra', 2)
# Bu da for loop lu cozum
def make_box(n):
    lst = []
    for i in range(n):
        if i == 0 or i == n-1:
            lst.append('#'*n)
        else:
            lst.append('#'+' '*(n-2)+'#')
    return lst


make_box(5)


def box(n):
    x = ['\"'+n*"#"+'\",' if x == 0 or x == n -
         1 else '\"#'+(n-2)*" "+'#\",' for x in range(n)]
    for i in range(n):
        print(x[i])
