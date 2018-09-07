import csv
import random
from random import shuffle
from random import randrange
random.seed(123)

def get_data(file,y_in,bias=False):
    reader = csv.reader(open("../datasets/"+file),delimiter=",")
    data=[]
    c=0
    for row in reader:
        if(c==0):
            c+=1
            continue
        data.append(row)
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
        y[i]=1-unique.index(y[i])
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
    prob_class={}
    summary={}
    # i=0
    tot=0
    for classes,indices in classes.items():
        temp=[{} for _ in range(n_f)]
        # print(len(indices))
        for ind in indices:
            for attr in range(n_f):
                if str(data[ind][attr]) not in temp[attr]:
                    temp[attr][str(data[ind][attr])]=1
                else:
                    temp[attr][str(data[ind][attr])]+=1
        # print(temp)
        for t in temp:
            for k,v in t.items():
                t[k]=v/len(indices)
        summary[classes]=temp
        prob_class[classes]=len(indices)/len(data)
        tot+=len(indices)
    # for k,v in prob_class.items():
    #     prob_class[k]=v/tot
    # print(prob_class)
    return summary,prob_class

def maxi(vec):
    max=-1
    for i in range(len(vec)):
        if vec[i]>max:
            max=vec[i]
            max_i=i
    return max_i

def predict(te,summary,prob_class):
    prob={}
    max=-1
    mclass=''
    for k,v in prob_class.items():
        prob[k]=v
        for attr in range(len(te)-1):
            try:
                prob[k]=prob[k]*summary[k][attr][str(te[attr])]
            except:
                pass
        if prob[k]>max:
            max=prob[k]
            mclass=k
    # print(max)
    return int(mclass)

def predict_all(data,summary,prob_class):
    pred=[]
    for te in data:
        pred.append(predict(te,summary,prob_class))
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
        summary,prob_class=get_proba(train_set)
        predicted = predict_all(test_set,summary,prob_class)
        print("FOLD ",f)
        print("predicted :",predicted)
        print("actual :",actual)
        accuracy = accuracy_metric(actual, predicted)
        precision,recall= confusion_matrix(actual,predicted)
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

    
data=get_data("SPECT.csv",0)
evaluate_algorithm(data,10)