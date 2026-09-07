#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np  
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score 
# df=pd.read_csv ('data.csv') 
data = load_iris() 
X = data.data 
y= data.target
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
k=3 
knn = KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test) 
accuracy = accuracy_score(y_test,y_pred) 
print(f'Accuracy of k-NN with k={k}:{accuracy:.2f}') 


# In[14]:


import numpy as np 
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelEncoder

#Load the breast cancer dataset
data=load_breast_cancer()
X=data.data #Features
y=data.target #Target(labels) 

#Split the dataset into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42) 

#Initialize the k-NN classifier with a specified value of k
k=3 #You can change this value as needed
knn=KNeighborsClassifier(n_neighbors=k)

#Fit the model on the training data
knn.fit(X_train,y_train) #Make predictions on the test data
y_pred=knn.predict(X_test)

#Calculate the accuracy of the model 
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy of k-NN with k={k}:{accuracy:.2f}') 


# In[16]:


import numpy as np
import pandas as pd 
# from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder 

data = pd.read_csv('food.csv') 
X = data.iloc[:, :3]
# print(X) 
y= data.iloc[:, 3] 

le = LabelEncoder() 
categorical_columns = ['Ingredient']  

for col in categorical_columns:
    X[col] = le.fit_transform(X[col])
y = le.fit_transform(y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
k=3 
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train,y_train) 
y_pred = knn.predict(X_test) 

sample=[[1,10,9]]
k=knn.predict(sample) 
print(k) 
accuracy = accuracy_score(y_test,y_pred) 
print(accuracy) 


# In[18]:


import numpy as np 
import pandas as pd 
# from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score 

data = pd.read_csv('insurance.csv')
X = data.iloc[:, :6] 
# print(X) 
y= data.iloc[:, 1] 

le = LabelEncoder() 
categorical_columns = ['sex', 'smoker', 'region']   
for col in categorical_columns:
    X[col] = le.fit_transform(X[col])

y = le.fit_transform(y)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42) 

k=3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test) 
sample=[[1,10,9,11,4,2]] 
k=knn.predict(sample) 

print(k) 
accuracy = accuracy_score(y_test,y_pred) 
print(accuracy)  


# In[19]:


import numpy as np
import pandas as pd
# from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('cricket.csv') 
X = data.iloc[:, :5] 
# print(X)
y= data.iloc[:, 4]
# print(y) 

le = LabelEncoder()
categorical_columns = ['Outlook','Temp','Humidity','Windy','Play Cricket'] 
for col in categorical_columns:
    X[col] = le.fit_transform(X[col])

y = le.fit_transform(y)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

k=3 
knn = KNeighborsClassifier(n_neighbors=k) 
knn.fit(X_train,y_train) 
y_pred = knn.predict(X_test) 
sample=[[1,10,9,11,4]] 
k=knn.predict(sample) 
print(k)
accuracy = accuracy_score(y_test,y_pred) 
print(accuracy) 


# In[ ]:




