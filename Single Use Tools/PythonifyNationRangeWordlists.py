#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org


#Turns a folder of Paul Nation's word lists for RANGE (organised by tab with numbers) into lines, with headword at beginning, so easier to process for families. Used once to prepapre lists for other programs. 
#source for lists -  http://www.victoria.ac.nz/lals/about/staff/paul-nation

import os, re, string

path = os.getcwd()

filelist=os.listdir(path)

for filename in filelist:
	if filename.endswith("txt"):
			infilepath=path+"/"+filename
			file = open(infilepath, 'r')	
			data=file.read()
			outfilepath=path+"/"+"DONE"+filename
			f = open(outfilepath, 'a')
			p=re.compile("\n")
			lines=p.split(data)
			for line in lines:
				if len(line)<2:
					 print "empty line skipped"
				elif not line.startswith("\t") and len(line)>0:
					splitline = string.split(line)
					print splitline[0]
					f.write("\n")
					target=splitline[0]
					target=target.lower()
					f.write(target)
				elif line.startswith("\t") and len(line)>0:
					 splitline = string.split(line)
					 f.write(" ")
					 target=splitline[0]
					 target=target.lower()
					 f.write(target)
				  
