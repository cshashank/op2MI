import sklearn as sklearn
import numpy as numpy
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
X_iris,y_iris = iris.data,iris.target
print (X_iris.shape,y_iris.shape)
print (X_iris[0],y_iris[0])
print (iris.target_names)