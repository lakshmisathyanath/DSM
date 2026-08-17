#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
ls=[10,20,30]
series=pd.Series(ls)
print(series)


# In[3]:


import pandas as pd
date=pd.date_range(start="2024-11-20",end="2024-11-24")
series=pd.Series(date)
print(series)


# In[11]:


import pandas as pd
data={'roll':[1,2,3,4],'name':["ammu","achu","paru","manu"]}
df=pd.DataFrame(data)
print(df)


# In[12]:


import pandas as pd
data={'roll':[1,2,3,4],'name':["ammu","achu","paru","manu"],'mark':[30,40,22,50]}
df=pd.DataFrame(data)
print(df)


# In[19]:


import pandas as pd
data=pd.DataFrame({'roll':[1,2,3,4],'name':["ammu","achu","paru","manu"],'mark':[30,40,22,50]})
print("head of data frame\n")
print(data.head())
print("\ntail of data frame \n",data.tail())


# In[20]:


import pandas as pd
data={'roll':[1,2,3,4],'name':["ammu","achu","paru","manu"],'mark':[30,40,22,50]}
df=pd.DataFrame(data)
select=df.loc[0:2]
print(select)


# In[21]:


import pandas as pd
data={'roll':[1,2,3,4],'name':["ammu","achu","paru","manu"],'mark':[30,40,22,50]}
df=pd.DataFrame(data)
fill=df.fillna(0)
print(fill)


# In[ ]:




