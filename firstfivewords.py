#!/usr/bin/env python
# Malcolm Prentice
# github@alba-english.com
# http://alba-english.com

#pulls formulaic sentence starters from a corpus

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
#set threshhold
threshhold=0

import os, re, csv, nltk
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
pattern = r'''(?x)([A-Z]\.)+|\w+([-']\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;"'?():-_']'''

import string
import Tkinter, tkFileDialog
root=Tkinter.Tk()
path=tkFileDialog.askdirectory(parent=root,initialdir="/",title='Select a directory')


filelist=os.listdir(path)
filedictionary3 = dict()
filedictionary4 = dict()
filedictionary5 = dict()

for filename in filelist:
﻿  if filename.endswith("txt"):
﻿  ﻿  ﻿  filepath=path+"/"+filename
﻿  ﻿  ﻿  file = open(filepath, 'r')﻿  
﻿  ﻿  ﻿  data=file.read()
﻿  ﻿  ﻿  sents = sent_tokenizer.tokenize(data)
﻿  ﻿  ﻿  for sentence in sents:
﻿  ﻿  ﻿  ﻿  if not "<" in sentence:
﻿  ﻿  ﻿  ﻿  ﻿  words=nltk.regexp_tokenize(sentence, pattern)
﻿  ﻿  ﻿  ﻿  ﻿  keyprep5 = ' '.join(words[0:5])
﻿  ﻿  ﻿  ﻿  ﻿  keyprep4 = ' '.join(words[0:4])
﻿  ﻿  ﻿  ﻿  ﻿  keyprep3 = ' '.join(words[0:3])
﻿  ﻿  ﻿  ﻿  ﻿  key5 = str(keyprep5)
﻿  ﻿  ﻿  ﻿  ﻿  key4 = str(keyprep4)
﻿  ﻿  ﻿  ﻿  ﻿  key3 = str(keyprep3)
﻿  ﻿  ﻿  ﻿  ﻿  if key5 not in filedictionary5:
﻿  ﻿  ﻿  ﻿  ﻿  ﻿  ﻿  filedictionary5[key5] = 1
﻿  ﻿  ﻿  ﻿  ﻿  else:
﻿  ﻿  ﻿  ﻿  ﻿  ﻿  ﻿  filedictionary5[key5] = (int(filedictionary5[key5]) + 1)
﻿  ﻿  ﻿  ﻿  ﻿  if key4 not in filedictionary4:
﻿  ﻿  ﻿  ﻿  ﻿  ﻿  ﻿  filedictionary4[key4] = 1
﻿  ﻿  ﻿  ﻿  ﻿  else:
﻿  ﻿  ﻿  ﻿  ﻿  ﻿  ﻿  filedictionary4[key4] = (int(filedictionary4[key4]) + 1)
﻿  ﻿  ﻿  ﻿  ﻿  if key3 not in filedictionary3:
﻿  ﻿  ﻿  ﻿  ﻿  ﻿  ﻿  filedictionary3[key3] = 1
﻿  ﻿  ﻿  ﻿  ﻿  else:
﻿  ﻿  ﻿  ﻿  ﻿  ﻿  ﻿  filedictionary3[key3] = (int(filedictionary3[key3]) + 1)﻿  

results5filepath=path+"/"+"results5.csv"
results4filepath=path+"/"+"results4.csv"
results3filepath=path+"/"+"results3.csv"
myfile = open(results5filepath, 'w')
mywriter = csv.writer(myfile, dialect='excel')
for k,y in sorted(filedictionary5.items()):
﻿  if filedictionary5[k] > threshhold:
﻿  ﻿  mywriter.writerow([k,y])
print "Here are the sentence counts for this corpus: "
print (sum(filedictionary5.values()))
print (sum(filedictionary4.values()))
print (sum(filedictionary3.values()))
print "\n Here are the sentence type counts for this corpus:\n"
print (len(filedictionary5.values()))
print " 5-gram sentence starter types, "
print (len(filedictionary4.values()))
print " 4-gram sentence starter types, and "
print (len(filedictionary3.values()))
print " 3-gram sentence starter types.\n"
myfile.close()            


myfile = open(results4filepath, 'w')
mywriter = csv.writer(myfile, dialect='excel')
for k,y in sorted(filedictionary4.items()):
﻿  if filedictionary4[k] > threshhold:
﻿  ﻿  mywriter.writerow([k,y])
myfile.close()            


myfile = open(results3filepath, 'w')
mywriter = csv.writer(myfile, dialect='excel')
for k,y in sorted(filedictionary3.items()):
﻿  if filedictionary3[k] > threshhold:
﻿  ﻿  mywriter.writerow([k,y])
myfile.close()            


