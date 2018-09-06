import csv
import random
from random import shuffle
from random import randrange

def get_data(file,y_in,bias=False):
    reader = csv.reader(open("../datasets/"+file),delimiter=",")
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
    if bias:
        for i in range(len(X)):
            X[i]=[1]+X[i]
    data=[]
    for i in range(len(X)):
        data.append(X[i]+[y[i]])
    return data



def seperate_classes(data):
    classes={}
    for i in range(len(data)):
        if str(data[i][-1]) not in classes:
            classes[str(data[i][-1])]=[]
        classes[str(data[i][-1])].append(i)
    return classes


def attribute_proba(classes,data):
    n_f=len(data[0])-1
    summary={}
    for classes,indices in classes.items():
        temp=[{} for _ in range(n_f)]
        for ind in indices:
            for attr in range(n_f):
                if str(data[ind][attr]) not in temp[attr]:
                    temp[attr][str(data[ind][attr])]=1
                else:
                    temp[attr][str(data[ind][attr])]+=1
        for t in temp:
            for k,v in t.items():
                t[k]=v/len(indices)
        summary[classes]=temp
    return summary

def maxi(vec):
    max=-1
    for i in range(len(vec)):
        if vec[i]>max:
            max=vec[i]
            max_i=i
    return max_i

def predict(te,summary):
    prob=[1 for _ in range(len(summary))]
    max=-1
    for i in range(len(prob)):
        for attr in range(len(te)-1):
            try:
                prob[i]*=summary[str(i)][attr][str(te[attr])]
            except:
                pass
        if prob[i]>max:
            max=prob[i]
            maxi=i
    return maxi

def predict_all(data,summary):
    pred=[]
    for te in data:
        pred.append(predict(te,summary))
    return pred

def get_proba(data):
    classes=seperate_classes(data)
    return attribute_proba(classes,data)

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

def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0

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
    # print(len(dataset))
    f=1
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
        # print(train_set)
        summary=get_proba(train_set)
        # print(summary)
        # print(len(test_set[0]))
        predicted = predict_all(test_set,summary)
        print("FOLD ",f)
        print("predicted :",predicted)
        print("actual :",actual)
        accuracy = accuracy_metric(actual, predicted)
        precision,recall= confusion_matrix(actual,predicted)
        print("accuracy :"+str(accuracy))
        print("precision :"+str(precision))
        print("recall :"+str(recall))
        print("-"*90)
        scores.append(["accuracy :"+str(accuracy),"precision :"+str(precision),"recall :"+str(recall)])
        f+=1
    
data=get_data("SPECT.csv",0)
evaluate_algorithm(data,20)