#!/usr/bin/env python
#Malcolm Prentice - github@alba-english.com
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
notesfolder = os.listdir(path)

#set up lists and dictionaries
print "Setting up"
taglist = [""]
contextlist = [""]
cloudstring=[""]
tagdictionary = dict()	
print "creating dictionary"

#create dictionary
for note in notesfolder:
    file = os.path.realpath(path+"/"+note)
    if note.endswith("txt") and not note.startswith("0-0"):
        note = open(file, "r")    
        notetext = note.read()
        notetext = set([word.lower() for word in notetext.split()])
	for word in notetext:
		if word.startswith("#") or word.startswith("~"):
			if not word.startswith("##") and not word.endswith("#") and not word.endswith("~") and not word.startswith("#ref"):
				if word in tagdictionary:
					tagdictionary[word] = (int(tagdictionary[word]) + 1)
				else:
					tagdictionary[word] = 1

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
	for note in notesfolder:
		if note.endswith("txt") and not note.startswith("0-0"):		
			fullpath = path+"/"+note
			pdfpath = fullpath[:-4] + ".pdf"
			filename=note
			note = open(fullpath, "r")
			notetext = note.read()
			notewords = set([word.lower() for word in notetext.split()])
			cloudtagfilelist=[""]
			if tag in notewords and not tag.startswith("##"):
				cloudstring.append("<a href="+"\"file://")
				cloudstring.append(""+fullpath+"")
				cloudstring.append("\">"+filename[:-4]+"</a>")
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
