# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:46:49 2019

@author: DrTartar
"""

#                                   ASSOCIATION RULE LEARNING
#                                            APRIORI

# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# A                   Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# B                   List olustruma
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20)]) #herbir islem liste haline getirildi


# C                  Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)


# C                   Visualising the results
results = list(rules)


## end