# Your computer might have been infected by a virus!
# Create a function that finds the viruses in files and removes them from your computer.

import re


def remove_virus(files):
    safe = [f for f in files[10:].split(", ") if f and not re.fullmatch(
        r"(?!not|anti).*(virus|malware)\.exe", f)]
    return "PC Files: %s" % (", ".join(safe) if safe else "Empty")


# "PC Files: spotifysetup.exe, dog.jpg"
remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")

# "PC Files: antivirus.exe, cat.pdf"
remove_virus(
    "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ")

remove_virus("PC Files: notvirus.exe, funnycat.gif")  # "PC Files: notvirus.


def remove_virus1(files):
    f = ', '.join([i for i in files[10:].replace(',', '').split(
    ) if 'anti' in i or 'not' in i or 'virus' not in i and 'malware' not in i])
    return 'PC Files: ' + f if f else 'PC Files: Empty'
