from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import sklearn as sklearn
import numpy as numpy
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
x_iris,y_iris = iris.data,iris.target
print (x_iris.shape,y_iris.shape)
print (x_iris[0],y_iris[0])
print (iris.target_names)
# Get dataset with only the first two attributes
x,y = x_iris[:,:2],y_iris
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=33)
print (x_train.shape,y_train.shape)
#Standardize the features
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)