from time import time
start_time = time()


def QuestionsMarks(s):
    qnum = 0
    dig = 0
    has_10 = False
    for ch in s:
        if ch.isdigit():
            if int(ch) + dig == 10:
                if qnum != 3:
                    return 'false'
                has_10 = True
            dig = int(ch)
            qnum = 0
        elif ch == '?':
            qnum += 1
    return 'true' if has_10 else 'false'


# print(QuestionsMarks("arrb6???4xxbl5???eee5"))  # => true
print(QuestionsMarks("acc?7??sss?3rr1??????5"))  # => true
# print(QuestionsMarks("5??aaaaaaaaaaaaaaaaaaa?5?5"))  # => false
# QuestionsMarks("9???1???9???1???9")  # => true
# QuestionsMarks("aa6?9")  # => false

print(f'---Time: {time()-start_time} seconds')
