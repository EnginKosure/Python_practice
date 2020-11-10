# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix1(strs):
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        short = min(strs, key=len)
        result = ""
        index = 0
        while index < len(short):
            for i in range(len(strs)):
                if strs[i][index] != short[index]:
                    return result
            result += short[index]
            index += 1
        return result


strs = ["flower", "flow", "flight"]

print(longestCommonPrefix1(strs))


def longestCommonPrefix2(strs):
    result = ""
    index = 0
    try:
        short = min(strs, key=len)
        result = ""
        i = 0
        while i < len(short):
            for item in strs:
                if item[i] != short[i]:
                    return result
            result += short[i]
            i += 1
    except:
        return result
    return result
