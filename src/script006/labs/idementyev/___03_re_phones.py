#!/usr/bin/env python3

"""
Find out which phones are russian from file
"""

import re

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-11'

phones_file = "___03_re_phones_list.txt"
digit_re = re.compile("\d")


def russian_code(number: str) -> bool:
    if number.startswith("9"):
        return True
    return False


valid = []

with open(phones_file, 'r') as in_f:
    lines = in_f.readlines()
    for line in lines:
        line = line.strip()
        digits = "".join(re.findall(digit_re, line))
        length = len(digits)

        if 10 <= length <= 11:
            # number of digits is valid
            if length == 11:
                # has prefix
                if line.startswith("+7") or line.startswith("8"):
                    # found +7 or 8, truncating first digit
                    digits = digits[1:]

            if russian_code(digits):
                valid.append(digits)

print(valid)
