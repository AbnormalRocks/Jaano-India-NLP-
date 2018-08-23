import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

dataset = pd.read_csv("dataset.csv")
col = dataset.columns
list=[]
llist=[]
#print(col[5])
for i in col:
	list.append(i)
#print(list[11])



import nltk
#nltk.download()
import re
#print(re.findall("[a-z]", "$34.55cash.kjhg32.,.f"))

def find(sentence):

	from nltk import ngrams
	#sentence = 'Primary Net Enrolment Ratio (%) DISE'
	n = 1
	k = 0
	max = 0
	s = ""
	
	sentence.lower();
	vgrams = ngrams(sentence.split(), n)


	vlist=[]


	
	for grams in vgrams:
	
		vlist.append(grams)
		map(lambda x:x.lower(),vlist)
	

	
	for i in list:
		#print(i)
		k = 0
		x=0
		y=0
		z=0
		ilist=[]
		igrams = ngrams(i.split(), n)
		for grams in igrams:
			ilist.append(grams)
		map(lambda x:x.lower(),ilist)
	
		for v in vlist:
			#print("x="+str(x))
			x+=1
		
			#print(v)
			for j in ilist:
				#print("y="+str(y))
				y+=1
			
				#print(j)
			
				if(v == j):
					#print("!@#$%^&&^%^&*())()*(*&^%$#@!@#$%^&*()(*&&*&^%$$%^&&^%$#@!@#$%^&      z="+str(z))
					z+=1
					#print(v)
					#print(j)
					k+=1;
					continue
				#print(3)
			#print(2)
		#print(1)
				
		if(k > max ):
			s = i
			max=k
			#print(k)
			#print(s)

	#print(s)
	return s
#sentence="Primary New Government Schools since 2003 (%) DISE"
#print(ngrams(sentence))
  

