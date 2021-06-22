
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[2]:


print(df.head(3), "\n======")
multi_group_var=df.groupby(['year','continent'])['lifeExp','gdpPercap'].mean()
print(multi_group_var)


# In[4]:


uniqueyear=df['year'].unique()
uniquecont=df['continent'].unique()
for idx in uniqueyear:
    print(idx)
    yearList=df[df['year'] == idx]
    for i in uniquecont:
        contList=yearList[df['continent'] == i]
        print(i, contList['lifeExp'].mean(), end = ' ')
        print("\t", contList['gdpPercap'].mean())

