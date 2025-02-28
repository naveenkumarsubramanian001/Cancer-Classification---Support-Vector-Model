# -*- coding: utf-8 -*-
"""Cancer Classification - Support Vector Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12ageZDoJqYwkxEZR7Zi81B_CUyyP9hOs
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

cancer_data= pd.read_csv('/content/Cancer_Data.csv')
cancer_data.head()

cancer_data.shape

cancer_data.isnull().sum()

cancer_data['diagnosis'].value_counts()

cancer_data.describe()

x=cancer_data.drop(['diagnosis','Unnamed: 32'],axis=1)
y=cancer_data['diagnosis']

print(x)

print(y)

scaler = StandardScaler()

scaler.fit(x)
stand_data = scaler.transform(x)

standardise_data = pd.DataFrame(stand_data,columns=x.columns)

standardise_data.describe()

X = standardise_data
Y = y

X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y)

print (X.shape, X_train.shape , Y_train.shape)

model = svm.SVC(kernel='linear')

model.fit(X_train,Y_train)

x_pred = model.predict(X_train)

acc_score = accuracy_score(x_pred,Y_train)

print(acc_score)

x_test_pred = model.predict(X_test)
accc_score = accuracy_score(x_test_pred,Y_test)
print(accc_score)

input = (8610908,12.86,18,83.19,506.3,0.09934,0.09546,0.03889,0.02315,0.1718,0.05997,0.2655,1.095,1.778,20.35,0.005293,0.01661,0.02071,0.008179,0.01748,0.002848,14.24,24.82,91.88,622.1,0.1289,0.2141,0.1731,0.07926,0.2779,0.07918)
input_data = np.asarray(input)
input_data = input_data.reshape(1,-1)
prediction = model.predict(input_data)
print(prediction)
if (prediction == 'M'):
  print('The tumor is Malignant')
else:
  print('The tumor is Benign')

