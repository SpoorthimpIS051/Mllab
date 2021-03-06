# -*- coding: utf-8 -*-
"""Spoorthimpprg4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/194NgFkPNf5lu5PPNL-mQn79rRr9u1XZI
"""

import matplotlib.pyplot as plt 

import pandas as pd 

import pylab as pl 

import numpy as np 

from sklearn import linear_model,metrics

from sklearn.metrics import mean_absolute_error



 
df = pd.read_csv("FuelConsumption.csv") 

df.head() 

 

cdf  =  df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB','CO2EMISSIONS']] 

cdf 

 

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS) 

plt.xlabel("ENGINESIZE") 

plt.ylabel("CO2EMISSIONS") 

plt.show() 

 
 

 

 
msk = np.random.rand(len(df)) < 0.8 

train = cdf[msk] 

test =  cdf[~msk] 

plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS) 
plt.xlabel("ENGINESIZE") 

plt.ylabel("CO2EMISSIONS") 

plt.show() 


 

reg = linear_model.LinearRegression() 

x = np.asanyarray(train[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB']]) 

y = np.asanyarray(train[['CO2EMISSIONS']]) 

reg.fit(x, y) 

 
 

print('Coefficients of the model:', reg.coef_) 

 
y_pred = reg.predict(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB']]) 

x_test= np.asanyarray(test[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_CITY','FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB']]) 

y_test = np.asanyarray(test[['CO2EMISSIONS']]) 

print('Intercept is:',reg.intercept_)

plt.scatter(y_test,y_pred)

b=mean_absolute_error(y_test,y_pred)
print('Mean absolute Error:',b)


print('Accuracy score: %2f'% reg.score(x_test,y_test))