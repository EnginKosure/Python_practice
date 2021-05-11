# Given a string, return the expansion of that string.

# Input will consist of only lowercase letters and numbers (1 to 9) in valid parenthesis.
# There will be no letters or numbers after the last closing parenthesis.

def solve(st):
    st = st.replace("(", "").replace(")", "")
    result = ""
    m = len(st) - 1
    for i in range(m, -1, -1):
        if st[i].isalpha():
            result += st[i]
        elif st[i].isdigit():
            result *= int(st[i])
    return result[::-1]


solve("3(ab)")  # "ababab"      because "ab" repeats 3 times
# because "a3(b)" == "abbb", which repeats twice.
solve("2(a3(b))")  # "abbbabbb"

for i in range(6, -5, -2):
    print(i)


def solve1(st):
    res = ""
    for i in reversed(st):
        if i.isalpha():
            res += i
        if i.isdigit():
            res *= int(i)
    return res[::-1]
