
# coding: utf-8

# In[9]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[13]:


uniqueyear=df['year'].unique()
uniquecont=df['continent'].unique()
print(uniqueyear)
print(uniquecont)


# In[22]:


for idx in uniqueyear:
    print(idx)
    yearList=df[df['year'] == idx]
    for i in uniquecont:
        contList=yearList[df['continent'] == i]
        print(i, contList['lifeExp'].mean(), end = ' ')
        print("\t", contList['gdpPercap'].mean())

