
# coding: utf-8

# In[4]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[5]:


uniqueList=df['continent'].unique()
for idx in uniqueList:
    yearList=df[df['continent'] == idx]
    print(yearList['lifeExp'].mean())


# In[6]:


grouped_country_df=df.groupby('continent')
grouped_country_df["lifeExp"].mean()

