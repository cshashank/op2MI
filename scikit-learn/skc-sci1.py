from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import sklearn as sklearn
import numpy as numpy
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

iris = datasets.load_iris()
X_iris,y_iris = iris.data,iris.target
# print (X_iris.shape,y_iris.shape)
# print (X_iris[0],y_iris[0])
# print (iris.target_names)
# Get dataset with only the first two attributesclear
x,y = X_iris[:,:2],y_iris
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=33)
# print (X_train.shape,y_train.shape)
#Standardize the features
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
colors = ['red','greenyellow','blue']
for i in range(len(colors)):
    xs = X_train[:,0][y_train == i]
    ys = X_train[:,1][y_train == i]
    # print(xs,ys,i)
    plt.scatter(xs,ys,c=colors[i])
plt.legend(iris.target_names)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
# plt.show()
clf = SGDClassifier()
clf.fit(X_train,y_train)
print (clf.coef_)
print(clf.intercept_)
