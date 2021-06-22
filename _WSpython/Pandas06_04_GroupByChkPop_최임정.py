
# coding: utf-8

# In[19]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[20]:


uniqueList=df['year'].unique()
for idx in uniqueList:
    yearList=df[df['year'] == idx]
    print(yearList['pop'].mean())

