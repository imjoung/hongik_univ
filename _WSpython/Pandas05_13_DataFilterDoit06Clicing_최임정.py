
# coding: utf-8

# In[1]:


import pandas
df= pandas.read_csv('../data/gapminder.tsv',sep='\t')
df.head(3)


# In[2]:


df.iloc[[0,99,999],[0,3,5]]


# In[3]:


df.loc[[0,99,999],['country','lifeExp','gdpPercap']]


# In[4]:


df.loc[10:13,['country','lifeExp','gdpPercap']]


# In[5]:


df.iloc[10:13,[0,3,-1]]

