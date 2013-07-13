#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org

import commands
cloudstring=[""]
tagdictionary = dict()	
filecount = 0
nohashcount = 0
cloudlisthtmlfile = ("/Users/malc/Desktop/Dropbox/CODE/00index.html")  #output location for index file

filelist = commands.getoutput('mdfind -onlyin ~/Desktop/Dropbox/CODE/ "#ref"')
filelist = sorted(filelist.split("\n"))

fileindex = 0
for file in filelist:
	filecount = filecount+1
	if file.endswith("txt"):
		note = open(file, "r")
		refline = note.readline()
		hashline = note.readline()
		if not hashline.startswith("#"):
			hashline = note.readline()
		if not hashline.startswith("#"):
			hashline = note.readline()
		if not hashline.startswith("#"):
			print "\n"
			print "MOVE THIS FILE'S HASHTAG UP A FEW LINES"
			print file
			print "\n"
			nohashcount +=1
		for word in str.split(hashline):
			word=word.lower()		
			if not word.startswith("##") and not word.endswith("#") and not word.endswith("~") and not word.startswith("#ref") and word.startswith("#"):
				if word in tagdictionary:
					tagdictionary[word] = (int(tagdictionary[word]) + 1)
				else:
					tagdictionary[word] = 1

#Print check for files
print filecount,
print " reference files processed. Is this correct?"
print nohashcount, 
print " file(s) have misplaced hashtags. See above."


#append cloud
cloudstring.append(r"<h1>Topic</h1>")	
for tag in sorted(tagdictionary.keys()):
	if tag.startswith("#"):
		cloudstring.append(r" <font size=")
		cloudstring.append(str(tagdictionary[tag]+1))
		cloudstring.append(r"><a href='#"+tag+r"'>"+tag+r"</a></font size> ")

cloudstring.append(r"<h1>Context</h1>")	

for tag in sorted(tagdictionary.keys()):
	if tag.startswith("~"):
		cloudstring.append(r" <font size=")
		cloudstring.append(str(tagdictionary[tag]+1))
		cloudstring.append(r"><a href='#"+tag+r"'>"+tag+r"</a></font size> ")


for tag in sorted(tagdictionary.keys()):
	cloudstring.append("</align=center>		<h1> <A NAME="+tag+">"+tag+"</a></h1>")
	cloudstring.append("<br>\n")
	for file in filelist:
		if file.endswith(".txt") and not file.startswith("0-"):		
			pdfpath = file[:-4] + ".pdf"
			filename= file
			note = open(file, "r")
			refline = note.readline()
			hashline = note.readline()
			if not hashline.startswith("#"):
				hashline = note.readline()
			if not hashline.startswith("#"):
				hashline = note.readline()
			for word in str.split(hashline):
				if tag in word:
					cloudstring.append("<a href="+"\"file://")
					cloudstring.append(""+file+"")
					cloudstring.append("\">"+refline+"</a>")
					cloudstring.append(" <a href="+"\"file://")
					cloudstring.append(""+pdfpath+"")
					cloudstring.append("\"> <strong><font color=\"FF00CC\">FILE</font></strong></a>")
					cloudstring.append("</p>\n")		
		
cloudstring.append(r"</body</html>")

#MAKE THE INDEX
print "making the index"
cloudfinalreally = ''.join(cloudstring)
cloudlisthtml = open(cloudlisthtmlfile, "w")
cloudlisthtml.write(cloudfinalreally)
cloudlisthtml.close()




