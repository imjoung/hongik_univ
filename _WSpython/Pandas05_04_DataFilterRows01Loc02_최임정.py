
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.DataFrame([[1,2],[4,5],[7,8]],
                index = ['cobra','viper','sidewinder'],
                columns=['max_speed','shield'])
df


# In[2]:


df.loc[['viper','sidewinder'],['shield']] = 50
df


# In[3]:


df.loc['cobra']=10
df


# In[4]:


df.loc[:,'max_speed']=30
df


# In[5]:


df.loc[df['shield']>35] = 0
df


# In[7]:


df=pd.DataFrame([[1,2],[4,5],[7,8]],
               index=[7,8,9],columns=['max_speed','shield'])
df


# In[11]:


df.loc[7:9,'shield']

