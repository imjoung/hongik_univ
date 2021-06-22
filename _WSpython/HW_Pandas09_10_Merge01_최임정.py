
# coding: utf-8

# In[6]:


import pandas as pd

df1=pd.DataFrame({'a':['foo','bar'],'b':[1,2]})
df2=pd.DataFrame({'a':['foo','baz'],'c':[3,4]})
df1


# In[7]:


df1.merge(df2,how='inner',on='a')


# In[8]:


df1.merge(df2,how='left',on='a')


# In[10]:


df1.merge(df2,how='right',on='a')

