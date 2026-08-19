#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
a=np.array([[2,4],[6,3]]);
b=np.array([[4,5],[7,8]]);
print("addition =\n",a+b)
print()
print("substraction=\n",a-b)
print()
print("Multiplication=\n",np.dot(a,b))
print()
print("division =\n",a/b)


# In[ ]:


import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[5,7],[9,4]])
u,s,vt=np.linalg.svd(x)
n_components=2


# In[17]:


import matplotlib.pyplot as plt
x=[3,5,6,8]
y=[1,4,6,8]
plt.plot(x,y)
plt.title("bloody graph")
plt.xlabel("petal length")
plt.ylabel("petal width")


# In[20]:


import matplotlib.pyplot as plt
subjects=["maths","english","social"]
marks=[60,70,40]
plt.bar(subjects,marks)
plt.title("Report")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[26]:


import matplotlib.pyplot as plt
subjects=["maths","english","social"]
marks=[60,70,40]
plt.scatter(subjects,marks)
plt.title("Report")
plt.xlabel("subjects")
plt.ylabel("marks")




# In[30]:


import matplotlib.pyplot as plt
marks=[60,55,40,30,10]
plt.hist(marks)
plt.title("Report")
plt.xlabel("mark")
plt.ylabel("range")


# In[40]:


import matplotlib.pyplot as plt
subjects=["maths","english","social"]
marks=[60,70,40]
plt.pie(marks,labels=subjects)
plt.show()


# In[42]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,"r:o")


# In[43]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y)
plt.bar(x,y)


# In[ ]:





# In[ ]:




