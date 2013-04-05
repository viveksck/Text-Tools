#!/usr/bin/env python
#Malcolm Prentice - malc@alba-english.com

import os
count = 0
for line in open("FINAL RESULTS SINCE1994THRESHOLD0.txt"):
    column = line.split("\t")
    if len(column) > 1:
        count=count + int(column[1])

print count