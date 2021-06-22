
# coding: utf-8

# In[2]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv',sep='\t')
df.head(10)


# In[3]:


df.groupby('year')['lifeExp'].mean()


# In[4]:


df['year'].unique()


# In[5]:


unList=df['year'].unique()
type(unList)


# In[6]:


unList

