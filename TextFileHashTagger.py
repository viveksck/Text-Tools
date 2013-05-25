#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.com
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
'''
import re, os 

#SET VARIABLES 
path = os.getcwd()

#set up lists and dictionaries
print "Setting up"
taglist = [""]
contextlist = [""]
cloudstring=[""]
tagdictionary = dict()	

#create dictionary
print "creating dictionary"
file_paths = []
for folder, subs, files in os.walk(path):
  for filename in files:
    file_paths.append(os.path.abspath(os.path.join(folder, filename)))

#TODOinsert check for number of files and number of entries
filecount = 0
nohashcount = 0
for filename in file_paths:
    if filename.endswith(".txt") and not filename.startswith("0-"):
		filecount +=1
		note = open(filename, "r")
		refline = note.readline()
		hashline = note.readline()
		numberoflinestotry = 4
		if not hashline.startswith("#"):
			hashline = note.readline()
		if not hashline.startswith("#"):
			hashline = note.readline()
		if not hashline.startswith("#"):
			print "\n"
			print "THIS FILE NEEDS A HASHTAG"
			print filename
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
print " file(s) did not have hashtags. Names above."


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

#append the links
print "appending links"
for tag in sorted(tagdictionary.keys()):
	cloudstring.append("</align=center>		<h1> <A NAME="+tag+">"+tag+"</a></h1>")
	cloudstring.append("<br>\n")
	for file in file_paths:
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
cloudlisthtmlfile = os.path.realpath(path+"/"+"00index.html")
cloudlisthtml = open(cloudlisthtmlfile, "w")
cloudlisthtml.write(cloudfinalreally)
cloudlisthtml.close()