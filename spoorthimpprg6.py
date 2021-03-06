# -*- coding: utf-8 -*-
"""spoorthimpPrg6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EAdmgizTcXh_rDOp-da3n16HzA4ylE08
"""

import pandas as pd 
import pylab as pl 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn import tree,metrics,model_selection,preprocessing
from sklearn.neighbors import KNeighborsClassifier
df=pd.read_csv('iris.csv') 
y=df.iloc[:,-1].values 
x=df.iloc[:,0:4].values 
x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.2) 
classifier=KNeighborsClassifier(n_neighbors=3) 
classifier.fit(x_train,y_train) 
y_predict=classifier.predict(x_test) 
accuracy=metrics.accuracy_score(y_test,y_predict)
print('the accuracy is:',accuracy)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_predict))