#!/usr/bin/env python3

"""
Ping Google, print packets and TTL.
Also mask IP addresses.
"""

import re
import os
import subprocess

__version__ = '0.0.1'
__author__ = 'Ilya R. Dementyev'
__date__ = '2018-10-11'

hostname = "google.com"
command = "ping"
args = {'win': ['-w', '1000', '-n', '10'],
        'nix': ['-W', '1', '-c', '10']}

# use the correct args
# type change: now args is a list
if os.name == 'nt':
    args = args['win']
else:
    args = args['nix']

p = subprocess.Popen((command, *args, hostname), stdout=subprocess.PIPE)
result = p.communicate()[0]

packets_str = "Packets: Sent = (\d+), Received = (\d+), Lost = (\d+) "
packets_re = re.compile(packets_str)
packets = packets_re.search(result.decode())
print("Packets:\nsent: {}\nreceived: {}\nlost: {}".format(packets[1],
                                                          packets[2],
                                                          packets[3]))

ttl_str = "TTL=(\d+)"
ttl_re = re.compile(ttl_str)
ttl = ttl_re.findall(result.decode())

print("\nTTL:\nmin: {}\nmax: {}".format(min(ttl),
                                        max(ttl)))

mask_str = "\d+\.\d+\.\d+\.\d+"
mask_re = re.compile(mask_str)
out_result = re.sub(mask_re, "x.x.x.x", result.decode())
print("\nVerbose output below:\n{}\n{}".format("-" * 32, out_result.strip()))
