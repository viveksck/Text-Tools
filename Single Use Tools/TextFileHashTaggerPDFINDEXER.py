#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.com

#takes a text file with a list of references, one perline, and creates a text file for each one prepped for hashtagindexer

from os import rename, listdir
import string
filenames = listdir('.')
goodchar = "-_.() %s%s" % (string.ascii_letters, string.digits)


for filename in filenames:
	if filename.endswith(".pdf"):
		goodfilename = ''.join(c for c in filename if c in goodchar)
		goodfilename = goodfilename[:250]
		rename(filename, goodfilename)
		textfilename = goodfilename[:-4]
		newfile=open(textfilename+".txt", "w")
		newfile.write(textfilename)
		newfile.write("\n")
		newfile.write("#ref #stereothreat")
		newfile.close()
