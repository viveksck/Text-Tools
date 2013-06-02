#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org
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
import tkFileDialog, nltk, re


from Tkinter import *
root = Tk()

	
def OpenProcess():
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose file 1')
	if file != None:
		data1 = file.read()	
	file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose file 2')
	if file != None:
		data2 = file.read()	
	loweredtext1=[]
	loweredtext2=[]
	pattern = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''
	for token in data1:
		rawtext=nltk.regexp_tokenize(data1, pattern)	
	for token in rawtext:
		loweredtext1.append(token.lower())
	for token in data2:
		rawtext=nltk.regexp_tokenize(data2, pattern)	
	for token in rawtext:
		loweredtext2.append(token.lower())
	f = open("results.txt", 'w')
	f.write("")
	f.close()
	f = open("results.txt", 'a')	
	f.write("File 1 has ")
	f.write(str(len(loweredtext1)))
	f.write(" tokens and ")
	f.write(str(len(set(loweredtext1))))
	f.write("types. ")
	f.write("File 2 has ")
	f.write(str(len(loweredtext2)))
	f.write(" tokens and ")
	f.write(str(len(set(loweredtext2))))
	f.write(" types.")
	f.write("\n\n The overlapping words are: \n\n\n")
	for word in loweredtext1:
		if word in loweredtext2:
			f.write(word)
			f.write(" ")
	f.close()

OpenProcess()