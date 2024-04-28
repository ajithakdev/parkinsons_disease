# -*- coding: utf-8 -*-
"""parkinson-s-disease-prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XhnJTmyoWdEwib1J456nPYeU2ov8uG9M
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

df = pd.read_csv("/content/parkinsons.csv")


df.head()

df.tail()

df.shape

df.info()

df.isnull().sum()

df.describe()

"""1--> POSITIVE
0--> NEGATIVE
"""

X = df.drop(columns=['name', 'status'], axis=1)
Y = df['status']

print(X)

print(Y)

scaler = StandardScaler()
# Fit the scaler on the training data before splitting
scaler = StandardScaler()
scaler.fit(X)  # Fit on the entire dataset before splitting

scaler.fit(X_train)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)



X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)

print(X_train)

model = svm.SVC(kernel='linear')

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)

print("Accuracy score on Training data:", training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)

print("Accuracy score on test data:", test_data_accuracy)

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)

prediction = model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")

"""Saving the trained model"""

import pickle


filename = 'trained_scaler.pkl'
pickle.dump(scaler, open(filename, 'wb')) 

filename = 'trained_model.sav'
pickle.dump(model,open(filename,'wb'))

#loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

std_data = scaler.transform(input_data_reshaped)

prediction = loaded_model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")
