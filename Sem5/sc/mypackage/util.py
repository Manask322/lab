import csv
import random
from random import shuffle


class util:
	def __init__(self, *args, **kwargs):
		pass
	
	def get_data(self,file,y_in):
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
		c=0
		# print(data)
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

	def accuracy_metric(self,actual, predicted):
		correct = 0
		for i in range(len(actual)):
			if actual[i] == predicted[i]:
				correct += 1
		return correct / float(len(actual)) * 100.0

	def confusion_matrix(self,y,y_pred):
		tp=0
		fp=0
		fn=0
		tn=0
		for i,j in zip(y,y_pred):
			if i==0:
				if j==0:
					tn+=1
				else:
					fp+=1
			elif i==1:
				if j==1:
					tp+=1
				else:
					fn+=1
		precision=tp/(tp+fp)
		recall=tp/(tp+fn)
		return precision,recall
