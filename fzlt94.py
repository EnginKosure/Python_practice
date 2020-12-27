strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
anag = {}
for i in strs:
    if "".join(sorted(i)) in anag:
        anag["".join(sorted(i))].append(i)
    else:
        anag["".join(sorted(i))] = [i]
print(list(anag.values()))
