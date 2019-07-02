# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:43:36 2019

@author: DrTartar
"""

#              RANDOM FOREST REGRESSION

##                     Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv') #Dosya okundu
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2:3].values #matrix icin 3 koyduk

# Feature Scaling
'''# Training ve test setlerimiz yok.
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)'''


##                  MODEL: RANDOM FOREST REGRESSION

# Fitting RANDOM FOREST REG to the dataset
# Create your regressor here
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100, random_state = 0) # 10 veya 100 300
regressor.fit (X, y)


#                   DEGER SORGULAMA
#predicting a new result with regression

y_pred=regressor.predict([[6.5]])


##                DATA VISUALIZATION

# Yapi non-continous oldugundan linearlik uygun olmuyor.
# Visualising the RANDOM FOREST results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.01) # 0.1 increment
X_grid = X_grid.reshape((len(X_grid), 1)) # matris oluyor
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or Bluff (RANDOM FOREST Reg Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

'''# Visualising the Decision Tree Reg results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Decision Tree Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()'''
### end  ###