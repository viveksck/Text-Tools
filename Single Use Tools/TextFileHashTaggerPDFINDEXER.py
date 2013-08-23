#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org

#takes a folder full of PDF, and creates a text file for each prepped for hashtagindexer
#cleans filenames while its at it
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
		newfile.write("#ref #pending")
		newfile.close()
