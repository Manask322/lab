import csv
reader = csv.reader(open("IRIS.csv"),delimiter=",")
import random
from random import shuffle
from math import exp
data=[]
c=0
for row in reader:
	if(c==0):
		c+=1
		continue
	data.append(row)
random.seed(123)
shuffle(data)

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


thresh=0.5
n_epochs=100
alpha=0.01
X_train=X[:90]
X_test=X[90:]
y_train=y[:90]
y_test=y[90:]


def train(X_train,y_train):
	global n_epochs,thresh,alpha
	nf=len(X[0])
	W=[1/(nf+1) for _ in range(nf)]
	prev=0
	mse=999
	while (abs(prev-mse) > 0.002):
		error=0
		for te in range(len(X_train)):
			sum=0
			for w,x in zip(W,X_train[te]):
				sum+=w*x
			pred=1 if 1/(1+exp(-sum))>thresh else 0
			iter_error=(pred-y_train[te])
			error+=abs(iter_error)
			for i in range(len(X_train[te])):
				update=alpha*iter_error*X[te][i]
				W[i]+=update
		prev=mse
		mse = float(error/len(X_train))
	return W

def set_threshold(W,data,y_train):
	global thresh
	avg_sum=[]
	for i in range(len(data)):
		sum=0
		for w,x in zip(W,data[i]):
			sum+=w*x
		avg_sum.append(sum)
	a_sum=0
	c=0
	for i in range(len(y_train)):
		if y_train[i]==0:
			a_sum+=avg_sum[i]
			c+=1
	thresh=a_sum/c

def predict(W,data):
	global thresh
	y_pred=[]
	avg_sum=[]
	for i in range(len(data)):
		sum=0
		for w,x in zip(W,data[i]):
			sum+=w*x
		avg_sum.append(sum)
		pred=1 if sum>thresh else 0
		y_pred.append(pred)
	return y_pred,avg_sum

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0


W=train(X_train,y_train)

# set_threshold(W,X_train,y_train)

y_pred,avg_sum=predict(W,X_train)


print("Train accuaracy: ",accuracy_metric(y_train,y_pred))

y_pred_test,_=predict(W,X_test)

print("Test accuracy : ",accuracy_metric(y_test,y_pred_test))
