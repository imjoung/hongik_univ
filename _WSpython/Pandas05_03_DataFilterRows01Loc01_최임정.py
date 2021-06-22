
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.DataFrame([[1,2],[4,5],[7,8]],
                index = ['cobra','viper','sidewinder'],
                columns=['max_speed','shield'])
df


# In[2]:


df.loc['viper']


# In[3]:


df.loc['cobra','shield']


# In[4]:


df.loc['cobra':'viper','max_speed']


# In[5]:


df.loc[[False,False,True]] #라벨3개중 true인 것만 출력


# In[6]:


df.loc[df['shield']>6]


# In[7]:


df.loc[df['shield'] >6, ['max_speed']]

