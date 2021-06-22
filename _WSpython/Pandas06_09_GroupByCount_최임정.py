
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[2]:


print(df.groupby('continent')['country'])


# In[5]:


print(df.groupby('continent')['country'].nunique())
print(df.groupby('continent')['country'].unique())
print(df.groupby('continent')['country'].nunique()['Oceania'])
print(df.groupby('continent')['country'].count())
print(df.groupby('continent')['country'].count()['Africa'])

