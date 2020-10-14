# Certain Updates were done on date 12 Feb 2020
#Data Preprocessing
#Import libraries
  
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('Data.csv')
features = dataset.iloc[:,:-1].values
result = dataset.iloc[:,3].values

# Imputer is sklearn inbuilt lib to preprocess data

from sklearn.impute import SimpleImputer as Im
imputer = Im(missing_values=np.nan, strategy="mean")

# Here we can choose the missing values as 0 or  any other
# Simply we can use mode or median for filling

imputer = imputer.fit(features[:,1:3])

#Here we fit the Imputer the preprocessor to data which is
#Valid

features[:,1:3] = imputer.transform(features[:,1:3])

#Transform helps to apply the transformation

from sklearn.preprocessing import LabelEncoder as lb

#Here its a counting function to repress the same data
#Hence by giving numbers i.e. meaning to the data

le_x = lb()
# features[:,0] = le_x.fit_transform(features[:,0])

#We fit it to the first column as it is a string data
#And mathematics(stats) only understand numbers

from sklearn.preprocessing import OneHotEncoder as Ohe

#Now to prevent a heirarchy by labelencoder we introduced 
#refine version i.e.  to distribute each label encoded
#As independent feature preventing catogrizing(segragation)

One_hot = Ohe(categories='auto')

#Only done to first column

f =  One_hot.fit_transform(features[:,0].reshape(-1,1)).toarray()
# With new update now it automatically does it's label encoding
# So I had to find a way around
features = np.append(f, features[: , 1:3], axis = 1)
result = le_x.fit_transform(result)

#Here result is fitted to have numbers i.e. N0->0 and
#Yes->1

# Here we expirement with spliting the data for test and train
# So please see that accuracy is maintained

# Splitting the dataset
# new one has test and train lib in model selection
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(features , result,test_size = 0.2, random_state = 42)

#This is what is called scaling
# It is of two types normalization and standarization
# Well we can see that stdn = (x - max(x))/std(x) 
# while nmz = (x- min(x))/(max(x)-min(x))

from sklearn.preprocessing import StandardScaler as Sc

# IF some algos are not scaled it will run forever
# Scaling testing and training sets on same basis to aviod
# Mismatch
# Only huge output values need feature scaling
Sc_x = Sc()
X_train = Sc_x.fit_transform(X_train)
X_test = Sc_x.transform(X_test)

