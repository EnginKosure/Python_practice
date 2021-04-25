# The goal of this challenge is to analyze a binary string consisting of only zeros and ones.
# Your code should find the biggest number of consecutive zeros in the string. For example,
# given the string:"1001101000110"
# The biggest number of consecutive zeros is 3.
def consecutive(s):
    # print(max([len(i) for i in s.split("1")]))
    return max([len(i) for i in s.split("1")])


t = "1001101000110"

consecutive(t)
