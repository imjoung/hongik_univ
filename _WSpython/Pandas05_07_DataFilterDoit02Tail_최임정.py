
# coding: utf-8

# In[1]:


import pandas as pd
df= pd.read_csv('../data/gapminder.tsv',sep='\t')


# In[3]:


number_of_rows=df.shape[0]
number_of_rows


# In[4]:


last_row_index=number_of_rows-1
df.loc[last_row_index]


# In[5]:


df.loc[len(df)-1]


# In[7]:


df.tail(n=1)


# In[8]:


df.tail(n=2)


# In[9]:


df.loc[[0,99,999]]

