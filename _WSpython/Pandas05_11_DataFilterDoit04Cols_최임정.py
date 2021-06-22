
# coding: utf-8

# In[1]:


import pandas
df= pandas.read_csv('../data/gapminder.tsv',sep='\t')
df.head(3)


# In[2]:


subset=df.loc[:,['year','pop']]
subset.head()


# In[3]:


subset=df.iloc[:,[2,4,-1]]
print(subset.head())

