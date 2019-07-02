# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:43:36 2019

@author: DrTartar
"""

# Simple Linear Regression

## PART 1                      Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv') #Dosya okundu
X = dataset.iloc[:, :-1].values # Experience degerleri X (son kolan haric tum kolonlar)
y = dataset.iloc[:, 1].values # Salary degerleyi y 01 kolondan 1.kolan(yani 2.siradaki)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


## PART 2                 MODEL: SIMPLE LINEAR REGRESSION


# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## PART 3                 Predicting the Test set results
# BU DEGER y_pred, gercek sonuc olan y_test degeri ile ortusmesi gerekir.
# y_pred PREDICTED RESULTS
# y_test ACTUAL RESULTS
y_pred = regressor.predict(X_test)



## PART 4                  DATA VISUALIZATION

# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # X_train vs y_train
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue') # we need to get the same regr line and to use it.
##### plt.plot(X_test, regressor.predict(X_test), color = 'blue') # we need to get the same regr line and to use it.
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

### end  ###
