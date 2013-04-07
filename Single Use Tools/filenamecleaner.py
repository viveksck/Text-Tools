#Malc Prentice
#cleans filenames
from os import rename, listdir
import string
filenames = listdir('.')
goodchar = "-_.() %s%s" % (string.ascii_letters, string.digits)

for filename in filenames:
	goodfilename = ''.join(c for c in filename if c in goodchar)
	rename(filename, goodfilename)