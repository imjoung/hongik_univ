
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('../data/gapminder.tsv','\t')


# In[2]:


multi_group_var=df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print(multi_group_var.mean())
print(multi_group_var.mean().count())

