#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement
# 

# To predict the weight using KNN algorithm without the usage of any packages.

# ## Formulas used

# Euclidean distance formula-The distance two points (x1,y1) and (x2,y2) is given by the formula :
# [(x2-x1)2 +(y2-y1)2] 1/2

# ## Algorithm
# 

# Step1: Start
# 
# Step 2: Load the train data
# 
# Step 3:Load the test data
# 
# Step 4:Assign k values
# 
# Step 5:Assign target variable
# 
# Step 6:Create the variable to store the predicted targeted values
# 
# Step 7:Repeat through the steps:
# 
# - Find the difference matrix
# 
# - Compute the distance using Euclidean distance formula
# 
# - Sort the train data in ascending order w.r.t the distances
# 
# - Compute average of the first k terms of train dataset 
# 
# - Append to predicted targeted values.
# 
# Step 8: Display the predicted targeted values
# 
# Step 9: Stop

# ## Code

# In[2]:


# -*- coding: utf-8 -*-
"""
@script-author:Melisa Dalmeida
@script-description:To predict the value using knn algorithm
@script-start date:08.01.20
@script-last updated:13.01.20
"""


# In[8]:


train=[[1,2,3],[4,5,6],[7,8,9]]
test = [[1,2], [2,4]]
avg=[]
for a in range(len(test)):
    test1=[]
    k=2
    sum=0
    diff=[]
    test1.append(test[a])
    d=[]
    for row in train:
        d.append(row[:-1])
    for i in range (len(d)):
        for j in range(len(test1[0])):
            diff1=(train[i][j]-test1[0][j])**2
            sum=sum+diff1
        sqr=sum**0.5
        diff.append([sqr,train[i][2]])
    diff.sort
    sum=0
    for i in range(0,k):
        for j in range(1):
            sum=sum+diff[i][1] 
    avg1=sum/k
    avg.append(avg1)
avg


# In[ ]:




