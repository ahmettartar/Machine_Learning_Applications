# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:31:08 2019

@author: DrTartar
"""

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# A              Importing Dataset

dataset=pd.read_csv('Data.csv')

# son kolon haric bir matrix olusturalim.
X = dataset.iloc[:,:-1].values

# 0123 sutunlarda 3,sutun Class
y = dataset.iloc [:,3].values



# D                SPLITTING DATASET INTO (TRAINING SET AND TEST SET)

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split # Eski versionda cross.validation vardi.

from sklearn.model_selection import train_test_split
# datanin 20% sini test olarak aldik, gerisi 80% training set oluyor.
# ayni ramdom sayilarla islem yapmak icin random_state 0 aliyoruz.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


'''# E                     FEATURE SCALLING

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
# SADECE VERILER uzerinde scaling yapiyoruz. Class zaten kategoriyi temsil ediyor.
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)'''





















