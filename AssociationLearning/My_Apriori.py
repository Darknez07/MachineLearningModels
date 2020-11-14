#!/usr/bin/env python
# coding: utf-8

# # Apriori

# In[8]:


# !pip install efficient-apriori


# ## Importing the libraries

# In[75]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ## Data Preprocessing

# In[76]:


dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
dataset = dataset.fillna(0)
data = []
for i in range(dataset.shape[0]):
    data.append([])
    for item  in dataset.iloc[i,:]:
        if item != 0:
            data[i].append(str(item))
    data[i] = tuple(data[i])


# ## Training the Apriori model on the dataset

# In[77]:


from efficient_apriori import apriori
itemset, rules = apriori(transactions=data, min_support=0.0028,
                         min_confidence = 0.2,max_length= 3)


# # Making a result matrix

# In[78]:


result = []
for row in rules:
    result.append([row.lhs, row.rhs, row.confidence, row.support, row.lift])


# ### Data frame of Result Matrix

# In[79]:


rulesresult = pd.DataFrame(data= result, columns=['lhs', 'rhs', 'conf', 'support', 'lift'])


# ### Display first 10 of dataframe

# In[80]:


rulesresult.head(10)


# ### Displaying the results non sorted

# In[81]:


rulesresult


# ### Displaying the results sorted by descending lifts

# In[94]:


rulesresult.sort_values('lift',ascending=False).head(10)

