def anagrams(word, words):
    # your code here
    # a_list = []
    # for i in words:
    #     if set(word) == set(i) and len(word) == len(i):
    #         a_list.append(i)
    # return a_list
    return [i for i in words if set(word) == set(i) and len(word) == len(i)]


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))  # ['aabb', 'bbaa']
