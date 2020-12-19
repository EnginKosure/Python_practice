import re


def remove_virus(s):
    # print(s.split())
    a = s.split()
    pattern1 = '\**virus*'
    pattern2 = '\**malware*'
    for i in a:
        if re.search(pattern1, i) or re.search(pattern2, i):
            print(a.index(i))
            del a[a.index(i)]

    print(a)
    return a

    # "PC Files: spotifysetup.exe, dog.jpg"
remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")

# "PC Files: antivirus.exe, cat.pdf"
remove_virus(
    "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")

# "PC Files: notvirus.exe, funnycat.gif")
remove_virus("PC Files: notvirus.exe, funnycat.gif")

# Bad files will contain "virus" or "malware", but "antivirus"
# and "notvirus" will not be viruses.
# Return "PC Files: Empty" if there are no files left on the computer.
