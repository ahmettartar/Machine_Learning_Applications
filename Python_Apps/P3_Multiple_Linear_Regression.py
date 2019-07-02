# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:43:36 2019

@author: DrTartar
"""

# Multiple Linear Regression

## PART 1                      Data Preprocessing
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv') #Dosya okundu
X = dataset.iloc[:, :-1].values # degerleri X (son kolan haric tum kolonlar)
y = dataset.iloc[:, 4].values # degerler y 01234 kolondan (yani 4.siradaki)


## Categorical veri var. Encoding yapmaliyiz.
# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

## AVOIDNG THE DUMMY VARIABLE TRAP
X = X [:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)



## PART 2                 MODEL: MULTIPLE LINEAR REGRESSION


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

## PART 3                 Predicting the Test set results
# BU DEGER y_pred, gercek sonuc olan y_test degeri ile ortusmesi gerekir.
# y_pred PREDICTED RESULTS
# y_test ACTUAL RESULTS
y_pred = regressor.predict(X_test)


## PART 4
# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
#X= np.append (arr=X, values= np.ones((50,1)).astype(int), axis=1) or
X= np.append (arr= np.ones((50,1)).astype(int), values=X, axis=1)

X_opt= X[:, [0,1,2,3,4,5]] # tum independent variables
regressor_OLS = sm. OLS(endog=y, exog=X_opt).fit() #fit the full model with all possible predictors
regressor_OLS.summary() # tum veri bilgisi alinir

# Burada en yuksek P degerine sahip olani bulup,
# birsonrakinde onu cikariyoruz.
# constant 0, x1 x2 x3 x4 x5 seklinde burada.
#x2 cikarirsak,
'''# yeni X_opt 2.parametre olmayacaktir.
#X_opt= X[:, [0,1,3,4,5]] # tum independent variables
#regressor_OLS = sm. OLS(endog=y, exog=X_opt).fit() #fit the full model with all possible predictors
#regressor_OLS.summary() # tum veri bilgisi alinir
'''


'''###                                       AUTOMATIC BACKWARD ELEMINATION

# OPTION 1: Backward Elimination with p-values only:
import statsmodels.formula.api as sm
def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)

# OPTION 2: Backward Elimination with p-values and Adjusted R Squared:

import statsmodels.formula.api as sm
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)
'''

'''
### end  ###
