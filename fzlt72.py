# Given a text file file.txt that contains list of phone numbers(one per line),
# write a one liner bash script to print all valid phone numbers.
# You may assume that a valid phone number must appear in one of the following two formats:
# (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)
# You may also assume each line in the text file must not contain leading or trailing white spaces.
# Example:
# Assume that file.txt has the following content:
# 987-123-4567
# 123 456 7890
# (123) 456-7890
# Your script should output the following valid phone numbers:
# 987-123-4567
# (123) 456-7890


import pandas as pd
import numpy as np
import re
# (123) 456-7890
wanted_format_1 = "^[(]{1}[0-9]{3}[)]{1}[\s]{1}[0-9]{3}[-]{1}[0-9]{4}$"
wanted_format_2 = "^[0-9]{3}[-]{1}[0-9]{3}[-]{1}[0-9]{4}$"  # 987-123-4567
with open("phonenumbers.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for ind, line in enumerate(lines):
        number = line if ind == len(lines)-1 else line[:-1]
        ok_1 = re.search(wanted_format_1, number)
        ok_2 = re.search(wanted_format_2, number)
        if ok_1 or ok_2:
            print(number)


for i in filter(lambda x: x is not np.nan, [x if "-" in x else np.nan for x in list(
    pd.read_csv("deneme.TXT", sep="\n", header=None)[0])]): print(i)
