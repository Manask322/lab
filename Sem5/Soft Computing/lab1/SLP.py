import csv
import random
from random import shuffle
from random import randrange
import sys



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
	c=0
	
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

thresh=0.6
n_epochs=10
alpha=0.01

def train(train):
	global n_epochs,thresh,alpha
	nf=len(train[0])-1
	W=[1/(nf+1) for _ in range(nf)]
	for _ in range(n_epochs):
		for te in range(len(train)):
			sum=0
			for w,x in zip(W,train[te][:-1]):
				sum+=w*x
			pred=1 if sum>=thresh else 0
			iter_error=(train[te][-1]-pred)
			for i in range(len(train[te][:-1])):
				update=alpha*iter_error*train[te][i]
				W[i]+=update
	return W


def set_threshold(W,data):
	global thresh
	avg_sum=[]
	for i in range(len(data)):
		sum=0
		for w,x in zip(W,data[i][:-1]):
			sum+=w*x
		avg_sum.append(sum)
	a_sum=0
	c=0
	for i in range(len(data)):
		if data[i][-1]==0:
			a_sum+=avg_sum[i]
			c+=1
	thresh=a_sum/c
	

def predict(W,data):
	global thresh
	y_pred=[]
	avg_sum=[]
	for i in range(len(data)):
		sum=0
		for w,x in zip(W,data[i][:-1]):
			sum+=w*x
		avg_sum.append(sum)
		pred=1 if sum>=thresh else 0
		y_pred.append(pred)
	return y_pred,avg_sum

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for _ in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split

def confusion_matrix(y,y_pred):
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


def evaluate_algorithm(dataset, n_folds):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	f=1
	average_acc=0
    average_prec=0
    average_recall=0
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		actual=[]
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			actual.append(row[-1])
		W=train(train_set)
		predicted ,_= predict(W,test_set)
		print("FOLD ",f)
		print("predicted :",predicted)
		print("actual :",actual)
		accuracy = accuracy_metric(actual, predicted)
		precision,recall=confusion_matrix(actual,predicted)
		average_acc+=accuracy
		average_prec+=precision
		average_recall+=recall
		print("accuracy :"+str(accuracy))
		print("precision :"+str(precision))
		print("recall :"+str(recall))
		print("-"*90)
		scores.append(["accuracy :"+str(accuracy),"precision :"+str(precision),"recall :"+str(recall)])
		f+=1
	print("average accuracy :",average_acc/n_folds)
    print("average precision :",average_prec/n_folds)
    print("average recall :",average_recall/n_folds)


data=get_data("../datasets/IRIS.csv",-1)
print("For IRIS data:")
evaluate_algorithm(data,10)
print("="*90)
data=get_data("../datasets/SPECT.csv",0)
print("For SPECT data:")
evaluate_algorithm(data,10)