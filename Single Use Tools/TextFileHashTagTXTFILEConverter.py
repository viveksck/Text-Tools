#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.com

#takes a text file with a list of references, one perline, and creates a text file for each one prepped for hashtagindexer

import string
titlelist = open("titles.txt")
goodchar = "-_.() %s%s" % (string.ascii_letters, string.digits)

for line in titlelist:
	print line
	filename = ''.join(c for c in line if c in goodchar)
	filename = filename[:250]
	newfile=open(filename+".txt", "w")
	newfile.write(line)
	newfile.write("\n")
	newfile.write("#ref #stereothreat")
	newfile.close()