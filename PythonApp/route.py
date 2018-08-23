from nlp import find
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import io






dataset = pd.read_csv("dataset.csv")
#print(dataset)
dataset['srno'] = dataset.index
#print(dataset['srno'])

col = dataset.columns
list=[]

z = dataset.iloc[1::3, :]
y = pd.DataFrame(columns=['State','srno'])

i=0
state = ""
for row in z.itertuples(index=True, name='Pandas'):
	if(getattr(row, "State")!=state):
		i+=1
		y.loc[i] = [getattr(row,'State'),getattr(row,'srno')]
		state = getattr(row,'State')
	
	
#print(y)


#print(col[5])
for i in col:
	list.append(i)

def route(sentence):
	new = z[['State', sentence]].copy()
	x = dataset.iloc[1::3, :]
	print(x)
	y = pd.DataFrame(columns=['srno','State'])

	i=0
	state = ""
	for row in x.itertuples(index=True, name='Pandas'):
		if(getattr(row, "State")!=state):
			i+=1
			y.loc[i] = [getattr(row,'srno'),getattr(row,'State')]
			state = getattr(row,'State')
	#print(y)
	return y.values
	