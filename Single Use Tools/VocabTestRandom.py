#!/usr/bin/env python

#generates ten random numbers in format pasteable into end of term vocab test file. 
import random

print "From a sample of 140"
list =   random.sample(xrange(140), 10) 
for item in list:
	print item

print "From a sample of 280"
list =   random.sample(xrange(280), 10) 
for item in list:
	print item

