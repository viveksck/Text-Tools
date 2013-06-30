#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.org

# Copyright 2011 Malcolm Prentice
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


'''
THANKS TO:
Various snippets of code came from stackoverflow (http://stackoverflow.com/), the NLTK manual and website (http://www.nltk.org/)
'''

#Define filter lists - names or any other words you want excluded from analysis
filterlistunsplit = ('''Malcolm Prentice ''')


#Stopword list from NLTK stopwords corpus
stopwords = (''' i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now''')

#Check Version - TkInter breaks on 2.6
import sys
if not sys.version_info[:2] == (2, 7):
	print "THIS PROGRAM REQUIRES PYTHON 2.7"

import string, re

from Tkinter import *
root = Tk()
root.geometry("800x600")
root.title("Text Grader")

p = re.compile(r'\W+')

     
def ShowCollocations():
	text.insert(END, "If this doesn't work, please check you have NLTK, PyYAML and the stopword list from the NLTK loaded. See Help for details \n\n\n")
	import nltk
	from nltk.collocations import BigramCollocationFinder
	from nltk.collocations import TrigramCollocationFinder
	from nltk.metrics import BigramAssocMeasures
	from nltk.metrics import TrigramAssocMeasures
	pattern = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''
	data = resultsbox.get(1.0,END)
	rawtext=nltk.regexp_tokenize(data, pattern)
	prepcolloc = [word.lower() for word in rawtext if not word in stopwords and word.isalpha()]
	text.delete(1.0, END)
	text.insert(END, "Collocations (occurring at least 3 times with a PMI of 10)\n")
	text.insert(END, "\nBigram Collocations:\n")
	bigram = BigramAssocMeasures()
	bigramfinder = BigramCollocationFinder.from_words(prepcolloc)
	bigramfinder.apply_freq_filter (3)
	bigrams=bigramfinder.nbest(bigram.pmi, 10)
	for item in bigrams:
		first = item[0]
		second = item[1]
		text.insert(END, first)
		text.insert(END, " ")
		text.insert(END, second)
		text.insert(END, "\n")

def ShowReadability():
    text.insert(END, "If this doesn't work, check NLTK is installed. If NLTK is installed, use nltk.download() to get cmudict and punkt sentence tokenizer. See Help for details \n\n\n")
    import nltk
    pattern = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''
    data = resultsbox.get(1.0,END)
    rawtext=nltk.regexp_tokenize(data, pattern)
    prepcolloc = (w.lower() for w in rawtext)
    text.delete(1.0, END)
    #sentences
    sentcountshort = 0
    sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
    sents = sent_tokenizer.tokenize(data)    
    for sent in sents:
        if len(sent) < 2:
            sentcountshort = sentcountshort+1
    
    numsents = len(sents) - sentcountshort
    numwords = len(p.split(data))-1
    sentcountshort = 0
    
    text.insert(END, "\nIgnoring one word sentences (like numbering), there are ")
    text.insert(END, numsents)
    text.insert(END, " sentences with an average of ")
    averagewordspersentence = numwords/numsents
    text.insert(END, averagewordspersentence)
    text.insert(END, " words per sentence.\n\n")


    #set up syllable dictionary        
    from math import sqrt as squareroot
    from nltk.corpus import cmudict
    syllables = dict()
    numeral = re.compile(r'\d')
    for (word, phonemes) in cmudict.entries():
        word = word.lower()
        count = len([x for x in list(''.join(phonemes)) if x >= '0' and x <= '9'])
        if syllables.has_key(word):
            count = min(count, syllables[word])
        syllables[word] = count        

    #count syllables    
    numsyllables=0
    wordsnotincmu=dict()
    for word in prepcolloc:
        if word in syllables:
            numsyllables = numsyllables + syllables[word]
    else:
        wordsnotincmu[word] = 1
        
    #count three syllable words
    threesyllcount=0
    for word in prepcolloc:
        if word in syllables and syllables[word] > 2:
            threesyllcount = threesyllcount + syllables[word]
        

    #calculate number of letters and numbers
    letnumcount=0
    for word in rawtext:
        if word.isalpha():
            letnumcount=letnumcount + len(word)        

    #adapted from Java at http://www.editcentral.com/gwt1/EditCentral.html
	#Flesch    
	Flesch = 206.835 - (1.015 * numwords) / numsents - (84.6 * numsyllables) / numwords
	Flesch = "%.1f" % Flesch
	#Automated readability index
	ARI = (4.71 * letnumcount) / numwords + (0.5 * numwords) / numsents -21.43;
	ARI = "%.1f" % ARI

	#Flesch-Kincaid grade level
	FK = (0.39 * numwords) / numsents + (11.8 * numsyllables) / numwords - 15.59;
	FK = "%.1f" % FK

	#Coleman-Liau index
	CL = (5.89 * letnumcount) / numwords - (30.0 * numsents) / numwords - 15.8;
	CL = "%.1f" % CL

	#gunning fog
	GunningFog = 0.4 * ( numwords / numsents + (100.0 * threesyllcount) / numwords );
	GunningFog = "%.1f" %GunningFog    
	#SMOG
	smog = squareroot( threesyllcount * 30.0 / numsents ) + 3.0;
	smog = "%.1f" % smog
	
    text.insert(END, "Flesch: ")
    text.insert(END, Flesch)
    text.insert(END, "\n")
    text.insert(END, "Automated readability index: ")
    text.insert(END, ARI)
    text.insert(END, "\n")
    text.insert(END, "Flesch-Kincaid grade level: ")
    text.insert(END, FK)
    text.insert(END, "\n")

    text.insert(END, "Coleman-Liau index: ")
    text.insert(END, CL)
    text.insert(END, "\n")

    text.insert(END, "Gunning fog index: ")
    text.insert(END, GunningFog)
    text.insert(END, "\n")

    text.insert(END, "Smog: ")
    text.insert(END, smog)
    text.insert(END, "\n\n")
    
    text.insert(END, "Following words not included in analysis - syllable count is missing from the cmudict database:\n\n")
    for k,y in sorted(wordsnotincmu.items()):
        text.insert(END, k)

    
    
