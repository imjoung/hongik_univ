
# coding: utf-8

# In[15]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv',sep='\t')
unList=df['continent'].unique()


# In[16]:


df.groupby('continent')['year'].count()


# In[22]:


for continent in unList:
    con=df[df['continent'] == continent]
    print(continent,con["year"].count())
    

