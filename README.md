Text-Tools
==========

Various tools for working with text and corpora.
Finished projects usually have an accompanying academic article, which if published should be available from here: http://scholar.google.co.jp/citations?user=-ShxkTcAAAAJ


First-Five-Words
===========
Requires:  Python, NLTK. Run from commandline in a directory containing text files.

Will process every text file in the folder it's run in, identify every sentence, and create three csv files with 3,4 and 5 words sentence starter (counts punctuation as a token). Initially created to help a colleague avoid hand-sorting large amounts of data. 

e.g. top five three-word sentence starters used in 90 undergraduate Uni Japanese essays are: "For example , / In addition , / However , I / Of course , / When I was". Note that punctuation is counted as a token in this version.

Aim is to identify formulaic language used to start sentences in a corpus of essays - either a student corpus or a target advanced learner / native speaker corpus Formulaic language adds fluency, accuracy and appropriateness to student writing. 

. If you can get your students essays in TXT format, then for sentence starters you can:
-measure uptake (are they using what you teach) 
-measure progress (from beginning of term to end) 
-identify lacks, compared to a native corpus or more advanced learners 


If you're using this for serious analysis rather than lesson planning , check your results against a hand-coded example. See article entitled "A Method for Extracting Formulaic Sequences from a Student Corpus" (http://scholar.google.co.jp/scholar?oi=bibs&hl=en&cluster=13556166500242376745&btnI=Lucky)


