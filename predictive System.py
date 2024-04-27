# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Lenovo/Downloads/MainProject/trained_model.sav', 'rb'))


input_data = (197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# Define and fit a StandardScaler
scaler = StandardScaler()
scaler.fit(input_data_reshaped)

std_data = scaler.transform(input_data_reshaped)

prediction = loaded_model.predict(std_data)
print(prediction)


if (prediction[0] == 0):
  print("The Person does not have Parkinsons Disease")

else:
  print("The Person has Parkinsons")
  
  """

import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Lenovo/Downloads/MainProject/trained_model.sav', 'rb'))

# Define the input data
input_data = np.array([197.07600,206.89600,192.05500,0.00289,0.00001,0.00166,0.00168,0.00498,0.01098,0.09700,0.00563,0.00680,0.00802,0.01689,0.00339,26.77500,0.422229,0.741367,-7.348300,0.177551,1.743867,0.085569])

# Reshape the input data
input_data_reshaped = input_data.reshape(1, -1)

# Define and fit a StandardScaler on the input data
scaler = StandardScaler()
scaler.fit(input_data_reshaped)

# Transform the input data
std_data = scaler.transform(input_data_reshaped)

# Make a prediction using the loaded model and the scaled input data
prediction = loaded_model.predict(std_data)
print(prediction)

if prediction[0] == 0:
    print("The Person does not have Parkinson's Disease")
else:
    print("The Person has Parkinson's")
