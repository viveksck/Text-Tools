#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org



import os

file= "FINAL TOP output.txt"
output= open(file, 'w')
for line in open("FINAL RESULTS SINCE1994THRESHOLD0.txt"):
    column = line.split("\t")
    if len(column) > 1:
        if int(column[1]) > 1000000:
            print line
            output.write(line)

