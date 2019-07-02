# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:43:36 2019

@author: DrTartar
"""

# POLYNOMIAL REGRESSION

## PART 1                      Data Preprocessing
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

'''
Veri az oldugu icin bolmeye gerek duymadik.
Ayrica, verideki bilgiler bolundugu zaman, bilgi kaybi olmus oluyor. 
Daha sonra predict etmek cok zor.

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
'''


## PART 2                 MODEL: POLYNOMIAL REGRESSION

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4) # DEFAULT DEGER 2dir
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


## PART 3                 DATA VISUALIZATION

# Visualising the Linear Regression results
plt.scatter(X, y, color = 'red') # actual values
plt.plot(X, lin_reg.predict(X), color = 'blue') # predicted
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising the Polynomial Regression results (for higher resolution and smoother curve)
X_grid = np.arange(min(X), max(X), 0.1) # 0.1 increment
X_grid = X_grid.reshape((len(X_grid), 1)) # matris oluyor
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# PART 4                        DEGER SORGULAMA
# Grafiklerden yararlanarak istenilen bir deger icin predick degeri alalim.
# Predicting a new result with Linear Regression
lin_reg.predict([[6.5]])
#lin_reg.predict(6.5)
# Predicting a new result with Polynomial Regression
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))


'''
### end  ###
