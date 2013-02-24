#!/usr/bin/env python
#Malcolm Prentice - malc@alba-english.com

'''
  This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

THANKS TO:
Various snippets of code came from stackoverflow (http://stackoverflow.com/), the NLTK manual and website (http://www.nltk.org/)
Thanks to Charles Kelly (http://aitech.ac.jp/~ckelly) for help with the 2009 version (tab-separated files, the word length bug and added the file naming/timing).

NOTES
The script strips out the POS tags and combines all types irrespective of POS.
New version produces vaguely alphabetised lists (a is scrambled, but comes before b)
	Python is less efficient than unix commands at sorting large lists. 
	SO Use unix "sort" on the final output file to alphabetise it or order it by frequency
	
NOTES ON POS AND TAGS
There are tags for:	 
	_num 	numeral
	_adj 	adjective
	_adp 	adposition(prepositionor postposition)
	_prt 	particle
	_adv 	adverb
	_det 	determiner or article
	_pron 	pronoun
	_verb 	verb
	_conj 	conjunction
	_noun	noun

THese are stripped - they aren't very good (since when is appendicitis _det? 
There are also parsing tags for sentence which are removed
	_start	
	_end
	_root
	
There is also an "_x" tag which seems to mark foreign words.
	Words tagged with this are not included in final list, but note that many foreign words are untagged									

SYSTEM REQUIREMENTS
The dataset itself is about 25GB
On a i7 MacAir with 8GB memory and an SSD, using the eng-all-1gram dataset from 2012, with a 1994 earliest year and a 1000 occurence threshhold
	The script took about 2 mins per GB (i.e. 4 mins for the 1.8GB, 54mins 30s for the whole dataset
	Memory requirements are under control in this alphabetised version - the thread does not use more than 100MB
	

Your mileage may vary - a 0 threshold with a 1900 earliest year will perform very differently
'''


import os
import time

#Set earliest year and lowest occurence rate you want to be included
earliestyear = 1994
yourthreshold = 1000

#We're using "more than", so minus one from year and from threshold
pythonearliestyear = earliestyear-1
threshold=yourthreshold-1


# CK added time
localtime = time.asctime( time.localtime(time.time()) )
print "\n==== "
print "Start Time: ", localtime
print "Earliest Year: ", pythonearliestyear
print "Threshold: ", yourthreshold
print "====\n"

path=os.getcwd()
filelist=os.listdir(path)   
outputfilename=str(earliestyear)+"THRESHOLD"+str(threshold)+".txt"

def filter():
	outputfile=open(outputfilename, 'w')
	outputfile.write("")
	outputfile.close()
	outputfile=open(outputfilename, 'a')
	path=os.getcwd()
	filelist=os.listdir(path)  
	for filename in filelist:
			if filename.startswith("googlebooks"):
					print filename
					filedictionary= dict()
					for line in open(filename):
							column = line.split("\t")
							if len(column) > 1:
									year = column[1]
									if year.isdigit() and int(year) > pythonearliestyear:
											ngram = column[0]
											value = str(column[2])
											key = ngram.lower()
											if key.endswith('_det') or key.endswith('_num') or key.endswith('_adj') or key.endswith('_adp') or key.endswith('_prt') or key.endswith('_adv'):
												key=key[:-4]
											if key.endswith('_pron') or key.endswith('_verb') or key.endswith('_conj') or key.endswith('_noun'):
												key=key[:-5]
											if key.endswith('_start'): 
												key=key[:-6]
											if key.endswith('_end'):
												key=key[:-4]
											if key.endswith('_root'):
												key=key[:-5] 
											if key not in filedictionary:
													filedictionary[key] = value
											else:
													filedictionary[key] = (int(filedictionary[key]) + int(value))
					for key in filedictionary:
						if filedictionary[key] > threshold and not key.endswith("_x"):
							outputfile.write(str(key))
							outputfile.write("\t")
							outputfile.write(str(filedictionary[key]))
							outputfile.write("\n")
                            

if outputfilename in filelist:
        print "You already ran that request with the data in this folder - the results are here:" 
        print outputfilename
        print "If the run did not complete, delete the output file before trying again"
else:
	filter()				
	localtime2 = time.asctime( time.localtime(time.time()) )
	print "\n==== "
	print "====  Start Time: ", localtime
	print "====    End Time: ", localtime2
	print "====\n"