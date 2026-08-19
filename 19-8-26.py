#!/usr/bin/env python
# coding: utf-8

# In[43]:


from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
iris=load_iris()
X=iris.data
y=iris.target
print(iris.feature_names)
print(iris.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_train,y_train) 
y_predict=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_predict)
print(accuracy)
print(f'{accuracy:.2f}')
new=[[1.2,2.2,3.2,3.4]]
new_predict=knn.predict(new)
print(new_predict)
print(iris.target_names[new_predict])


# In[45]:


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
iris=load_breast_cancer()
X=iris.data
y=iris.target
print(iris.feature_names)
print(iris.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3) 
knn.fit(X_train,y_train) 
y_predict=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_predict)
print(accuracy)
print(f'{accuracy:.2f}')


# In[ ]:




