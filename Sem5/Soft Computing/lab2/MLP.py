import csv
import random
from random import shuffle
from math import exp
from random import randrange
import numpy as np
import pandas as pd



def layer_sizes(X, Y):
    n_x =X.shape[0]
    n_h = 5
    n_y = Y.shape[0] 
    return (n_x, n_h, n_y)


def initialize_parameters(n_x, n_h, n_y):
    np.random.seed(2)
    W1 = np.random.randn(n_h,n_x)*0.01
    b1 = np.zeros((n_h,1))
    W2 = np.random.randn(n_y,n_h)*0.01
    b2 = np.zeros((n_y,1))
    assert (W1.shape == (n_h, n_x))
    assert (b1.shape == (n_h, 1))
    assert (W2.shape == (n_y, n_h))
    assert (b2.shape == (n_y, 1))
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    return parameters

def sigmoid(X):
    return 1/(1+np.exp(-X))

def forward_propagation(X, parameters):
    W1 = parameters["W1"]
    b1 = parameters["b1"]
    W2 = parameters["W2"]
    b2 = parameters["b2"]
   
    Z1 = np.dot(W1,X)+b1

    A1 = np.tanh(Z1)
    Z2 = np.dot(W2,A1)+b2
    A2 = sigmoid(Z2)
    # print(A2.shape)
    assert(A2.shape == (1, X.shape[1]))
    
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    
    return A2, cache

def compute_cost(A2, Y, parameters):
    m = Y.shape[1] 
    logprobs = np.multiply(np.log(A2),Y)+np.multiply(np.log(1-A2),1-Y)
    cost = -1*np.sum(logprobs)/m
    cost = np.squeeze(cost)    
    return cost

def backward_propagation(parameters, cache, X, Y):
    m = X.shape[1]
    W2 = parameters["W2"]
    A1 = cache["A1"]
    A2 = cache["A2"]
   
    dZ2 = A2-Y
    dW2 = np.dot(dZ2,A1.T)/m
    db2 = np.sum(dZ2,axis=1,keepdims=True)/m
    dZ1 = np.dot(W2.T,dZ2)*(1-np.power(A1,2))
    dW1 = np.dot(dZ1,X.T)/m
    db1 = np.sum(dZ1,axis=1,keepdims=True)/m
    
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    
    return grads

def update_parameters(parameters, grads, learning_rate = 1.2):

    W1 = parameters["W1"]
    b1 = parameters["b1"]
    b2=parameters["b2"]
    W2 = parameters["W2"]
    
    dW1 = grads["dW1"]
    db1 = grads["db1"]
    dW2 = grads["dW2"]
    db2 = grads["db2"]
    
    W1 = W1-learning_rate*dW1
    b1 = b1-learning_rate*db1
    W2 = W2-learning_rate*dW2
    b2 = b2-learning_rate*db2
   
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters

def nn_model(X, Y, n_h, num_iterations = 10000, print_cost=True):
    np.random.seed(3)
    # print(X.shape)
    n_x = layer_sizes(X, Y)[0]
    n_y = layer_sizes(X, Y)[2]
 
    parameters = initialize_parameters(n_x,n_h,n_y)
  
    for i in range(0, num_iterations):
        A2, cache = forward_propagation(X,parameters)
        cost = compute_cost(A2,Y,parameters)
 
        grads = backward_propagation(parameters,cache,X,Y)
 
        parameters = update_parameters(parameters,grads)
        
        # Print the cost every 1000 iterations
        if print_cost and i % 1000 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))
    return parameters

def predict(parameters, X): 
    A2,_ = forward_propagation(X,parameters)
    predictions=[1 if A2[0][i]>0.5 else 0   for i in range(A2.shape[1])] 
    return predictions

data=pd.read_csv("../datasets/SPECT.csv",delimiter=",")

data = data.sample(frac=1,random_state=123).reset_index(drop=True)

X=data.drop(['Class'],axis=1)
y=data['Class'].replace(['Yes','No'],[1,0])
m=X.shape[0]
test_size=int(0.7*m)
X_train=X[:test_size]
y_train=y[:test_size]
X_test=X[test_size:]
y_test=y[test_size:]
X_train=np.array(X_train).T
y_train=np.array(y_train).reshape(1,y_train.shape[0])
X_test=np.array(X_test).T
y_test=np.array(y_test).reshape(1,y_test.shape[0])

parameters=nn_model(X_train,y_train,5)
pred=predict(parameters,X_test)

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

# print(list(pred))
print(accuracy_metric(y_test.reshape(-1,1),pred))
print(confusion_matrix(y_test.reshape(-1,1),pred))
