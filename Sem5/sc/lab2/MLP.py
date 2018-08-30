import csv
import random
from random import shuffle
from math import exp
from random import randrange

def get_data(file,y_in):
	reader = csv.reader(open(file),delimiter=",")
	data=[]
	c=0
	for row in reader:
		if(c==0):
			c+=1
			continue
		data.append(row)
	random.seed(123)
	shuffle(data)
	for item in data:
		item[-1], item[y_in] = item[y_in], item[-1]
	X=[]
	y=[]
	for row in data:
		X.append(row[:-1])
		y.append(row[-1])
	unique=[]
	for i in range(len(y)):
		if y[i] not in unique:
			unique.append(y[i])
	for i in range(len(y)):
		y[i]=unique.index(y[i])
	for i in range(len(X)):
		for j in range(len(X[0])):
			X[i][j]=float(X[i][j])
	for i in range(len(X)):
		X[i]=[1]+X[i]
	data=[]
	for i in range(len(X)):
		data.append(X[i]+[y[i]])
	return data

