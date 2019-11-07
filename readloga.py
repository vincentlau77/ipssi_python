#!/usr/bin/python3

import os
apath = os.path.expanduser("~/a.log")
print("chemin etendu en", apath)
with open(apath) as fd:
    for line in fd:
       print(line)
       break

