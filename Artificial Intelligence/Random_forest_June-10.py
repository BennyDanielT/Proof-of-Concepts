# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 09:35:39 2019

@author: kgcg148
"""

from sklearn import metrics
import pandas as pd
import numpy as np
#import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
#import matplotlib.pyplot as plt

#np.set_printoptions(threshold=sys.maxsize)

data=pd.read_csv("C:\\Users\\kgcg148\\Desktop\\HACKIT-2K19\\COMM_HKTHN_'19\\Sales_Data_2016-19_Vol.csv")

#data=ds.sample(frac=1) #Used to scramble/shuffle the data
data=data.drop(['txn_date_sk','txn_dt','sls_tm_sk'],axis=1)
print("\033[1;32;40m Bright Green  \nData-Head\n",data.head())
X = data.iloc[:, 0:3].values
print("Input Columns Without Transformations\n",X)
labelencoder_X = LabelEncoder()
X[:,0] = labelencoder_X.fit_transform(X[:,0]) #L I have Label encoded the Terr_pos_sks here
X[:,1] = labelencoder_X.fit_transform(X[:,1]) #L I have Label encoded the brands here
print("Input Columns after label Encoding",X)
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray()
#print("Input Columns after Onehot Encoding",X)

#print("Let's have a peek at the data\n",data.head())
yaxis=data['volume']
#print("Y-AXIS.head\n",yaxis.head())

'''plt.hist(yaxis, bins=100)
plt.ylabel('Frequency')
plt.show()'''
print(X[X.columns[0:]].corr()['volume'][:])
#df[['Income', 'Education', 'LoanAmount']].corr()['LoanAmount'][:]

Y=pd.cut(yaxis,bins=500,labels=np.arange(500))
Bins=pd.cut(yaxis,bins=500,retbins=True)
print("Y-bins\t Bin Intervals\n")
print("Volume-BINS\n",Y)
print("Bin Intervals",Bins)
print("Max-Volume:",yaxis.max())
("Min-Volume:",yaxis.min())
print("Avg-Volume:",yaxis.mean())

xaxis_train, xaxis_test, yaxis_train, yaxis_test =train_test_split(X, Y, test_size = 0.2 , random_state = 5,shuffle=False)
model=RandomForestClassifier(n_estimators=100)
model.fit(xaxis_train,yaxis_train)
prediction=model.predict(xaxis_test)
print("Actual",yaxis_test)
print("/t Predicted",prediction)
# predict for the test data
#prediction will contain the predicted value by our model predicted values of diagnosis column for test inputs
print("Accuracy: ",metrics.accuracy_score(prediction,yaxis_test)*100,"%")  # to check the accuracy
# here we will use accuracy measurement between our predicted value and our test output values'''

'''print("I/p test values:\n",xaxis_test)
print("O/p test values:\n",prediction)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):
print("Expected test values:\n",yaxis_test)

df=pd.DataFrame(xaxis_test)
df.to_csv('Pred_output.csv')'''