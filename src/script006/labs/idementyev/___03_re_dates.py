#!/usr/bin/env python3

"""
Switch month and day using re
"""

import re

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-11'

in_date = '2018-10-11T11:26:00'
groups = re.compile("(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})")
gr = groups.match(in_date)
print("I caught these:")
for i, group in enumerate(gr.groups()):
    print("{}:   {}".format(i, group))

print("\nIN:  {}".format(in_date))
print("OUT: {}-{}-{}T{}:{}:{}".format(gr[1],
                                      gr[3],
                                      gr[2],
                                      gr[4],
                                      gr[5],
                                      gr[6]))
