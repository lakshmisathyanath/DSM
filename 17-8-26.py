#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
a={'roll':[1,2,3,4],
'name':["ammu","achu","manu","paru"]
}
d=pd.DataFrame(a)
print (d)


# In[13]:


import pandas as pd
a=[1,2,3,4]
b=pd.Series(a, index=["a","b","c","d"])
c={'roll':[1,2,3,4],
'name':["ammu","achu","manu","paru"]}
d=pd.DataFrame(c)
print( d.loc[0])


# In[25]:


import pandas as pd
a=pd.read_csv('test.csv')
b=a.dropna()
print(b)


# In[ ]:


import pandas as pd
a=pd.read_csv('test.csv')
print(a)
b=a.dropna()
print(b)

