# -*- coding: utf-8 -*-
"""logisticRegression

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r7u1SNPuV1QSud9fKJmHKJTRv3AFk7PP
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('Social_Network_Ads.csv')

# menghapus User ID
data = df.drop(columns=['User ID'])
data = pd.get_dummies(data)

# memisahkan atribut dan label
predictions = ['Age' , 'EstimatedSalary' , 'Gender_Female' , 'Gender_Male']
X = data[predictions]
y = data['Purchased'] 

# membagi data training dan testing
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=42)

# membuat model untuk training
from sklearn import linear_model
model = linear_model.LogisticRegression()
model.fit(X_train, y_train)

# menguji akurasi model
model.score(X_test, y_test)