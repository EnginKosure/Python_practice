strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anag = {}
for i in strs:
    if "".join(sorted(i)) in anag:
        anag["".join(sorted(i))].append(i)
    else:
        anag["".join(sorted(i))] = [i]
print(list(anag.values()))


strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = []
for j in strings:
    item = [x for x in strings if sorted(j) == sorted(x)]
    if item not in result:
        result.append(item)
print(result)
