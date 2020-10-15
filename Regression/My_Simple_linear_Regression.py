# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:40:02 2020

@author: rishi
"""

# y = b0 + b1*x => Simple linear regression equation
# b0 is bais and b1 is cofficient for unit 
# Implementing the model

# Step:-1 Preprocessing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Step:-2 Splitting the data

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Step:-3 Training the model

# Fitting the dataset as per the requirements
# Most simple or noob model
from sklearn.linear_model import LinearRegression as Lr
regressor = Lr()
regressor.fit(X_train, y_train)

# Step:-4   Predicting the data
y_pred = regressor.predict(X_test)

# Step:-5 Visualizing the dataset

#Train set
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary Vs Experience(Training Set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

#Test set
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary Vs Experience(Testing Set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()

# new_pred = regressor.predict(np.array([[1.3],[2.4]]))


