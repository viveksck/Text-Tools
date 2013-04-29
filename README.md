Text-Tools Overview
==========

Various tools for working with text and corpora.

1. malc-text-grader - for creating graded readings, and analysing vocabulary
2. firstfivewords.py - for pulling formulaic sentence starters from a corpus of text
3. ngramstripper2009.py - for simplifying the Google Books ngram data into a frequency word list
4. TextFileHashTagger.py - for a folder full of text files containing hash tags, creates an index 

*Some projects have been described in articles. PDFs available here: http://scholar.google.co.jp/citations?user=-ShxkTcAAAAJ
*Some projects have a screencast showing how to use them: http://www.youtube.com/user/malcprentice
*My normal website here: http://alba-english.com

---

1) text-grader.py
================
Requires Python. Collocation and readability features require NLTK (http://nltk.org/)

For text, pasted in or opened from a txt file, the script will 
*give basic information on the vocab in the text 
*highlight the vocabulary by colour using its frequency (British National Corpus lists; General Service List, Academic Word List)
*list the words which are from each list, andwhich are MISSING from each list

The initial aim was to allow easy editing of a text to make it graded - to remove low frequency words, or to deliberately suggest words of a
certain level for inclusion. Existing programs either did not work on mac, or crashed, or analysed the text without allowing editing. 

Some other bits and pieces such as collocations and readability indices added for fun, but these require NLTK to be installed
(http://nltk.org/)

ISSUES
*very slow on long texts
*Just cannot work out how to add "ctrl-a" select all or get undo/redo working on mac
*broken under Python 2.6. Fine for 2.7+ - no plans to fix this. 

Code released under GNU GPL, but the word Lists embedded in file used are from RANGE (http://www.victoria.ac.nz/lals/about/staff/paul-nation),
used by permission.

Article describing this tool here: http://scholar.google.co.jp/citations?view_op=view_citation&hl=en&user=-ShxkTcAAAAJ&citation_for_view=-ShxkTcAAAAJ:Tyk-4Ss8FVUC

2) firstfivewords.py
===========
Requires:  Python, NLTK. Run from commandline in a directory containing text files.

Will process every text file in the folder it's run in, identify every sentence, and create three csv files with 3,4 and 5 words sentence starter (counts punctuation as a token). Initially created to help a colleague avoid hand-sorting large amounts of data.  

e.g. top five three-word sentence starters used in 90 undergraduate Uni Japanese essays are: "For example , / In addition , / However , I / Of course , / When I was". Note that punctuation is counted as a token in this version.

Aim is to identify formulaic language used to start sentences in a corpus of essays - either a student corpus or a target advanced learner / native speaker corpus Formulaic language adds fluency, accuracy and appropriateness to student writing. 

If you can get your students essays in TXT format, then for sentence starters you can:
*measure uptake (are they using what you teach) 
*measure progress (from beginning of term to end) 
*identify lacks, compared to a native corpus or more advanced learners 


If you're using this for serious analysis rather than lesson planning , check your results against a hand-coded example. 

Article describing this tool here:  http://scholar.google.co.jp/scholar?oi=bibs&hl=en&cluster=13556166500242376745&btnI=Lucky


3) ngramstripper2009.py
=============
Python script for pulling usable word lists (single tokens, bigrams, trigrams, 4-grams and 5-grams) from Google Books nGram datasets

A lot of books were scanned for Google Books project. It's not the biggest corpus in the world, but it's close. The English section is about
300 billion tokens - 20.6 billion "the"s alone. There are various subsets: US English, UK, Fiction and a random sample of a million books.
However, it's hard to analyse the lists for useful information when even opening files is difficult. The files are 1GB each (up to 800 of
them), with words dating back to 1520, split across files by capitalisation.

Run the script in a folder of Google ngram data CSV files from here: http://ngrams.googlelabs.com/datasets 

It will go line by line through the files, sorts some split-across-files-by-capitalisation errors, and output the list you tell it to ( e.g.
"words before 1994 occurring 10000+ times". It takes about 10 mins to do this for the 1-grams.

In theory, the script also works with 2,3,4 and 5grams. In practice, 5-grams require a 3TB hard disk and 20GB+ of memory (swap memory works
but is so slow it's pointless. I'm rewriting the script now)

As a teacher, there's no reason you would want to do any of the above. I was just curious. The corpus is full of uncorrected OCR errors and
has a suspicious number of quote marks, and a number of other issues that mean you should probably stick to the BNC / COCA / GSL or whatever
you are using now. See article below for the limitations. Unless you desperately want to make your own Fiction / 1890 / 3 gram list for some reason, email me for a list copy.

Article PDF describing this tool available here: http://scholar.google.co.jp/citations?view_op=view_citation&hl=en&user=-ShxkTcAAAAJ&citation_for_view=-ShxkTcAAAAJ:9yKSN-GCB0IC

ngramstripper2012.py
====================
Google recently released new data, alphabetised and with POS. Work ongoing on an update. Slowly. 


4) TextFileHashTagger.py
===================
I was tired of pulling files in and out of Zotero, Mendeley, and other reference management software, so I decided to just use PDF files and TXT notes. Problem is, I liked the ability to tag files so they could appear in different projectså. This program, if you keep all your notes in one folder, will find all hashtags (e.g. #memory or #socialpsych), and also all tildatags which I use for context (e.g. ~canada, ~tertiary), and create an html index with links to the notes and a cloud of tags where size represents number of files with that tag. Checkes every file one time for every tag - very inefficient and slow for projects with large numbers of tags. Only works on a single folder - does not traverse folders yet. Will break on unusual characters, but tools available in "Single USe Tools" folder which can take a folder of PDFs, rename them cleanly, and create one TXT file for each ready to be indexed by the HashTagger. Tool also available for making a list of referneces in a TXT file into a bunch of clean filename reference files. 


Single use tools
===================
Just some scraps I've needed in the past to count, compare and preprocess things.
Filenamecleaner.py - cleans a folder of files from bad characters in their filenames (e.g. for Dropbox syncing, TextFileHashtTagger links)
NGRAM_linecountskipblankstabdelimited.py - counts the lines in file, without counting blank lines. 
NGRAM_topXcountY.py - ngramstripper has a built in lower bound on the frequency of words. If this is not used, the file is often to big to do it later by hand. Use this instead
NLTK_OverlapDiffTwoTextfiles.py - for two files, which are only in 1, which are only in 2, and which are in both. 
PythonifyNationRangeWordlists.py - Turns a folder of Paul Nation's word lists for RANGE (organised by tab with numbers) into lines, with headword at beginning, so easier to process for families. Used once to prepare lists for text-grader.py
TextFileHashTaggerPDFINDEXER.py - takes a folder of PDFs and produces one text file for each, ready for notes, with optional default tags. For TextFileHashTagger 
TextFileHashTagTXTFILEConverter - given a text file with one reference per line, produces one text file for each, ready for notes, with optional default tags. TextFileHashTagger

