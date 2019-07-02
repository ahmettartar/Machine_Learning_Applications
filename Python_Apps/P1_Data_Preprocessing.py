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


#B                Missing Data           ############################3

from sklearn.preprocessing import Imputer # Gerekli toolu aldik

# Nan Degerleri tespit ediliyor, mean degeri ile degistiriliyor 
## STRATEGY : mean, median ve most_frequent UC FARKLI DEGER ALABILIR

imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) # 0 for columns/features 1 for rows

# bu nesne ile X matrisini sekillendiriyoruz. Hala ilk tablonun index degerleri ile isliyor.
imputer = imputer.fit(X[:, 1:3])

# Tekrar gercek matrise bu degerleri yukluyoruz.
X[:, 1:3] = imputer.transform(X[:, 1:3])


#C                Encoding categorical data

# Encoding the Independent Variable
# datasetteki verileri isleyebilmek icin numeric olmayan degeleri numeric hale cevirmemiz lazim.
# bu sekilde categorik verileri sayisal ifade etmis oluruz.

# Datasetteki ulke adlarini encoding yapalim
# ulkeleri numaralandirmis olduk.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) # ulke kolonunu aldik.

# Ulkeleri kategorilestirdikten sonra
# onlarin hepsini ayri bir sutunda 010 seklinde hangisine uygunsa 1, digerleri 0 olarak temsil edlilir

onehotencoder = OneHotEncoder(categorical_features = [0])# o veya all degerler 
X = onehotencoder.fit_transform(X).toarray()

# y degerleri de non-numeric oldugundan onun icinde numeric encoding yapiyoruz.
# yes ve nolari 0 ve 1 olarak gostermis olduk.
# Encoding the Dependent Variable or Class
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# D                SPLITTING DATASET INTO (TRAINING SET AND TEST SET)

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split # Eski versionda cross.validation vardi.

from sklearn.model_selection import train_test_split
# datanin 20% sini test olarak aldik, gerisi 80% training set oluyor.
# ayni ramdom sayilarla islem yapmak icin random_state 0 aliyoruz.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# E                     FEATURE SCALLING

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
# SADECE VERILER uzerinde scaling yapiyoruz. Class zaten kategoriyi temsil ediyor.
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)





















