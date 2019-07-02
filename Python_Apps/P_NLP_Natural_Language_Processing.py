# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:46:49 2019

@author: DrTartar
"""
##                                NATURAL LANGUAGE PROCESSING

# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
# Reviewler arasinda virgul(,) kullanildigindan tab ile ayrilmis veri tsv kullaniyoruz.
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)# ignore the double quoting

# Cleaning the texts
import re
import nltk
nltk.download('stopwords') # List of world indirilir yani sozluk gibi
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) # metinden kaldirilmayacaklar (harfler ve bosluk)
    review = review.lower()
    review = review.split() #Liste halinde herbir kelime ayrilir 
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    # Burasi, listede olmayan kelimeleri secer ve fiileri v1 haline donusturur.
    review = ' '.join(review) # Kelimeleri tek string yapar, bir bosluk birakarak.
    corpus.append(review) # temizlenmis data

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500) # 1565 tane farkli kelime cikti, sinirlamak icin 1500
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values # datasetin sinif verisi liked 1.kolon alindi.(Positive 1, negative 0)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

## end