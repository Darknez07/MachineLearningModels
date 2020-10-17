# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:45:39 2020

@author: rishi
"""
# Multi Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import OneHotEncoder as Ohe

One_hot = Ohe(categories='auto')


features = np.append(One_hot.fit_transform(X[:,3].reshape(-1,1)).toarray(), 
                     X[: , :3], 
                     axis = 1)

X  = np.array(features, dtype = np.float64)
# Dummy variable trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

#Fit the model right here
from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train, y_train)

#Predicting on the trained model

y_pred = regressor.predict(X_test)

plt.subplots(nrows=2,ncols=1)
plt.plot(y_test,'k.')
plt.plot(y_pred,'r.')
# plt.figure(X_train,y_pred)

#Building a forward eliminati0on 
# New documentation says this is good

import statsmodels.regression.linear_model as smf
# This is the intial b0
# Which is added to y = b0+b1*x1.....
X = np.append(arr = np.ones((X.shape[0],1),dtype=int), values = X, axis=1)
# Highest p value among the collection of predictors
# Optimal features which are neccessary that is p values less than p0 i.e. 0.05
# Hence LOS is 5%

index_arr = [0, 1, 2, 3, 4, 5]

X_opt = X[:, index_arr]

#New Regressor for changing it ever time
# This is fitting of the the model
regressor_ols = smf.OLS(endog = y,exog = X_opt).fit()

# Check for highest P values

# Calculates the regressor for the minimum P value
# Hence finding the most statistically significant variable

for i in range(5):
  if float(regressor_ols.pvalues.max()) > 0.05:
    del index_arr[np.argmax(regressor_ols.pvalues)]
    X_opt = X[:, index_arr]
    regressor_ols = smf.OLS(endog= y, exog=X_opt).fit()
  else:
    break

regressor_ols.summary()