def ShowHelp():
    text.delete(1.0, END)
    text.insert(END, "You need to install the Natural Language Toolkit (NLTK)\n\n 1) Install the Natural Language ToolkitNLTK, along with the other programs it needs - instructions at http://www.nltk.org/download.\n\n 2) Install the Punkt package - http://www.nltk.org/data\n\n\n\n") 
    
    
    

def OpenFile():
    import tkFileDialog
    resultsbox.delete(1.0,END)
    text.delete(1.0,END)
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        data = file.read()
        for word in data:
            if "\r" in word and not "\n" in word:
                resultsbox.insert(END, word)
                resultsbox.insert(END, "\n")
            else:
                resultsbox.insert(END, word)

def SaveText():
    from time import gmtime, strftime
    reftime = strftime("%b_%d_%Y__%H_%M_%S")
    f = open("EDITED TEXT_Version_"+reftime+".txt", 'a')    
    notes = resultsbox.get(1.0, END)
    notes = notes.encode('utf-8')
    f.write(notes)
    f.close()
    
def SaveInfo():
    from time import gmtime, strftime
    reftime = strftime("%b_%d_%Y__%H_%M_%S")
    f = open("RESULTS_Version_"+reftime+".txt", 'a')    
    notes = text.get(1.0, END)
    notes = notes.encode('utf-8')
    f.write(notes)
    f.close()
    
#PACK interface
                
textframe = Frame(root, bd=5, relief=SUNKEN)
resultsframe = Frame(root, bd=5, relief=SUNKEN)
buttonframe = Frame(root, bd=5, relief=SUNKEN)


collocations_button = Button(buttonframe, text="Collocations", command = ShowCollocations)
readability_button = Button(buttonframe, text="Readability", command = ShowReadability)

openfile_button = Button(buttonframe, text="Open File", command = OpenFile)
savetext_button = Button(buttonframe, text="Save Text (bottom box)", command = SaveText)
saveinfo_button = Button(buttonframe, text="Save Info (top box)", command = SaveInfo)
help_button = Button (buttonframe, text="Help & About", command = ShowHelp)

textscrollbar = Scrollbar(textframe, orient=VERTICAL)
text = Text(textframe, yscrollcommand=textscrollbar.set, takefocus=0)
textscrollbar.configure(command=text.yview)


resultsscrollbar = Scrollbar(resultsframe, orient=VERTICAL)
resultsbox = Text(resultsframe, yscrollcommand=resultsscrollbar.set, takefocus=0)
resultsscrollbar.configure(command=resultsbox.yview)



collocations_button.pack(side=LEFT)
readability_button.pack(side=LEFT)
openfile_button.pack(side=LEFT)
savetext_button.pack(side=LEFT)
saveinfo_button.pack(side=LEFT)
help_button.pack(side=LEFT)

text.pack(side=LEFT, fill=BOTH, expand=1)
textscrollbar.pack(side=RIGHT, fill=Y)

resultsbox.pack(side=LEFT,fill=BOTH, expand=1)
resultsscrollbar.pack(side=RIGHT, fill=Y)

buttonframe.pack(fill=X, expand=1)

textframe.pack(fill=BOTH, expand=1)
resultsframe.pack(fill=BOTH, expand=1)

resultsbox.insert(END, "Open a text (TXT) file using the buttons above, paste text here, or just start typing")
text.insert(END, "Information will appear here after you run the program")
root.mainloop()
    


