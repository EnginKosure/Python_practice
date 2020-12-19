

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
