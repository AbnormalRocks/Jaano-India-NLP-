from nlp import find
from route import route
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

dataset = pd.read_csv("dataset.csv")
dataset['srno'] = dataset.index
col = dataset.columns
list=[]

z = dataset.iloc[1::3, :]


#print(col[5])
for i in col:
	list.append(i)
#print(list[11])



search=""
from nltk import ngrams
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
	return render_template('home.html')
@app.route("/list",methods = ['POST', 'GET'])
def list():
	
		
	sentence = request.form['search']
	#print(sentence)
	
	sentence=sentence.lower()
	print(sentence)
	v = find(sentence)
	v=str(v)
	print(v)
	r = route(v)	
	
	return render_template('list.html', r=r)			


		 
		 


		 
if __name__ == '__main__':         
	app.run(debug=True)
