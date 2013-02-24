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
Some changes by Charles Kelly, July 2-7, 2011, http://aitech.ac.jp/~ckelly - added tab-separated files, fixed the word length = 0 bug (e.g. eng-us-all-4gram-20090715-191.csv), and added the file naming and timing

Before using, check memory requirements and see the note on thresholds in the article linked in Google code wiki
'''


import os
import time

#Set Year and threshold.
earliestyear = 1994
yourthreshold = 3000

#We're using "more than", so minus one from year and from threshold
pythonearliestyear = earliestyear-1
threshold=yourthreshold-1


# CK added time
localtime = time.asctime( time.localtime(time.time()) )
print "\n==== "
print "====         Start Time: ", localtime
print "====      Earliest Year: ", earliestyear
print "====      Threshold: ", threshold
print "====\n"

path=os.getcwd()
filelist=os.listdir(path)   

def filteryearandalphabetise():
    path=os.getcwd()
    filelist=os.listdir(path)  
    tempfileA =  "Alphabetised_TEMP_A"+"."+str(earliestyear)
    unfilteredA = open(tempfileA, 'a')        
    tempfileB =  "Alphabetised_TEMP_B"+"."+str(earliestyear)
    unfilteredB = open(tempfileB, 'a')
    tempfileC =  "Alphabetised_TEMP_C"+"."+str(earliestyear)
    unfilteredC = open(tempfileC, 'a')
    tempfileD =  "Alphabetised_TEMP_D"+"."+str(earliestyear)
    unfilteredD = open(tempfileD, 'a')
    tempfileE =  "Alphabetised_TEMP_E"+"."+str(earliestyear)
    unfilteredE = open(tempfileE, 'a')
    tempfileF =  "Alphabetised_TEMP_F"+"."+str(earliestyear)
    unfilteredF = open(tempfileF, 'a')
    tempfileG =  "Alphabetised_TEMP_G"+"."+str(earliestyear)
    unfilteredG = open(tempfileG, 'a')
    tempfileH =  "Alphabetised_TEMP_H"+"."+str(earliestyear)
    unfilteredH = open(tempfileH, 'a')
    tempfileI =  "Alphabetised_TEMP_I"+"."+str(earliestyear)
    unfilteredI = open(tempfileI, 'a')
    tempfileJ =  "Alphabetised_TEMP_J"+"."+str(earliestyear)
    unfilteredJ = open(tempfileJ, 'a')
    tempfileK =  "Alphabetised_TEMP_K"+"."+str(earliestyear)
    unfilteredK = open(tempfileK, 'a')
    tempfileL =  "Alphabetised_TEMP_L"+"."+str(earliestyear)
    unfilteredL = open(tempfileL, 'a')
    tempfileM =  "Alphabetised_TEMP_M"+"."+str(earliestyear)
    unfilteredM = open(tempfileM, 'a')
    tempfileN =  "Alphabetised_TEMP_N"+"."+str(earliestyear)
    unfilteredN = open(tempfileN, 'a')
    tempfileO =  "Alphabetised_TEMP_O"+"."+str(earliestyear)
    unfilteredO = open(tempfileO, 'a')
    tempfileP =  "Alphabetised_TEMP_P"+"."+str(earliestyear)
    unfilteredP = open(tempfileP, 'a')
    tempfileQ =  "Alphabetised_TEMP_Q"+"."+str(earliestyear)
    unfilteredQ = open(tempfileQ, 'a')
    tempfileR =  "Alphabetised_TEMP_R"+"."+str(earliestyear)
    unfilteredR = open(tempfileR, 'a')
    tempfileS =  "Alphabetised_TEMP_S"+"."+str(earliestyear)
    unfilteredS = open(tempfileS, 'a')
    tempfileT =  "Alphabetised_TEMP_T"+"."+str(earliestyear)
    unfilteredT = open(tempfileT, 'a')
    tempfileU =  "Alphabetised_TEMP_U"+"."+str(earliestyear)
    unfilteredU = open(tempfileU, 'a')
    tempfileV =  "Alphabetised_TEMP_V"+"."+str(earliestyear)
    unfilteredV = open(tempfileV, 'a')
    tempfileW =  "Alphabetised_TEMP_W"+"."+str(earliestyear)
    unfilteredW = open(tempfileW, 'a')
    tempfileX =  "Alphabetised_TEMP_X"+"."+str(earliestyear)
    unfilteredX = open(tempfileX, 'a')
    tempfileY =  "Alphabetised_TEMP_Y"+"."+str(earliestyear)
    unfilteredY = open(tempfileY, 'a')
    tempfileZ =  "Alphabetised_TEMP_Z"+"."+str(earliestyear)
    unfilteredZ = open(tempfileZ, 'a')
    tempfileELSE =  "Alphabetised_TEMP_ELSE"+"."+str(earliestyear)
    unfilteredELSE =  open(tempfileELSE, 'a')
    filesprocessed=0
    for filename in filelist:
            if filename.endswith("csv"):
                    filesprocessed=filesprocessed+1
                    print filesprocessed
                    filedictionary= dict()
                    for line in open(filename):
                            column = line.split("\t")
                            if len(column) > 1:
                                    year = column[1]
                                    if year.isdigit() and int(year) > pythonearliestyear:
                                            ngram = column[0]
                                            key = ngram.lower()
                                            value = str(column[2])
                                            if key not in filedictionary:
                                                    filedictionary[key] = value
                                            else:
                                                    filedictionary[key] = (int(filedictionary[key]) + int(value))
                    for key in filedictionary:
                        if key.startswith("a"):
                            unfilteredA.write(str(key))
                            unfilteredA.write("\t")
                            unfilteredA.write(str(filedictionary[key]))
                            unfilteredA.write("\n")
                        elif key.startswith("b"):
                            unfilteredB.write(str(key))
                            unfilteredB.write("\t")
                            unfilteredB.write(str(filedictionary[key]))
                            unfilteredB.write("\n")
                        elif key.startswith("c"):
                            unfilteredC.write(str(key))
                            unfilteredC.write("\t")
                            unfilteredC.write(str(filedictionary[key]))
                            unfilteredC.write("\n")
                        elif key.startswith("d"):
                            unfilteredD.write(str(key))
                            unfilteredD.write("\t")
                            unfilteredD.write(str(filedictionary[key]))
                            unfilteredD.write("\n")
                        elif key.startswith("e"):
                            unfilteredE.write(str(key))
                            unfilteredE.write("\t")
                            unfilteredE.write(str(filedictionary[key]))
                            unfilteredE.write("\n")
                        elif key.startswith("f"):
                            unfilteredF.write(str(key))
                            unfilteredF.write("\t")
                            unfilteredF.write(str(filedictionary[key]))
                            unfilteredF.write("\n")
                        elif key.startswith("g"):
                            unfilteredG.write(str(key))
                            unfilteredG.write("\t")
                            unfilteredG.write(str(filedictionary[key]))
                            unfilteredG.write("\n")
                        elif key.startswith("h"):
                            unfilteredH.write(str(key))
                            unfilteredH.write("\t")
                            unfilteredH.write(str(filedictionary[key]))
                            unfilteredH.write("\n")
                        elif key.startswith("i"):
                            unfilteredI.write(str(key))
                            unfilteredI.write("\t")
                            unfilteredI.write(str(filedictionary[key]))
                            unfilteredI.write("\n")
                        elif key.startswith("j"):
                            unfilteredJ.write(str(key))
                            unfilteredJ.write("\t")
                            unfilteredJ.write(str(filedictionary[key]))
                            unfilteredJ.write("\n")
                        elif key.startswith("k"):
                            unfilteredK.write(str(key))
                            unfilteredK.write("\t")
                            unfilteredK.write(str(filedictionary[key]))
                            unfilteredK.write("\n")
                        elif key.startswith("l"):
                            unfilteredL.write(str(key))
                            unfilteredL.write("\t")
                            unfilteredL.write(str(filedictionary[key]))
                            unfilteredL.write("\n")
                        elif key.startswith("m"):
                            unfilteredM.write(str(key))
                            unfilteredM.write("\t")
                            unfilteredM.write(str(filedictionary[key]))
                            unfilteredM.write("\n")
                        elif key.startswith("n"):
                            unfilteredN.write(str(key))
                            unfilteredN.write("\t")
                            unfilteredN.write(str(filedictionary[key]))
                            unfilteredN.write("\n")
                        elif key.startswith("o"):
                            unfilteredO.write(str(key))
                            unfilteredO.write("\t")
                            unfilteredO.write(str(filedictionary[key]))
                            unfilteredO.write("\n")
                        elif key.startswith("p"):
                            unfilteredP.write(str(key))
                            unfilteredP.write("\t")
                            unfilteredP.write(str(filedictionary[key]))
                            unfilteredP.write("\n")
                        elif key.startswith("q"):
                            unfilteredQ.write(str(key))
                            unfilteredQ.write("\t")
                            unfilteredQ.write(str(filedictionary[key]))
                            unfilteredQ.write("\n")
                        elif key.startswith("r"):
                            unfilteredR.write(str(key))
                            unfilteredR.write("\t")
                            unfilteredR.write(str(filedictionary[key]))
                            unfilteredR.write("\n")
                        elif key.startswith("s"):
                            unfilteredS.write(str(key))
                            unfilteredS.write("\t")
                            unfilteredS.write(str(filedictionary[key]))
                            unfilteredS.write("\n")
                        elif key.startswith("t"):
                            unfilteredT.write(str(key))
                            unfilteredT.write("\t")
                            unfilteredT.write(str(filedictionary[key]))
                            unfilteredT.write("\n")
                        elif key.startswith("u"):
                            unfilteredU.write(str(key))
                            unfilteredU.write("\t")
                            unfilteredU.write(str(filedictionary[key]))
                            unfilteredU.write("\n")
                        elif key.startswith("v"):
                            unfilteredV.write(str(key))
                            unfilteredV.write("\t")
                            unfilteredV.write(str(filedictionary[key]))
                            unfilteredV.write("\n")
                        elif key.startswith("w"):
                            unfilteredW.write(str(key))
                            unfilteredW.write("\t")
                            unfilteredW.write(str(filedictionary[key]))
                            unfilteredW.write("\n")
                        elif key.startswith("x"):
                            unfilteredX.write(str(key))
                            unfilteredX.write("\t")
                            unfilteredX.write(str(filedictionary[key]))
                            unfilteredX.write("\n")
                        elif key.startswith("y"):
                            unfilteredY.write(str(key))
                            unfilteredY.write("\t")
                            unfilteredY.write(str(filedictionary[key]))
                            unfilteredY.write("\n")
                        elif key.startswith("z"):
                            unfilteredZ.write(str(key))
                            unfilteredZ.write("\t")
                            unfilteredZ.write(str(filedictionary[key]))
                            unfilteredZ.write("\n")
                        else:
                            unfilteredELSE.write(str(key))
                            unfilteredELSE.write("\t")
                            unfilteredELSE.write(str(filedictionary[key]))
                            unfilteredELSE.write("\n")
                                

def combinecapitalsandapplythreshold():
        path=os.getcwd()
        filelist=os.listdir(path)  
        finalfilename = "FINAL RESULTS SINCE" + str(earliestyear)+"THRESHOLD"+str(threshold)+".txt"
        resultsfile = open(finalfilename, 'a')
        for filename in filelist:
            if filename.endswith(str(earliestyear)):
                    print filename
                    filedictionary= dict()
                    for line in open(filename):
                        column = line.split("\t")
                        key = column[0]
                        value = str(column[1])
                        if key not in filedictionary:             
                                filedictionary[key] = value
                        else:
                                filedictionary[key] = (int(filedictionary[key]) + int(value))

                    for key in filedictionary:
                            if int(filedictionary[key]) > threshold:
                                    resultsfile.write(str(key))
                                    resultsfile.write("\t")
                                    resultsfile.write(str(filedictionary[key]))
                                    resultsfile.write("\n")




#Check for what has already been done. Just in case the data folder is not clear from previous runs
filecount=0
finaldone=0
for file in filelist:
    if file.endswith(str(earliestyear)):
        filecount=filecount+1
    if file.endswith(str(earliestyear)+"THRESHOLD"+str(threshold)+".txt"):
        finaldone=1
        
if filecount is 0 and finaldone is 0:
    print "Creating alphabet sorted temp files"
    print "Files processed:"
    filteryearandalphabetise()
    print "Finished created alphabet-sorted temp files for this year."
    print "Now combining the capitalised versions and creating final results file\n\n"
    combinecapitalsandapplythreshold()
    print "Finished combining the capitalised versions and creating final results file\n\n"
    
elif filecount is 27 and finaldone is 0:
    print "Found alphabet-sorted temp files for target already in this folder.\n\n"
    print "Now combining the capitalised versions and creating final results file\n\n"
    combinecapitalsandapplythreshold()
    print "Finished combining the capitalised versions and creating final results file\n\n"

elif finaldone is 1:
    print "You already have results for the exact year and threshold you added. Stopping. Clean the folder of results if you want to repeat a search"

else:
    print "Something is weird. Here's my guess: you have "
    print filecount
    print "temp files."
    print "Either a temp file is missing or you haven't cleaned a run properly before repeating it"

# CK addition
localtime2 = time.asctime( time.localtime(time.time()) )
print "\n==== "
print "====  Start Time: ", localtime
print "====    End Time: ", localtime2
print "====\n"