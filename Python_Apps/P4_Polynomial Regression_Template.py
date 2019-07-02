# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:43:36 2019

@author: DrTartar
"""

# REGRESSION MODEL TEMPLATE

##                     Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv') #Dosya okundu
# X = dataset.iloc[:, 1].values # Matris yapmak icin 1:2 seklinde yaziyoruz.
# Position kismini almadik, sadece level  ind.var olarak aliyoruz.Degerler: Level ve Salary
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


##                  MODEL: REGRESSION

# Fitting Regression Model to the dataset
# Create your regressor here

#                   DEGER SORGULAMA
#predicting a new result with regression
y_pred=regressor.predict([[6.5]])


##                DATA VISUALIZATION
# Visualising the Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1) # 0.1 increment
X_grid = X_grid.reshape((len(X_grid), 1)) # matris oluyor
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
'''
### end  ###
