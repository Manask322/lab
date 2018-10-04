import random
from random import randrange
import csv

k=5
n_classes=2
def find_class(train,test):
    global k,n_classes
    distances=[]
    for i in range(len(train)):
        dist=0
        for x1,x2 in zip(train[i][:-1],test):
            dist+=(x2-x1)**2
        distances.append([dist,train[i][-1]])
    distances=sorted(distances,key=lambda x:x[0])
    classes=[0 for _ in range(n_classes)]
    max=0
    for i in range(k):
        classes[distances[i][1]]+=1
        if classes[distances[i][1]]>max:
            max=classes[distances[i][1]]
            cl=distances[i][1]
    return cl

def get_data(file,y_in,flag=0,bias=False):
    reader = csv.reader(open("../datasets/"+file),delimiter=",")
    data=[]
    c=0
    for row in reader:
        if(c==0):
            c+=1
            continue
        data.append(row)
    random.seed(123)
    # shuffle(data)
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
        if flag:
            y[i]=1-unique.index(y[i])
        else :
            y[i]=unique.index(y[i])
    for i in range(len(X)):
        for j in range(len(X[0])):
            X[i][j]=float(X[i][j])
    if bias:
        for i in range(len(X)):
            X[i]=[1]+X[i]
    data=[]
    for i in range(len(X)):
        data.append(X[i]+[y[i]])
    return data

def predict(train_set,test_set):
    pred=[]
    for te in test_set:
        pred.append(find_class(train_set,te))
    return pred
    

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

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

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
		predicted = predict(train_set,test_set)
		print("FOLD ",f)
		print("predicted :",predicted)
		print("actual    :",actual)
		accuracy = accuracy_metric(actual, predicted)
		precision,recall=confusion_matrix(actual,predicted)
		average_acc+=accuracy
		average_prec+=precision
		average_recall+=recall
		print("accuracy  : "+str(accuracy))
		print("precision : "+str(precision))
		print("recall :"+str(recall))
		print("-"*90)
		scores.append(["accuracy :"+str(accuracy),"precision :"+str(precision),"recall :"+str(recall)])
		f+=1
	print("average accuracy :",average_acc/n_folds)
	print("average precision :",average_prec/n_folds)
	print("average recall :",average_recall/n_folds)

data=get_data("IRIS.csv",-1)
evaluate_algorithm(data,10)