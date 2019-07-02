# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:35:23 2019

@author: DrTartar
"""

# RANDOM FOREST ORNEK
# COLAB ta cozumu yapilmistir

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline -COLAB CODE

#data = pd.read_csv('https://raw.githubusercontent.com/HakkiKaanSimsek/Makine_Ogrenmesi_Dersleri/master/5.rassal_orman/ml_5a_regresyon/data/housing.csv')
data = pd.read_csv('Social_Network_Ads.csv')

data.info()
data.head()

# Modelimizdeki hedef değişken ‘median_house_value’ olduğu için onun
# dağılımına bakıyoruz ve veri setinin geri kalanından ayırıyoruz.
plt.figure(figsize=(12,8))
'''X = data.drop(['USER ID'], axis=1)
y = data['Purchased']'''
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values
sns.distplot(y)
plt.show()

'''Makine öğrenmesi modelleri kategorik değişkenleri algılayamadığı 
#için ‘object’ tipindeki değişkenleri one-hot-encoding yöntemiyle 0 ve 1'lere
# ayırıyoruz. Ayrıca ‘total_bedroom’ değişkenindeki eksik değerleri
# doldurmamız gerekiyor.
''
Yapmamız gerekenler sırasıyla şöyle:

    ocean_proximity değişkeni pd.get_dummies() fonksiyonuyla zenginleştirilir.
    Bu değişken veri setinden atılır.
    total_bedroom değişkeni yine o sütunun median() değeriyle doldurulur.'''
'''   
X = pd.concat([X, pd.get_dummies(X.ocean_proximity)], axis=1)
X = X.drop(['ocean_proximity'],axis=1)
X['total_bedrooms'] = X['total_bedrooms'].fillna(X['total_bedrooms'].median())

'''
'''
Modelimizi kurmaya hazırız şimdi standart modelleme süreçlerini uygulayacağız.

Veriyi eğitim ve test alt-veri setlerine ayırma.
Karar ağacı modeli oluşturma.
Modeli eğitim verisine ‘fit’ etme.'''
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
rf = RandomForestRegressor(n_estimators=100, max_depth = 3, random_state=42)
rf.fit(X_train, y_train)

'''
Gerçek değerle tahmin arasındaki benzerliğe göre mean absolute error, 
mean squared error ve root mean squared error hesaplama.'''

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(rf.predict(X_test), y_test)
mse = mean_squared_error(rf.predict(X_test), y_test)
rmse = np.sqrt(mse)

print('Mean Absolute Error (MAE): %.2f' % mae)
print('Mean Squared Error (MSE): %.2f' % mse)
print('Root Mean Squared Error (RMSE): %.2f' % rmse)

# Rastgele ormandan bir karar ağacı çekip görselleştirme.

from ipywidgets import Image
from io import StringIO
import pydotplus
from sklearn.tree import export_graphviz

d_tree99 = rf.estimators_[99]
dot_data = StringIO()
export_graphviz(d_tree99, feature_names = X.columns,
               out_file = dot_data, filled = True, rounded=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(value = graph.create_png())

#7 Sınıflandırma modeli kurulurken yapılan öznitelik 
#önem sıralamasını görselleştirme.

'''Burada derinliği 8 olan yeni bir model kurup o modelin başarı 
oranına bakıyoruz ve öznitelik sıralamasını görselleştiriyoruz.'''
rf = RandomForestRegressor(n_estimators=100, max_depth = 8, random_state=0)
rf.fit(X_train, y_train)

mae = mean_absolute_error(rf.predict(X_test), y_test)
mse = mean_squared_error(rf.predict(X_test), y_test)
rmse = np.sqrt(mse)

print('Mean Absolute Error (MAE): %.2f' % mae)
print('Mean Squared Error (MSE): %.2f' % mse)
print('Root Mean Squared Error (RMSE): %.2f' % rmse)

plt.figure(figsize=(16, 9))

ranking = rf.feature_importances_
features = np.argsort(ranking)[::-1][:10]
columns = X.columns

plt.title("Feature importances based on Random Forest Regressor", y = 1.03, size = 18)
plt.bar(range(len(features)), ranking[features], color="aqua", align="center")
plt.xticks(range(len(features)), columns[features], rotation=80)
plt.show()



################   END    #####################################

#### and
'''
Gerçek değerle tahmin arasındaki benzerliğe göre confusion matrix bulma.


predictions = d_tree1.predict(X_test)
score = round(accuracy_score(y_test, predictions), 3)
cm1 = cm(y_test, predictions)
sns.heatmap(cm1, annot=True, fmt=".0f")
plt.xlabel('Predicted Values')
plt.ylabel('Actual Values')
plt.title('Accuracy Score: {0}'.format(score), size = 15)
plt.show()

Precision, recall, f1-score değerlerini bulma.


from sklearn.metrics import classification_report
print(classification_report(y_test, predictions, target_names=['<=50K', '>50K']))


'''






