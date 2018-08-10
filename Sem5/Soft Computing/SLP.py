import csv
reader = csv.reader(open("IRIS.csv"),delimiter=",")
from random import shuffle
data=[]
c=0
for row in reader:
	if(c==0):
		c+=1
		continue
	data.append(row)
shuffle(data)
X=[]
y=[]
c=0
for row in data:
	if(c==0):
		c+=1
		continue
	X.append(row[:-1])
	y.append(row[-1])
#print(X)
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
#print(X)
nf=len(X)
W=[1/(nf+1) for _ in range(nf)]
#W=[1]+W
n_epochs=20
y_pred=[0 for i in range(len(y))]
X_train=X[:90]
X_test=X[90:]
y_train=y[:90]
y_test=y[90:]
thresh=0
alpha=0.01
#update=[[0] for _ in range(W)]
for e in range(n_epochs):
	for te in range(len(X_train)):
		sum=0
		for w,x in zip(W,X_train[te]):
			sum+=w*x
		y_pred[te]=1 if sum>thresh else 0
	for i in range(len(W)):
		update=alpha*(y_pred[te]-y[te])*X[te][i]
		W[i]+=update
print(y_pred)
