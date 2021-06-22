
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('../data/gapminder.tsv',sep='\t')


# In[2]:


country_df=df['country']
type(country_df)


# In[3]:


country_df.head())


# In[4]:


country_df.tail()


# In[5]:


subset = df[['country','continent','year']]
type(subset)


# In[6]:


subset.head()


# In[7]:


subset.tail()

